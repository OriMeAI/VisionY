/**
 * 角色页面
 */

import { RoleItemObj } from "./../../../../libs/interfaces";
import { Checkbox } from "antd";
import React, { useContext } from "react";
import {
  IRoleViewContexts,
  RoleViewContexts,
} from "../../../../contexts/role-view-contexts";
import DefaultRoleItemImg from "../DefaultRoleItemImg";

interface IProps {
  roleItem: RoleItemObj; // 角色列表项
  roleIndex: number; // 角色列表项索引
}

const RoleItem: React.FC<IProps> = ({
  roleItem,
  roleIndex,
}: IProps) => {
  const roleViewContexts: IRoleViewContexts =
    useContext<IRoleViewContexts>(RoleViewContexts);
  const onRoleItemClick = () => {
    roleViewContexts.setCheckedRoleItemIndex(roleIndex);
  };
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
        ) : (
          <DefaultRoleItemImg />
        )}
        <div
          className={`absolute inset-0 w-full h-full border-2 rounded-lg z-10 transition duration-300 ease-in-out ${
            roleViewContexts.checkedRoleItemIndex === roleIndex
              ? "opacity-100 border-primary"
              : "opacity-0 border-transparent"
          }`}
        >
          {roleViewContexts.checkedRoleItemIndex === roleIndex ? (
            <Checkbox
              checked={
                roleViewContexts.checkedRoleItemIndex === roleIndex
              }
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
