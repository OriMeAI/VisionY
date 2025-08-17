/**
 * 角色页面
 */

import { Checkbox } from "antd";
import React, { useContext } from "react";
import { RoleItemObj } from "./../../../../libs/interfaces";
import {
  IShareRoleViewContexts,
  ShareRoleViewContexts,
} from "./../contexts/share-role-view-contexts";

interface IProps {
  roleItem: RoleItemObj; // 角色列表项
  roleIndex: number; // 角色列表项索引
}

const RoleItem: React.FC<IProps> = ({ roleItem, roleIndex }: IProps) => {
  const roleViewContexts: IShareRoleViewContexts =
    useContext<IShareRoleViewContexts>(ShareRoleViewContexts);
  const onRoleItemClick = () => {
    roleViewContexts.setCheckedRoleItemIndex(roleIndex);
  };
  console.log("roleViewContexts", roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex],  roleItem.roleId);
  return (
    <li onClick={onRoleItemClick}>
      <div className="w-[152px] h-[270px] relative flex flex-col items-center cursor-pointer rounded-lg bg-background overflow-hidden justify-center">
        {roleItem.url ? (
          <div className="w-full h-full overflow-hidden">
            <img
              src={roleItem.url}
              className={`w-full h-full object-contain transition duration-300 ease-in-out ${
            roleViewContexts.checkedRoleItemIndex === roleIndex
              ? "scale-110"
              : "scale-100"
          }`}
              alt=""
            />
          </div>
        ) : null}
        <div
          className={`absolute inset-0 w-full h-full border-2 rounded-lg z-10 transition duration-300 ease-in-out opacity-100 ${
            roleViewContexts.checkedRoleItemIndex === roleIndex
              ? "border-primary"
              : "border-transparent"
          }`}
        >
          {roleViewContexts.checkedRoleItemIndex === roleIndex ? (
            <Checkbox
              checked={roleViewContexts.checkedRoleItemIndex === roleIndex}
              className={`absolute top-0.5 right-1 z-10`}
            />
          ) : null}
        </div>
      </div>
      <p className="mt-1">{roleItem.figureName}</p>
    </li>
  );
};

export default RoleItem;
