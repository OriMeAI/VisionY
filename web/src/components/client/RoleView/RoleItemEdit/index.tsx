/**
 * 角色编辑组件
 */

import { Avatar, Button, Input, Skeleton, App } from "antd";
import redDeleteIcon from "./../../../../../assets/images/icons/red_delete_icon.svg";
import noRoleDefaultImg from "./../../../../../assets/images/pages/roleView/no-role.svg";
import whiteGenImgIcon from "./../../../../../assets/images/pages/roleView/white_gen_img_icon.svg";
import projectApi from "./../../../../api/projectApi";

import React, { useContext, useEffect, useState } from "react";
import { createPortal } from "react-dom";
import { useTranslation } from "react-i18next";
import { useNavigate } from "react-router-dom";
import {
  DetailContexts,
  IDetailContexts,
} from "../../Common/DetailContainer/contexts/detail-contexts";
import ImagePreview from "../../Common/ImagePreview";
import {
  IRoleViewContexts,
  RoleViewContexts,
} from "../../../../contexts/role-view-contexts";
import DefaultRoleItemImg from "../DefaultRoleItemImg";
import FaceRefer from "../FaceRefer";
import RegenerateImgBtn from "../RegenerateImgBtn";
import ViewHistoryImages from "../ViewHistoryImages";
import RoleDelBtn from "../RoleDelBtn";
import previewIcon from "./../../../../../assets/images/pages/boardView/preview_icon.svg";
import previewIconHover from "./../../../../../assets/images/pages/boardView/preview_icon_hover.svg";
import style from "./style.module.css";

interface IProps {
  loading?: boolean; // 是否加载中
}

