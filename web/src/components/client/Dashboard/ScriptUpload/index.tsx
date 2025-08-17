/**
 * 上传剧本
 */

import { Button, UploadFile, App } from "antd";
import deleteIcon from "./../../../../../assets/images/icons/delete_icon.svg";
import fileUploadIcon from "./../../../../../assets/images/icons/file_upload_icon.svg";
import {
  CreateNewContexts,
  ICreateNewContexts,
} from "./../../../../contexts/create-new-contexts";
import fileUploadHelper from "./../../../../libs/file-upload-helper";
import { 
  DOCX_ICON_BASE64_SRC,
  PDF_ICON_BASE64_SRC,
  XLSX_ICON_BASE64_SRC,
  TXT_ICON
} from "./../dashboard-config";

import React, { useContext, useState, lazy } from "react";
import { useTranslation } from "react-i18next";

const fileTypeIconMaps = {
  ["docx"]: DOCX_ICON_BASE64_SRC,
  ["pdf"]: PDF_ICON_BASE64_SRC,
  ["xlsx"]: XLSX_ICON_BASE64_SRC,
  ["txt"]: TXT_ICON,
};

import FileUpload from "../../Common/FileUpload";

interface IProps {}

const ScriptUpload: React.FC<IProps> = ({}: IProps) => {
  const { t } = useTranslation();
  const { message: messageApi } = App.useApp();
  const createNewContexts: ICreateNewContexts = useContext<ICreateNewContexts>(CreateNewContexts);
  const [fileType, setFileType] = useState<string | null>(null);

  const onFileListChange = (fileList: UploadFile[]) => {
    if (fileList.length > 0) {
      const file = fileList[0];

      const size = file.size;
      if (size > 5 * 1024 * 1024) {
        messageApi.error(t("file_size_limit_5m"));
        createNewContexts.setUploadScriptFile(null);
        return;
      }

      createNewContexts.setUploadScriptFile(file);

      const fileType = file.name.split(".")[1];
      setFileType(fileType);
    } else {
      createNewContexts.setUploadScriptFile(null);
    }
  };

  return (
    <div className="mt-4">
      {createNewContexts.uploadScriptFile ? (
        <>
          <div className="border rounded-lg h-[72px] p-4 flex justify-between mt-4">
            <div className="flex justify-between w-full">
              <div className="flex items-center">
                <img
                    src={
                      fileTypeIconMaps[
                        fileType as keyof typeof fileTypeIconMaps
                      ]
                    }
                    className="w-10 h-10"
                    alt=""
                  />
                <div className="text-sm ml-3">
                  <h2 className="text-slate-700">
                    {createNewContexts.uploadScriptFile.name}
                  </h2>
                  <div className="text-slate-600 flex">
                    {fileUploadHelper.formatFileSize(
                      createNewContexts.uploadScriptFile.size
                    )}
                  </div>
                </div>
              </div>
              <Button
                type="text"
                icon={<img src={deleteIcon} alt="" />}
                onClick={() => {
                  createNewContexts.setUploadScriptFile(null);
                }}
              />
            </div>
          </div>
        </>
      ) : (
        <FileUpload
          originNode={
            <div className="border rounded-lg p-4 relative cursor-pointer">
              <div className="flex flex-col items-center">
                <div className="w-10 h-10 border rounded-lg flex justify-center items-center">
                  <img src={fileUploadIcon} alt="" />
                </div>
                <p className="text-xs mt-3 text-center text-slate-600">
                  <span className="mr-1 text-violet-500 font-semibold">
                    {t("click_to_upload")}
                  </span>
                  {t("select_local_file")}
                  <br />
                  {t("supported_file_types")}
                </p>
              </div>
            </div>
          }
          onFileListChange={onFileListChange}
          listType="picture"
          accept="text/plain,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
          showUploadList={false}
        />
      )}
    </div>
  );
};

export default ScriptUpload;
