/**
 * 历史画面
 */

import { Button, App, Tooltip } from "antd";
import historyIcon from "./../../../../../assets/images/pages/boardView/history_icon.svg";
import historyIconHover from "./../../../../../assets/images/pages/boardView/history_icon_hover.svg";
import {
  ImageGenerateHistoryItem,
} from "./../../../../libs/interfaces";


import React, { useContext, useState } from "react";
import { createPortal } from "react-dom";
import { useTranslation } from "react-i18next"; // 添加 useTranslation 导入
import {
  DetailContexts,
  IDetailContexts,
} from "../DetailContainer/contexts/detail-contexts";
import ModalBase from "../ModalBase";
import StoryboardImgHistoryContent from "../StoryboardImgHistoryContent";
import projectApi from "./../../../../api/projectApi";
import { ShotResource } from "./../../../../types/storyboard";

interface IProps {
  boardId: string;
  setSelectShotResource : (source: ShotResource) => void;
  setIsRegenerating: (isRegenerating: boolean) => void;
  setLoadingText: (loadingText: string) => void;
}

const StoryboardImgHistory: React.FC<IProps> =  ({
  boardId,
  setSelectShotResource,
  setIsRegenerating,
  setLoadingText,
}: IProps) => {
  const { t } = useTranslation(); // 添加 useTranslation hook
  const detailContexts: IDetailContexts = useContext<IDetailContexts>(DetailContexts);
  const [isModalOpen, setIsModalOpen] = React.useState<boolean>(false);
  const [imageGenerateHistoryList, setImageGenerateHistoryList] = useState< ImageGenerateHistoryItem[] >([]);
  const [checkedImageGenerateHistory, setCheckedImageGenerateHistory] = useState<ImageGenerateHistoryItem>();

  //初始化选取的id
  const [initCheckedId, setInitCheckedId] = useState<string>();

  const { message: messageApi } = App.useApp();

  const getImageGenerateHistory = async () => {
    const res = await projectApi.getImageGenerateHistory({
      projectId: detailContexts.projectItemObj?.id,
      storyboardId: boardId,
    });
    if (res.success && res.result?.code === 0) {
      setImageGenerateHistoryList(res.result.data);
      const history = res.result.data.find( (history: ImageGenerateHistoryItem) => history.selected === true );
      setCheckedImageGenerateHistory(history);
      setInitCheckedId(history?.id);
      setIsModalOpen(true);
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };

  const applyHistoryImage = async () => {
    if (checkedImageGenerateHistory?.id === initCheckedId) {
      return;
    }

    setLoadingText(t("image_replacing"));
    setIsRegenerating(true);

    const res = await projectApi.applyHistoryImage({
      projectId: detailContexts.projectItemObj?.id,
      storyboardId: boardId,
      targetId:checkedImageGenerateHistory?.id,
    });
    setIsRegenerating(false);
    if (res.success && res.result?.code === 0) {
      if (res.result?.data) {
        setSelectShotResource(res.result?.data);
        messageApi.success(t("apply_shot_image_success"));
      }
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };

  const showModal = () => {
    getImageGenerateHistory();
  };
  const handleModalCancel = async () => {
    setIsModalOpen(false);
  };
  const handleModalOk = async () => {
    setIsModalOpen(false);
    applyHistoryImage();
  };
  return (
    <>
      <Tooltip placement="top" title={t("image_history")}>
        <Button
          onClick={showModal}
          className="disabled:bg-white/70 bg-white/80 group"
          icon={
            <div className="relative w-6 h-6">
              <img
                src={historyIcon}
                alt="history"
                className="absolute top-1/2 -translate-y-1/2 left-1/2 -translate-x-1/2 inset-0 transition-opacity duration-200 group-hover:opacity-0"
              />
              <img
                src={historyIconHover}
                alt="history hover"
                className="absolute top-1/2 -translate-y-1/2 left-1/2 -translate-x-1/2 inset-0 opacity-0 transition-opacity duration-200 group-hover:opacity-100"
              />
            </div>
          }
        />
      </Tooltip>
      {createPortal(
        <ModalBase
          open={isModalOpen}
          onOk={handleModalOk}
          onCancel={handleModalCancel}
          okText={t("apply_shot_image_confirm")}
          cancelText={t("cancel")}
          width={848}
          height={674}
        >
          <StoryboardImgHistoryContent
            imageGenerateHistoryList={imageGenerateHistoryList}
            checkedImageGenerateHistory={checkedImageGenerateHistory}
            setCheckedImageGenerateHistory={setCheckedImageGenerateHistory}
          />
        </ModalBase>,
        document.body
      )}
    </>
  );
};

export default StoryboardImgHistory;
