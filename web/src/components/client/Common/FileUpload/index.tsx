import type { UploadFile, UploadProps } from "antd";
import { Upload, message, App } from "antd";
import { UploadListType } from "antd/es/upload/interface";
import React, { useState } from "react";
import style from "./style.module.css";
import { useTranslation } from "react-i18next";

interface IFileUploadProps {
  className?: string;
  listType?: UploadListType;
  originNode?: React.ReactNode;
  onUploadFileChange?: (file: File) => void;
  onFileListChange?: (fileList: UploadFile[]) => void;
  action?: string;
  onBeforeUpload?: (file: File) => Promise<boolean>;
  accept?: string;
  progress?: React.CSSProperties;
  maxFileSize?: number;
  showUploadList?: boolean;
  onPreview?: (file: UploadFile) => void;
}
const FileUpload: React.FC<IFileUploadProps> = ({
  originNode,
  listType = "picture-circle",
  onUploadFileChange,
  onFileListChange,
  // onBeforeUpload = async (file: File) => {
  //   const isLt5M = file.size / 1024 / 1024 <= 5;
  //   if (!isLt5M) {
  //     message.error("请选择不大于 5M 的文件");
  //   }
  //   return isLt5M;
  // },
  accept,
  showUploadList,
  onPreview,
}) => {
  const [fileList, setFileList] = useState<UploadFile[]>([]);
  const { t } = useTranslation();
  const { message: messageApi } = App.useApp();

  const onChange: UploadProps["onChange"] = ({ fileList: newFileList }) => {
    setFileList(newFileList);
    onFileListChange && onFileListChange(newFileList);
  };

  const beforeUpload = async (file: File) => {
    // const isValid = await onBeforeUpload(file);
    // if (isValid) {
    //   onUploadFileChange && onUploadFileChange(file);
    // }
    return false;
  };

  return (
    <Upload
      className={style.fileUploadWrapper}
      accept={accept || "image/*"}
      listType={listType}
      fileList={fileList}
      onChange={onChange}
      maxCount={1}
      multiple={false}
      beforeUpload={beforeUpload}
      showUploadList={showUploadList ? true : false}
      style={{ width: "100%" }}
      onPreview={onPreview}
    >
      {originNode ? originNode : null}
    </Upload>
  );
};

export default FileUpload;
