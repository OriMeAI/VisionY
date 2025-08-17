/**
 * 查看历史形象按钮及弹窗
 */

import { Button, App } from "antd";
import React, { useContext, useState } from "react";
import { createPortal } from "react-dom";
import { useTranslation } from "react-i18next";
import ModalBase from "../../Common/ModalBase";
import {
  IRoleViewContexts,
  RoleViewContexts,
} from "../../../../contexts/role-view-contexts";
import ViewHistoryImagesContent from "../ViewHistoryImagesContent";
import projectApi from "./../../../../api/projectApi";
import { RoleImageHistoryItem } from "./../../../../libs/interfaces";

interface IProps {}

const ViewHistoryImages: React.FC<IProps> = ({}: IProps) => {
  const { t } = useTranslation();

  const roleViewContexts: IRoleViewContexts =useContext<IRoleViewContexts>(RoleViewContexts);
  const [isModalOpen, setIsModalOpen] = React.useState<boolean>(false);
  const [roleImageHistoryList, setRoleImageHistoryList] = useState<RoleImageHistoryItem[]>([]);
  const [checkedRoleImageHistory, setCheckedImageHistory] =useState<RoleImageHistoryItem>();
  const [selectedRoleImage, setSelectedImage] = useState<RoleImageHistoryItem>(); // 新增状态变量，用于存储选中的项

  const { message: messageApi } = App.useApp();

  const getRoleImageHistory = async () => {
    const res = await projectApi.getRoleImageHistory({
      projectId: roleViewContexts.projectId,
      roleId:roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex]?.roleId,
    });
    if (res.success && res.result?.code === 0) {
      if (res.result?.data) {
        setRoleImageHistoryList(res.result.data.figures);
        //fix bug 应该用 selected 字段
        // 查找 selected 为 true 的项作为默认选中项
        const selectedImage = res.result.data.figures.find((item: RoleImageHistoryItem) => item.selected === true);
        // 如果找到了 selected 为 true 的项，则设置为选中项，否则默认选择第一项
        setCheckedImageHistory(selectedImage || res.result.data.figures[0]);
        setSelectedImage(selectedImage || res.result.data.figures[0]);
      }
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };
  const showModal = async () => {
    await getRoleImageHistory();
    setIsModalOpen(true);
  };
  const handleModalCancel = async () => {
    setIsModalOpen(false);
  };

  const handleModalOk = async () => {
    handleModalCancel();
    if(selectedRoleImage.id === checkedRoleImageHistory?.id){
      return;
    }
    const res = await projectApi.updateDefaultHistory({
      projectId: roleViewContexts.projectId,
      roleId:roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex].roleId,
      targetId: checkedRoleImageHistory?.id
    });
    if (res.success && res.result?.code === 0) {
      if (res.result?.data) {
        //更新用户列表的信息
        let newRoleList = roleViewContexts.roleList;
        newRoleList[roleViewContexts.checkedRoleItemIndex] = res.result?.data;
        roleViewContexts.setRoleList([...newRoleList]);
        //todo 需要多语言支持
        messageApi.success(t("viewHistory_modal_success"));
      }
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);       
      }
    }  
  };
  return (
    <>
      <Button
        size="large"
        className="px-8 my-6"
        onClick={showModal}
        disabled={
          roleViewContexts.roleList.length === 0 ||
          !roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex]?.url
        }
      >
        <span>{t("viewHistory_button_text")}</span>
      </Button>

      {createPortal(
        <ModalBase
          open={isModalOpen}
          onOk={handleModalOk}
          onCancel={handleModalCancel}
          okText={t("viewHistory_modal_ok")}
          cancelText={t("viewHistory_modal_cancel")}
          width={848}
          height={674}
        >
          <ViewHistoryImagesContent
            roleImageHistoryList={roleImageHistoryList}
            checkedRoleImageHistory={checkedRoleImageHistory}
            setCheckedImageHistory={setCheckedImageHistory}
          />
        </ModalBase>,
        document.body
      )}
    </>
  );
};

export default ViewHistoryImages;
