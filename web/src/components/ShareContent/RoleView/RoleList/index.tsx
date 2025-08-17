/**
 * 角色页面
 */

import React from "react";
import RoleItem from "../RoleItem";
import { RoleItemObj } from "./../../../../libs/interfaces";
import { useTranslation } from "react-i18next";

interface IProps {
  roleList: RoleItemObj[]; // 角色列表
  loading?: boolean; // 是否加载中
}

const RoleList: React.FC<IProps> = ({ roleList, loading }: IProps) => {
  const { t } = useTranslation();

  return (
    <div style={{ height: '788px', overflowY: 'auto' }}>
      {Array.isArray(roleList) && roleList.length === 0 && !loading ? (
        <>
          <ul className="grid grid-cols-2 gap-6"></ul>
          <div className="text-gray-500 text-xl">{t("roleList_noRoles")}</div>
        </>
      ) : null}
      <ul className="grid grid-cols-2 gap-6">
        {Array.isArray(roleList) && roleList.length > 0
          ? roleList.map((roleItem: RoleItemObj, roleIndex: number) => {
              return (
                <RoleItem
                  key={`roleItem-${roleItem.roleId}-${roleIndex}`}
                  roleItem={roleItem}
                  roleIndex={roleIndex}
                />
              );
            })
          : null}
      </ul>
    </div>
  );
};

export default RoleList;
