/**
 * 局部重绘按钮及弹窗
 */

import { Button, Tooltip, App } from "antd";
import imageIcon from "./../../../../../assets/images/pages/boardView/image_hover_icon.svg";
import imageHoverIcon from "./../../../../../assets/images/pages/boardView/image_icon.svg";
import { ImageGenerateHistoryItem } from "./../../../../libs/interfaces";
import { ShotResource } from "./../../../../types/storyboard";

import React, { useContext, useState } from "react";

import { createPortal } from "react-dom";
import { useTranslation } from "react-i18next";
import ModalBase from "../ModalBase";
import drawHelper from "./../../../../libs/draw-helper";
import CanvasEditor from "../../Editor/CanvasEditor";

import {
  DetailContexts,
  IDetailContexts,
} from "../DetailContainer/contexts/detail-contexts";

import projectApi from "./../../../../api/projectApi";
import {
  EditorApiContexts,
  IEditorApiContexts,
} from "./../../../../contexts/editor-api-contexts";

interface IProps {
  boardId: string; // 故事板id
  setSelectShotResource: (source: ShotResource) => void;
}

const PartialRedrawBtn: React.FC<IProps> = ({
  boardId,
  setSelectShotResource,
}: IProps) => {
  const { t } = useTranslation();
  const detailContexts: IDetailContexts =
    useContext<IDetailContexts>(DetailContexts);

  const [isModalOpen, setIsModalOpen] = React.useState<boolean>(false);
  const [imageGenerateHistoryList, setImageGenerateHistoryList] = useState<
    ImageGenerateHistoryItem[]
  >([]);

  //初始化选取的id
  const [initCheckedId, setInitCheckedId] = useState<string>();

  const modalWidth = 1400;
  const modalHeight = 960;

  // 将 modalWidth 移到 state 中，只在组件挂载时计算一次
  // const [modalWidth] = useState(() => {
  //   const winWidth = drawHelper.getWinW();
  //   // if (winWidth <= 1024) return 1024;
  //   // if (winWidth >= 1400) return 1400;
  //   // return winWidth;
  //   if (winWidth >= 1400) {
  //     return 1400;
  //   }else{
  //     return 1024;
  //   }
  // });

  // const [modalHeight] = useState(() => {
  //   const winHeight = drawHelper.getWinH();
  //   // if (winHeight <= 833) return 702;
  //   // if (winHeight >= 1091) return 960;
  //   // return winHeight - 131;
  //   if (winHeight >= 1091) {
  //     return 960;
  //   }else{
  //     return 702;
  //   }
  // });

  const { message: messageApi } = App.useApp();

  const getImageGenerateHistory = async () => {
    const res = await projectApi.getImageGenerateHistory({
      projectId: detailContexts.projectItemObj?.id,
      storyboardId: boardId,
    });
    if (res.success && res.result?.code === 0) {
      setImageGenerateHistoryList(res.result.data);
      const history = res.result.data.find(
        (history: ImageGenerateHistoryItem) => history.selected === true
      );
      setInitCheckedId(history?.id);
      setIsModalOpen(true);
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };

  const applyHistoryImage = async (resourceId: string) => {
    if (resourceId === initCheckedId) {
      return;
    }

    const res = await projectApi.applyHistoryImage({
      projectId: detailContexts.projectItemObj?.id,
      storyboardId: boardId,
      targetId: resourceId,
    });
    if (res.success && res.result?.code === 0) {
      if (res.result?.data) {
        messageApi.success(res.result.msg);
        setSelectShotResource(res.result?.data);
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
  return (
    <>
      <Tooltip placement="top" title={t("partial_redraw")}>
        <Button
          icon={
            <div className="relative w-6 h-6 flex items-center justify-center">
              <img
                src={imageIcon}
                alt="preview"
                className="absolute inset-0 m-auto opacity-100 transition-opacity duration-200 group-hover:opacity-0"
              />
              <img
                src={imageHoverIcon}
                alt="preview hover"
                className="absolute inset-0 m-auto opacity-0 transition-opacity duration-200 group-hover:opacity-100"
              />
            </div>
          }
          className="bg-white/80 group"
          onClick={showModal}
        />
      </Tooltip>
      {createPortal(
        <ModalBase
          open={isModalOpen}
          onCancel={handleModalCancel}
          width={modalWidth}
          height={modalHeight}
          showFooter={false}
          footer={null}
        >
          <EditorApiContexts.Provider value={{} as IEditorApiContexts}>
            <div className="w-auto flex flex-col gap-4 px-6 pt-6">
              <div className="space-y-1.5">
                <div className="text-lg font-semibold text-center">
                  {t("partial_redraw")}
                </div>
              </div>
              <CanvasEditor
                storyboardId={boardId}
                outerHistoryItems={imageGenerateHistoryList}
                applyHistoryImage={applyHistoryImage}
              />
            </div>
          </EditorApiContexts.Provider>
        </ModalBase>,
        document.body
      )}
    </>
  );
};

export default PartialRedrawBtn;
