/**
 * 新增角色弹窗
 */

import { ArrowsAltOutlined } from "@ant-design/icons";
import { Button, Divider, Empty, Input } from "antd";
import React, { useState } from "react";
import { createPortal } from "react-dom";
import { useTranslation } from "react-i18next";
import ImagePreview from "../../Common/ImagePreview";
import NextImg from "../../Common/NextImg";
import searchIcon from "./../../../../../assets/images/pages/roleView/search_icon.svg";
import smileFaceIcon from "./../../../../../assets/images/pages/roleView/smile_face_icon.svg";
import drawHelper from "./../../../../libs/draw-helper";
import { RecentRoleItemObj } from "./../../../../libs/interfaces";
import previewIcon from "./../../../../../assets/images/pages/boardView/preview_icon.svg";
import previewIconHover from "./../../../../../assets/images/pages/boardView/preview_icon_hover.svg";
interface IProps {
  recentRoleList: RecentRoleItemObj[];
  checkedRecentRole: RecentRoleItemObj | undefined;
  setCheckedRecentRole: React.Dispatch< React.SetStateAction<RecentRoleItemObj | undefined> >;
  recentRoleTotalCount: number;
  onMoreClick?: () => void;
  onSearchChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const RoleItemAddContent: React.FC<IProps> = ({
  recentRoleList,
  checkedRecentRole,
  setCheckedRecentRole,
  recentRoleTotalCount,
  onMoreClick,
  onSearchChange,
}: IProps) => {
  const { t } = useTranslation();
  const [previewImageVisible, setPreviewImageVisible] = useState<boolean>(false);

  return (
    <>
      <div className="px-6 py-5 border-b">
        <div className="flex space-x-4">
          <div className="border h-12 w-12 rounded-lg flex items-center justify-center">
            <NextImg icon={smileFaceIcon} />
          </div>
          <div>
            <h2 className="text-gray-900 text-lg font-semibold">
              {t("roleView_add_role_title")}
            </h2>
            <p className="text-slate-600 text-sm">
              {t("roleView_add_role_subtitle")}
            </p>
          </div>
        </div>
      </div>
      <div className="flex w-full border-b">
      <div className="flex-1 px-6 py-4 h-[708px]">
          <div className="flex items-center justify-between">
            <div className="flex space-x-1 mb-1">
              <Button
                type="text"
                className="font-semibold hover:bg-primary/10 hover:text-primary transition-colors duration-300 ease-in-out bg-primary/10 text-primary"
              >
                <span>{t("roleView_add_role_recently_used")}</span>
              </Button>
            </div>
            <div className="flex">
              <Input
                size="small"
                placeholder={t("roleView_add_role_search_placeholder")}
                allowClear
                prefix={<img src={searchIcon} alt="" />}
                onChange={onSearchChange}
              />
            </div>
          </div>
          <div
            className={`w-full box-content`}
            style={{
              margin: "16px 0",  // 上下padding为16px，左右为0
              height: 624,
              overflowY: "auto",
            }}
          >
            {Array.isArray(recentRoleList) && recentRoleList.length > 0 ? (
              <>
                <ul className="pb- grid grid-cols-[repeat(auto-fill,minmax(120px,1fr))] gap-4">
                  {recentRoleList.map(
                    (
                      recentRoleItem: RecentRoleItemObj,
                      recentRoleIndex: number
                    ) => {
                      return (
                        <li
                          className="flex flex-col cursor-pointer"
                          key={`recentRoleItem-${recentRoleItem.id}-${recentRoleIndex}`}
                          onClick={() => {
                            setCheckedRecentRole(recentRoleItem);
                          }}
                        >
                          <div
                            className={`border rounded-lg w-full min-h-[258px] overflow-hidden border-${
                              recentRoleItem.id === checkedRecentRole?.id
                                ? "primary"
                                : "transparent"
                            }`}
                          >
                            <div
                              draggable="false"
                              className="ant-image css-aw5bp3"
                              style={{ width: "100%", height: "100%" }}
                            >
                              <img
                                draggable="false"
                                alt={recentRoleItem.figureName}
                                className="ant-image-img css-aw5bp3"
                                src={recentRoleItem.url}
                                width="100%"
                                height="100%"
                                style={{ height: "100%", objectFit: "cover" }}
                              />
                            </div>
                          </div>
                          <p className="font-semibold">
                            {recentRoleItem.figureName}
                          </p>
                        </li>
                      );
                    }
                  )}
                </ul>
                <div className="flex justify-center py-6">
                  {recentRoleList.length < recentRoleTotalCount ? (
                    <Button
                      type="primary"
                      variant="solid"
                      size="large"
                      ghost
                      onClick={onMoreClick && onMoreClick}
                    >
                      <span>{t("common_load_more")}</span>
                    </Button>
                  ) : null}
                </div>
              </>
            ) : (
              <ul className="pb-5 grid grid-cols-[repeat(auto-fill,minmax(120px,1fr))] gap-1 pr-3">
                <Empty
                  image={Empty.PRESENTED_IMAGE_SIMPLE}
                  className="col-span-full h-full"
                  description={t("common_no_data")}
                />
              </ul>
            )}
          </div>
        </div>

        <Divider
          type="vertical"
          className="h-[708px] mx-0"
          style={{ borderColor: "rgb(229, 231, 235)" }}
        />

        <div
          className={`w-[180px] px-6 py-5 box-content`}
          style={{ height: 668, overflowY: "auto" }}
        >
          <h2 className="text-slate-700 text-sm font-semibold">
            {t("roleView_add_role_selected_role")}
          </h2>
          <div className="flex flex-col mt-4">
            <div className="w-full h-80 rounded-lg overflow-hidden relative">
              <div
                draggable="false"
                className="ant-image css-aw5bp3"
                style={{ width: "100%", height: "100%" }}
              >
                <img
                  draggable="false"
                  alt={checkedRecentRole?.figureName}
                  src={checkedRecentRole?.url}
                  width="100%"
                  height="100%"
                  style={{ height: "100%", objectFit: "contain" }}
                />

                {createPortal(
                  <ImagePreview
                    imageList={[
                      {
                        id: checkedRecentRole?.id,
                        src: checkedRecentRole?.url,
                        alt: checkedRecentRole?.figureName,
                      },
                    ]}
                    current={0}
                    previewImageVisible={previewImageVisible}
                    setPreviewImageVisible={setPreviewImageVisible}
                  />,
                  document.body
                )}
              </div>
              <div className="absolute bottom-2 right-2">
                <Button
                  className="bg-white/80 group"
                  onClick={() => setPreviewImageVisible(true)}
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
            <p className="font-semibold">{checkedRecentRole?.figureName}</p>
            <div
              className="mt-4 text-slate-500 max-h-[250px] overflow-y-auto"
            >
              <div style={{ margin: 0 }}>
                <div>
                  <div style={{ right: 0, bottom: 0 }}>
                    <div
                      role="region"
                      aria-label="scrollable content"
                      style={{ height: "auto", overflow: "hidden" }}
                    >
                      <div style={{ padding: 0 }}>
                        {checkedRecentRole?.cnDesc}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default RoleItemAddContent;