const RoleItemEdit: React.FC<IProps> = ({ loading }: IProps) => {
  const navigate = useNavigate();
  const { t } = useTranslation();
  const { message: messageApi } = App.useApp();
  const roleViewContexts: IRoleViewContexts =
    useContext<IRoleViewContexts>(RoleViewContexts);
  const [figureName, setFigureName] = useState<string>(
    roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex]?.figureName
  );
  //add by soongxl 做边界检查
  const [defaultFigureName, setDefaultFigureName] = useState<string>(
    roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex]?.figureName
  );

  const [figureDesc, setFigureDesc] = useState<string>(
    roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex]?.figureDesc
  );
 
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

  //优化代码逻辑
  useEffect(() => {
    if (roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex]) {
      setFigureName(
        roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex]?.figureName
      );
      setDefaultFigureName(
        roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex]?.figureName
      );
      setFigureDesc(
        roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex]?.figureDesc
      );
    }
  }, [roleViewContexts.roleList, roleViewContexts.checkedRoleItemIndex]);

  const detailContexts: IDetailContexts =
    useContext<IDetailContexts>(DetailContexts);
  // 预览图片
  const [previewImageVisible, setPreviewImageVisible] = useState<boolean>(false);

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
      messageApi.success(t("roleEdit_messages_deleteSuccess"));
      roleViewContexts.setUploadExampleFigureImg("");
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };
  const scriptToShot = async () => {
    navigate(`/project/${roleViewContexts.projectId}/tableview`);
  };

  const onFigureNameChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFigureName(e.target.value);
  };
  const onFigureDescChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setFigureDesc(e.target.value);
    roleViewContexts.roleList[
      roleViewContexts.checkedRoleItemIndex
    ].figureDesc = e.target.value;
  };
  const onFigureNameBlur = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const currentName = e.target.value
    //如果输输入没变化，直接返回 add by soongxl
    if (currentName === defaultFigureName) {
      return;
    }
    if (currentName === "") {
      setFigureName(defaultFigureName);
      return;
    }
    
    roleViewContexts.roleList[
      roleViewContexts.checkedRoleItemIndex
    ].figureName = currentName;
    roleViewContexts.setRoleList([...roleViewContexts.roleList]);

    const res = await projectApi.renameRole({
      projectId: roleViewContexts.projectId,
      roleId:roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex].roleId,
      figureName: currentName,
    });
    if (res.success && res.result?.code === 0) {
      //todo 需要多语言支持
      messageApi.success(res.result.msg);
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };
  return (
    <div
      className={`${style.roleItemEditWrapper} relative rounded-lg flex-1 pt-7 bg-white flex flex-col h-full`}
    >
      {Array.isArray(roleViewContexts.roleList) &&
      roleViewContexts.roleList.length === 0 &&
      !loading ? (
        <div className="px-6 overflow-auto mt-3">
          <div className="h-[460px] w-[260px] rounded-lg bg-gradient-to-b from-white to-black/5 flex justify-center items-center mx-auto">
            <div className="w-[130px] h-[130px] flex flex-col items-center">
              <img
                className="w-[100px] h-[100px]"
                src={noRoleDefaultImg}
                alt={t("roleEdit_noRole")}
              />
              <p className="text-gray-300">{t("roleEdit_noRole")}</p>
            </div>
          </div>
        </div>
      ) : null}
      {roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex] ? (
        <div className="flex justify-between px-6 pb-4">
          <div className="mx-auto w-44 first-step">
            <Input
              maxLength={20}
              className="text-center"
              onBlur={onFigureNameBlur}
              onChange={onFigureNameChange}
              value={figureName}
            />
          </div>
        </div>
      ) : null}
      {loading && !roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex] ? (
        <div className="flex justify-center p-6 pt-0">
          <Skeleton.Button className={style.skeletonTitle} active />
        </div>
      ) : null}

      {roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex] ? (
        <div className="px-6 overflow-auto mt-3">
          <div className="flex space-y-8 flex-col h-full">
            <div className="w-[260px] h-[460px] rounded-lg overflow-hidden relative flex items-center bg-background justify-center mx-auto">
              {roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex].url ? (
                <img
                  className="w-full h-full object-cover"
                  src={
                    roleViewContexts.roleList[
                      roleViewContexts.checkedRoleItemIndex
                    ].url
                  }
                  alt={t("roleEdit_figureName_placeholder")}
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
            {roleViewContexts.uploadExampleFigureImg ? (
              <div className="flex justify-between w-[260px] mx-auto">
                <div className="flex space-x-3">
                  <Avatar
                    src={
                      <img
                        src={roleViewContexts.uploadExampleFigureImg}
                        alt="avatar"
                      />
                    }
                  />
                  <div className="text-sm flex items-center">
                    <h2 className="text-gray-900 my-0">
                      {t("roleEdit_faceReference_title")}
                    </h2>
                  </div>
                </div>
                <Button
                  type="text"
                  onClick={deleteRoleExample}
                  icon={
                    <img
                      src={redDeleteIcon}
                      alt={t("roleEdit_actions_delete")}
                    />
                  }
                />
              </div>
            ) : null}
            <div className="flex-1 flex flex-col mt-auto mx-[80px]">
              <Input.TextArea
                value={figureDesc}
                onChange={onFigureDescChange}
                placeholder={t("roleEdit_figureDesc_placeholder")}
                maxLength={500}
                style={{ resize: "none", height: 80, minHeight: 80 }}
              />
            </div>
          </div>
        </div>
      ) : null}
      {loading && !roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex] ? (
        <div className="mt-5 px-6">
          <div className="flex flex-col space-y-8 w-full justify-center items-center">
            <Skeleton.Button
              className={`${style.skeletonImage} rounded-xl`}
              active
            />
          </div>
        </div>
      ) : null}
      <div className="absolute bottom-0 left-0 right-0">
        <div className="w-full px-6 flex items-center">
          {/* {roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex] ? (
            <FaceRefer />
          ) : null} */}
          <div className="flex-1 flex justify-center">
            <ViewHistoryImages />
          </div>
          <div className="flex-1 flex justify-center">
            <RegenerateImgBtn />
          </div>
          <div className="flex-1 flex justify-center">
            <RoleDelBtn />
          </div>
        </div>
        {/* {!(roleViewContexts.roleList.length === 0 || detailContexts.projectItemObj.hasShot) && ( */}
        {!detailContexts.projectItemObj.hasShot && (
          <div className="border-t space-x-3 flex flex-row items-center h-[76px] px-6 justify-center">
            <Button
              type="primary"
              size="large"
              ref={roleViewContexts.tourRef3}  // 绑定到按钮元素
              disabled={
                roleViewContexts.roleList.length === 0 ||
                detailContexts.projectItemObj.hasShot
              }
              onClick={scriptToShot}
            >
              <img 
                src={whiteGenImgIcon} 
                alt={t("roleEdit_actions_generate")} 
                className={`${
                  roleViewContexts.roleList.length === 0 ||
                  detailContexts.projectItemObj.hasShot
                    ? 'opacity-25 brightness-0'
                    : ''
                }`}
              />
              <span>{t("roleEdit_actions_generate")}</span>
            </Button>
          </div>
        )}
      </div>
    </div>
  );
};

export default RoleItemEdit;
