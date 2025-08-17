/**
 * 历史画面
 */

import { Button, App, Tooltip, UploadFile } from "antd";
import replaceIcon from "./../../../../../assets/images/pages/boardView/replace_icon.svg";
import replaceIconHover from "./../../../../../assets/images/pages/boardView/replace_icon_hover.svg";
import projectApi from "./../../../../api/projectApi";
import { ShotResource } from "./../../../../types/storyboard";

import React, { useContext } from "react";
import { useTranslation } from "react-i18next"; // 添加 useTranslation 导入
import {
  DetailContexts,
  IDetailContexts,
} from "../DetailContainer/contexts/detail-contexts";
import FileUpload from "../FileUpload";
import style from "./style.module.css";

interface IProps {
  boardId: string;
  setSelectShotResource : (source: ShotResource) => void;
  setIsRegenerating: (isRegenerating: boolean) => void;
  setLoadingText: (loadingText: string) => void;
}

const StoryboardReplaceImg: React.FC<IProps> = ({
  boardId,
  setSelectShotResource,
  setIsRegenerating,
  setLoadingText,
}: IProps) => {
  const { t } = useTranslation(); // 添加 useTranslation hook
  const detailContexts: IDetailContexts = useContext<IDetailContexts>(DetailContexts);
  const { message: messageApi } = App.useApp();

  const fileToBase64 = (file: File): Promise<string> => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => resolve(reader.result as string);
      reader.onerror = error => reject(error);
    });
  } 
  // 替换图片
  const replaceImage = async (file: File) => {

    const size = file.size;
    if (size > 5 * 1024 * 1024) {
      messageApi.error(t("file_size_limit_5m"));
      return;
    }

    setLoadingText(t("image_replacing"));
    setIsRegenerating(true);

    // 将文件转换为base64
    const base64Data = await fileToBase64(file);

    const res = await projectApi.replaceImage({
      shotId: boardId,
      projectId: detailContexts.projectItemObj?.id,
      fileData: base64Data,
      fileName: file.name,
    });
    setIsRegenerating(false);
    if (res.success && res.result?.code === 0) {
      if (res.result?.data) {
        setSelectShotResource(res.result?.data);
      }
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };

  const onFileListChange = (fileList: UploadFile[]) => {
    
    if (fileList.length > 0) {
      const file = fileList[0];
      replaceImage(file.originFileObj as File);
    } else {
      // 用户取消了文件选择，可以在这里执行其他操作
    }
  };


  return (
    <div className={style.replaceImageFileUploadWrapper}>
      {/* {isShowModal && (
        <div 
          className="fixed inset-0 bg-red bg-opacity-50 z-[10000]"
        />
      )} */}
      <FileUpload
        originNode={
          <Tooltip placement="top" title={t("replace_image")}>
            <Button className="disabled:bg-white/70 w-8 relative overflow-hidden bg-white/80 group">
              <div className="relative w-full h-full">
                <img
                  className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 block group-hover:opacity-0"
                  style={{ maxWidth: "none" }}
                  src={replaceIcon}
                  alt="replace"
                />
                <img
                  className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 block opacity-0 group-hover:opacity-100"
                  style={{ maxWidth: "none" }}
                  src={replaceIconHover}
                  alt="replace hover"
                />
              </div>
            </Button>
          </Tooltip>
        }
        onFileListChange={onFileListChange}
        accept="image/jpeg,image/png,image/jpg"
        showUploadList={false}
      />
    </div>
  );
};

export default StoryboardReplaceImg;
