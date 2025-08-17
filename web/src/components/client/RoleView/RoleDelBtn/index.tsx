/**
 * 角色页面
 */

import projectApi from "./../../../../api/projectApi";
import { Button, Modal, App } from "antd";
import React, { useContext, useState } from "react";
import {
    IRoleViewContexts,
    RoleViewContexts,
} from "../../../../contexts/role-view-contexts";
import roleViewStore from "../roleViewStore";
import { useTranslation } from "react-i18next";

interface IProps {}

const RoleDelBtn: React.FC<IProps> = ({}: IProps) => {
  const { t } = useTranslation();
  const roleViewContexts: IRoleViewContexts =
    useContext<IRoleViewContexts>(RoleViewContexts);
  const [open, setOpen] = useState<boolean>(false);
  const { message: messageApi } = App.useApp();

  const deleteRole = async () => {
    const res = await projectApi.deleteRole({
      projectId: roleViewContexts.projectId,
      roleId:roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex].roleId,
    });
    if (res.success && res.result?.code === 0) {
      messageApi.success(res.result.msg);
      await roleViewStore.getRoleList(roleViewContexts, () => {});
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };
  const handleOk = () => {
    handleCancel();
    deleteRole();
  };

  const handleCancel = () => {
    setOpen(false);
  };
  return (
    <Button
      size="large"
      className="px-8 my-6"
      style={{ color: roleViewContexts.roleList.length === 0 ? "#bbbbbb" : "#ff4d4f" }}
      disabled={roleViewContexts.roleList.length === 0}
      onClick={() => {
        Modal.confirm({
          open,
          title: t("roleView_delete_delete_title"),
          content: t("roleView_delete_delete_confirm"),
          okText: t("common_confirm"),
          cancelText: t("common_cancel"),
          centered: true,
          okButtonProps: {
            className: "custom-ok-button",
            style: { backgroundColor: "#7E2FFF", borderColor: "#7E2FFF" }
          },
          cancelButtonProps: {
            className: "custom-cancel-button",
            style: { borderColor: "#7E2FFF", color: "#7E2FFF" }
          },
          onOk() {
            handleOk();
          },
          onCancel() {
            handleCancel();
          },
        });
      }}
    >
      <span>{t("roleView_delete_delete_role")}</span>
    </Button>
  );
};

export default RoleDelBtn;
