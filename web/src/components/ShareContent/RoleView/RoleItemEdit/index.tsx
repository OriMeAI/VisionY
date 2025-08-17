/**
 * 角色编辑组件
 */
import { createPortal } from "react-dom";
import { Button, App } from "antd";
import projectApi from "../../../../api/projectApi";
import ImagePreview from "../../../client/Common/ImagePreview";
import DefaultRoleItemImg from "../../../client/RoleView/DefaultRoleItemImg";
import previewIcon from "./../../../../../assets/images/pages/boardView/preview_icon.svg";
import previewIconHover from "./../../../../../assets/images/pages/boardView/preview_icon_hover.svg";

import React, { useContext, useEffect, useState } from "react";
import {
  IShareRoleViewContexts,
  ShareRoleViewContexts,
} from "../contexts/share-role-view-contexts";
import style from "./style.module.css";
import { useTranslation } from "react-i18next"; // 添加 i18n 引入

interface IProps {}

const RoleItemEdit: React.FC<IProps> = ({}: IProps) => {
  const { t } = useTranslation(); // 添加 t 函数
  const roleViewContexts: IShareRoleViewContexts = useContext<IShareRoleViewContexts>(ShareRoleViewContexts);

  // 预览图片
  const [previewImageVisible, setPreviewImageVisible] = useState<boolean>(false);

  const [figureName, setFigureName] = useState<string>(
    roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex]?.figureName
  );
  const [figureDesc, setFigureDesc] = useState<string>(
    roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex]?.figureDesc
  );
  const { message: messageApi } = App.useApp();

  const [imageList, setImageList] = useState<
    { id: string; src: string; alt: string; originIndex: number }[]
  >([]);

  useEffect(() => {
      const imageList = roleViewContexts.roleList
      .map((role, idx) => ({
        id: role.roleId,
        src: role.url,
        alt: role.figureName,
        originIndex: idx,
      }))
      .filter(item => !!item.src);
      setImageList(imageList);
  }, [roleViewContexts.roleList]);

  useEffect(() => {
    setFigureName(
      roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex]
        ?.figureName
    );
  }, [roleViewContexts.roleList, roleViewContexts.checkedRoleItemIndex]);

  useEffect(() => {
    setFigureDesc(
      roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex]
        ?.figureDesc
    );
  }, [roleViewContexts.roleList, roleViewContexts.checkedRoleItemIndex]);

  const onRoleItemPrev = () => {
    if (roleViewContexts.checkedRoleItemIndex === 0) {
      return;
    }
    roleViewContexts.setCheckedRoleItemIndex(
      roleViewContexts.checkedRoleItemIndex - 1
    );
  };
  const onRoleItemNext = () => {
    if (
      roleViewContexts.checkedRoleItemIndex ===
      roleViewContexts.roleList.length - 1
    ) {
      return;
    }
    roleViewContexts.setCheckedRoleItemIndex(
      roleViewContexts.checkedRoleItemIndex + 1
    );
  };
  const deleteRoleExample = async () => {
    const res = await projectApi.deleteRoleExample({
      projectId: roleViewContexts.projectId,
      roleId:
        roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex].roleId,
    });
    if (res.success && res.result?.code === 0) {
      messageApi.success(t("roleItemEdit_delete_success")); // 使用 t 函数替换中文
      roleViewContexts.setUploadExampleFigureImg("");
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };
  return (
    <div
      className={`${style.roleItemEditWrapper}  rounded-lg flex-1 pt-7 pb-7 bg-white flex flex-col`}
    >
      {roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex] ? (
        <div className="flex justify-between px-6 pb-4">
          <div className="mx-auto w-44 first-step">
            <div className="text-center cursor-default">{figureName}</div>
          </div>
        </div>
      ) : null}

      {roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex] ? (
        <div className="flex-1 px-6 mt-3 pb-6">
          <div className="h-full flex flex-col items-center justify-between">
            <div className="w-[260px] h-[460px] rounded-lg relative flex items-center bg-background justify-center">
              {roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex].url ? (
                <img
                  className="w-full h-full object-cover rounded-lg"
                  src={
                    roleViewContexts.roleList[
                      roleViewContexts.checkedRoleItemIndex
                    ].url
                  }
                  alt={t("roleItemEdit_character_image")} // 使用 t 函数替换中文
                />
              ) : (
                <DefaultRoleItemImg />
              )}

              {!(roleViewContexts.roleList.length === 0 || 
                !roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex]?.url) && createPortal(
                <ImagePreview
                  imageList={[imageList.filter(item => item.originIndex === roleViewContexts.checkedRoleItemIndex)[0]]}
                  current={0}
                  previewImageVisible={previewImageVisible}
                  setPreviewImageVisible={setPreviewImageVisible}
                />,
                document.body
              )}
              {!(roleViewContexts.roleList.length === 0 || 
                !roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex]?.url) &&
              (<div className="absolute bottom-2 right-2 space-x-2">
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
              </div>)}
            </div>
            <div className="flex-1 flex flex-col justify-center h-full px-12">
              <div style={{ resize: "none", height: 76, minHeight: 76, cursor: "default" }}>
                {figureDesc}
              </div>
            </div>
          </div>
        </div>
      ) : null}
    </div>
  );
};

export default RoleItemEdit;
