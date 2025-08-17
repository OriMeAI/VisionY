/**
 * 查看历史形象按钮及弹窗
 */

import { RoleImageHistoryItem } from "@/src/libs/interfaces";
import viewHistoryIcon from "./../../../../../assets/images/pages/roleView/view_history_icon.svg";
import { Checkbox,Button } from "antd";
import { useTranslation } from "react-i18next";
import { createPortal } from "react-dom";
import ImagePreview from "../../Common/ImagePreview";

import React, { useState } from "react";
import DefaultRoleItemImg from "../DefaultRoleItemImg";

import previewIcon from "./../../../../../assets/images/pages/boardView/preview_icon.svg";
import previewIconHover from "./../../../../../assets/images/pages/boardView/preview_icon_hover.svg";

interface IProps {
  checkedRoleImageHistory?: RoleImageHistoryItem;
  roleImageHistoryList?: RoleImageHistoryItem[];
  setCheckedImageHistory: (item: RoleImageHistoryItem) => void;
}

const ViewHistoryImagesContent: React.FC<IProps> = ({
  checkedRoleImageHistory,
  roleImageHistoryList,
  setCheckedImageHistory,
}: IProps) => {
  const { t } = useTranslation();
  // 预览图片
  const [previewImageVisible, setPreviewImageVisible] = useState<boolean>(false);


  return (
    <div>
      <div className="px-6 pt-6 pb-5">
        <div className="flex space-x-4">
          <div className="border h-12 w-12 rounded-lg flex items-center justify-center">
            <img src={viewHistoryIcon} alt={t("viewHistoryImages_title")} />
          </div>
          <div>
            <h2 className="text-gray-900 text-lg font-semibold">
              {t("viewHistoryImages_header_title")}
            </h2>
            <p className="text-slate-600 text-sm ">
              {t("viewHistoryImages_header_subtitle")}
            </p>
          </div>
        </div>
      </div>
      <div className="h-[494px] flex px-6 pt-6 border-t">
        <div className="flex space-x-5 w-full">
        <div className="border flex-1 rounded-lg">
            <h2 className="px-5 py-4 text-slate-700 text-sm font-medium">
              {t("viewHistoryImages_history_title")}
            </h2>
            <div className="h-[401px] overflow-auto">
              <ul className="px-4 grid grid-cols-4 gap-4">
                {Array.isArray(roleImageHistoryList) &&
                roleImageHistoryList.length > 0
                  ? roleImageHistoryList.map((item, index) => {
                      return (
                        <li
                          key={`role-image-history-${item.id}-${index}`}
                          className={`"w-[122px] h-[220px] relative ${
                            checkedRoleImageHistory?.id === item.id
                              ? "border"
                              : ""
                          } rounded-lg overflow-hidden flex items-center justify-center bg-background`}
                          onClick={() => {
                            setCheckedImageHistory(item);
                          }}
                        >
                          <div className="w-full h-full overflow-hidden">
                            <img
                              src={item.url}
                              className="w-full h-full transition duration-300 ease-in-out scale-110 object-cover"
                              alt=""
                            />
                          </div>
                          {checkedRoleImageHistory?.id === item.id ? (
                            <div className="absolute inset-0 w-full h-full border-2 border-primary rounded-lg z-10 transition duration-300 ease-in-out opacity-100">
                              <Checkbox
                                checked={true}
                                className={`absolute top-0.5 right-1 z-10`}
                              />
                            </div>
                          ) : null}
                        </li>
                      );
                    })
                  : null}
              </ul>
            </div>
          </div>
          <div className="px-5 pb-5">
            <h2 className="py-4 text-slate-700 text-sm font-medium">
              {t("viewHistoryImages_current_image_title")}
            </h2>
            <ul>
              {checkedRoleImageHistory ? (
                <li>
                  <div className="w-[152px] h-[270px] rounded-lg overflow-hidden flex items-center justify-center bg-background">
                    <div className="w-full h-full relative">
                      <img
                        className="w-full h-full"
                        src={checkedRoleImageHistory.url}
                        alt=""
                      />
                      <div className="absolute bottom-2 right-2 space-x-2">
                        <Button
                          onClick={() => {
                            setPreviewImageVisible(true);
                          }}
                          className="bg-white/80 hover group"
                          icon={
                            <div className="relative w-6 h-6 flex items-center justify-center">
                              <img
                                src={previewIcon}
                                alt="preview"
                                className="absolute inset-0 m-auto transition-opacity duration-200 group-hover:opacity-0"
                              />
                              <img
                                src={previewIconHover}
                                alt="preview hover"
                                className="absolute inset-0 m-auto opacity-0 transition-opacity duration-200 group-hover:opacity-100"
                              />
                            </div>
                          }
                        />
                      </div>
                    </div>
                    {
                      createPortal(
                        <ImagePreview
                          imageList={[{
                            id: checkedRoleImageHistory.id,
                            src: checkedRoleImageHistory.url,
                            alt: checkedRoleImageHistory.figureName,
                          }]}
                          current={0}
                          previewImageVisible={previewImageVisible}
                          setPreviewImageVisible={setPreviewImageVisible}
                        />,
                        document.body
                      )
                    }
                  </div>
                  <p className="text-gray-900 text-base font-semibold mt-1">
                    {checkedRoleImageHistory.figureName}
                  </p>
                </li>
              ) : (
                <li>
                  <div className="w-[152px] h-[270px] rounded-lg overflow-hidden flex items-center justify-center bg-background">
                    <DefaultRoleItemImg />
                  </div>
                  <p className="text-gray-900 text-base font-semibold mt-1"></p>
                </li>
              )}
            </ul>
          </div>

        </div>
      </div>
    </div>
  );
};

export default ViewHistoryImagesContent;
