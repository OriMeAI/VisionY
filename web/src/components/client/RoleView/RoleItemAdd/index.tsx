/**
 * 新增角色按钮及弹窗
 */

import { Button, App } from "antd";
import plusIcon from "./../../../../../assets/images/icons/plus.svg";
import projectApi from "./../../../../api/projectApi";
import { RecentRoleItemObj, RoleItemObj } from "./../../../../libs/interfaces";

import { debounce } from "lodash";
import React, { useCallback, useContext, useState } from "react";
import { createPortal } from "react-dom";
import { useTranslation } from "react-i18next";
import ModalBase from "../../Common/ModalBase";
import {
  IRoleViewContexts,
  RoleViewContexts,
} from "../../../../contexts/role-view-contexts";
import RoleItemAddContent from "../RoleItemAddContent";

interface IProps {}

const RoleItemAdd: React.FC<IProps> = ({}: IProps) => {
  const { t } = useTranslation();
  const { message: messageApi } = App.useApp();
  const roleViewContexts = useContext<IRoleViewContexts>(RoleViewContexts);
  const [isModalOpen, setIsModalOpen] = useState<boolean>(false);
  // 最近使用的角色列表
  const [recentRoleList, setRecentRoleList] = React.useState<RecentRoleItemObj[]>([]);
  const [recentRoleTotalCount, setRecentRoleTotalCount] = React.useState<number>(0);
  const pageNum = React.useRef<number>(0);
  // 当前选中的角色
  const [checkedRecentRole, setCheckedRecentRole] = React.useState<RecentRoleItemObj>();
  const [currFigureName, setCurrFigureName] = React.useState<string>("");
  // 获取最近使用的角色列表
  const getRecentRoleList = async (figureName:string) => {
    const data = await projectApi.getRecentRoleList({
      pageSize: 20,
      pageNum: pageNum.current,
      figureName: figureName,
    });
    if (pageNum.current === 0) {
      setRecentRoleList(data.result.data.records);
    } else {
      setRecentRoleList([...recentRoleList, ...data.result.data.records]);
    }
    setRecentRoleTotalCount(data.result.data.total);
    if ( Array.isArray(data.result.data.records) && data.result.data.records.length > 0 && pageNum.current === 0) {
      setCheckedRecentRole(data.result.data.records[0]);
    }
  };
  const onMoreClick = async () => {
    pageNum.current++;
    await getRecentRoleList(currFigureName);
  };

  const debouncedGetRecentRoleList = useCallback(
    debounce((searchText: string) => getRecentRoleList(searchText), 1000),
    []
  );

  const onSearchChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    pageNum.current = 0;
    const searchText = e.target.value;
    setCurrFigureName(searchText);
    debouncedGetRecentRoleList(searchText);
  };
  const showModal = async () => {
    setIsModalOpen(true);
    // 重置页码 modified by soongxl
    pageNum.current = 0;
    // 清空当前搜索条件
    setCurrFigureName("");
    await getRecentRoleList("");
  };

  const addRoleItem = async () => {

    //检测是否有空角色
    //检测是否有空角色
    const emptyRoleIndex = roleViewContexts.roleList.findIndex(role => !role.url || role.url === "");
    
    if (emptyRoleIndex !== -1) {
      messageApi.warning(t("please_generate_empty_role_first"));
      return;
    }

    const res = await projectApi.addRoleItem({
      projectId: roleViewContexts.projectId,
    });
    if (res.success && res.result?.code === 0) {
      if (res.result?.data) {
        updateRoleList(res.result.data);
      }
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };
  const copyRoleItem = async () => {
    const res = await projectApi.copyRoleItem({
      projectId: roleViewContexts.projectId,
      roleId: checkedRecentRole?.id
    });
    if (res.success && res.result?.code === 0) {
      if (res.result?.data) {
        updateRoleList(res.result.data);
      }
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };
  const updateRoleList = (data: RoleItemObj) => {
    roleViewContexts.setRoleList([data, ...roleViewContexts.roleList, ]);
    roleViewContexts.setCheckedRoleItemIndex(0);
  };

  const handleModalCancel = async () => {
    setIsModalOpen(false);
    setCheckedRecentRole(recentRoleList[0]);
  };

  const onNewDefaultRole = async () => {
    await addRoleItem();
    await handleModalCancel();
  };

  const handleModalOk = async () => {
    if (checkedRecentRole) {
      await copyRoleItem();
    }
    await handleModalCancel();
  };
  return (
    <>
      <Button
        // onClick={onNewDefaultRole}
        onClick={showModal}
        size="large"
        className="group"
        icon={
          <img
            src={plusIcon}
            alt={t("add_role_alt")}
            className="transition-all duration-200 group-hover:[filter:invert(46%)_sepia(97%)_saturate(1396%)_hue-rotate(225deg)_brightness(89%)_contrast(93%)]"
          />
        }
      >
        <span>{t("add_role")}</span>
      </Button>

      {createPortal(
        <ModalBase
          open={isModalOpen}
          onOk={handleModalOk}
          onCancel={handleModalCancel}
          okText={t("role_item_add_copy_directly")}
          cancelText={t("role_item_add_create_new")}
          width={1024}
          height={885}
          footer={
            <>
              <Button size="large" onClick={onNewDefaultRole}>
                <span>{t("create_without_selection")}</span>
              </Button>
              <Button type="primary" size="large" onClick={handleModalOk}>
                <span>{t("confirm_selection")}</span>
              </Button>
            </>
          }
        >
          <RoleItemAddContent
            recentRoleList={recentRoleList}
            checkedRecentRole={checkedRecentRole}
            setCheckedRecentRole={setCheckedRecentRole}
            recentRoleTotalCount={recentRoleTotalCount}
            onMoreClick={onMoreClick}
            onSearchChange={onSearchChange}
          />
        </ModalBase>,
        document.body
      )}
    </>
  );
};

export default RoleItemAdd;
