/**
 * 人脸参考弹窗内容
 */

import projectApi from "./../../../../api/projectApi";

import faceReferPhotoImage1 from "./../../../../../assets/images/pages/roleView/Photo01.min-sbSsjjLI.png";
import faceReferPhotoImage2 from "./../../../../../assets/images/pages/roleView/Photo02.min-DnQLtC4E.png";
import faceReferPhotoImage3 from "./../../../../../assets/images/pages/roleView/Photo03.min-CuUS1ImY.png";
import faceReferPhotoImage4 from "./../../../../../assets/images/pages/roleView/Photo04.min-CH1vpAKR.png";
import correctIcon from "./../../../../../assets/images/pages/roleView/correct_icon.svg";
import errorIcon from "./../../../../../assets/images/pages/roleView/error_icon.svg";

import fileUploadIcon from "./../../../../../assets/images/icons/file_upload_icon.svg";
import { App, UploadFile } from "antd";
import { useTranslation } from "react-i18next";

import React, { useContext } from "react";
import FileUpload from "../../Common/FileUpload";
import {
  IRoleViewContexts,
  RoleViewContexts,
} from "../../../../contexts/role-view-contexts";
import style from "./style.module.css";

interface IProps {}

const FaceReferContent: React.FC<IProps> = ({}: IProps) => {
  const { t } = useTranslation();
  const { message: messageApi } = App.useApp();

  const FACE_REFER_PHOTO_EXAMPLES = [
    {
      id: 1,
      imageSrc: faceReferPhotoImage1,
      desc: t("clear_features"),
      icon: correctIcon,
    },
    {
      id: 2,
      imageSrc: faceReferPhotoImage2,
      desc: t("not_front"),
      icon: errorIcon,
    },
    {
      id: 3,
      imageSrc: faceReferPhotoImage3,
      desc: t("face_blocked"),
      icon: errorIcon,
    },
    {
      id: 4,
      imageSrc: faceReferPhotoImage4,
      desc: t("photo_blurry"),
      icon: errorIcon,
    },
  ];

  const roleViewContexts = useContext<IRoleViewContexts>(RoleViewContexts);

  const fileToBase64 = (file: File): Promise<string> => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => resolve(reader.result as string);
      reader.onerror = error => reject(error);
    });
  }

  const onFileListChange = (fileList: UploadFile[]) => {
    if (fileList.length > 0) {
      const file = fileList[0];
      uploadExampleFigure(file.originFileObj as File);
    } else {
      roleViewContexts.setUploadExampleFigureImg("");
    }
  };

  const uploadExampleFigure = async (file: File) => {
    // 将文件转换为base64
    const base64Data = await fileToBase64(file);

    const res = await projectApi.uploadExampleFigure({
      projectId: roleViewContexts.projectId,
      fileData: base64Data,
      fileName: file.name,
    });

    if (res.result.code === 0) {
      roleViewContexts.setUploadExampleFigureImg(res.result.data);
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };
  return (
    <div className={style.faceReferContentWrapper}>
      <div className="mt-8">
        <FileUpload
          originNode={
            <div
              style={{
                background: "white",
                border: "1px solid rgb(229, 231, 235)",
                marginBottom: 32,
                padding: 16,
                marginTop: 8,
                borderRadius: 8,
                width: "100%",
              }}
            >
              <div className="flex flex-col items-center py-1.5">
                <div className="w-10 h-10 border rounded-lg flex justify-center items-center">
                  <img src={fileUploadIcon} alt="" />
                </div>
                <p className="text-xs mt-3 text-center">
                  <span className="mr-1 text-violet-500">{t("faceReferContent_upload_click_or_drag")}</span>
                  {t("faceReferContent_upload_description")}
                  <br />
                  {t("faceReferContent_upload_format_info")}
                </p>
              </div>
            </div>
          }
          onFileListChange={onFileListChange}
          listType="picture-card"
          accept="image/png,image/jpeg,image/webp"
          showUploadList={true}
        />
      </div>
      <div className="mt-8">
        <h2>{t("faceReferContent_examples_title")}</h2>
        <ul className="mt-1 grid grid-cols-4 gap-5">
          {Array.isArray(FACE_REFER_PHOTO_EXAMPLES) &&
          FACE_REFER_PHOTO_EXAMPLES.length > 0
            ? FACE_REFER_PHOTO_EXAMPLES.map((item, index) => (
                <li key={`face-refer-photo-example-${item.id}-${index}`}>
                  <img
                    className="w-36 h-36 rounded-lg overflow-hidden bg-neutral-200"
                    src={item.imageSrc}
                    alt=""
                  />
                  <div className="flex justify-center mt-2">
                    <img src={item.icon} alt="" className="mr-1" />
                    <span className="text-xs">{item.desc}</span>
                  </div>
                </li>
              ))
            : null}
        </ul>
        <p className="text-sm text-slate-500 mt-3">
          {t("faceReferContent_examples_privacy_notice")}
        </p>
      </div>
    </div>
  );
};

export default FaceReferContent;
