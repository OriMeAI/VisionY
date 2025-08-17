/**
 * 角色页面
 */

import { Skeleton } from "antd";
import React from "react";
import style from "./style.module.css";

interface IProps {}

const RoleItemSkeleton: React.FC<IProps> = ({}: IProps) => {
  return (
    <li className={`space-y-1 flex flex-col ${style.roleItemSkeletonWrapper}`}>
      <Skeleton.Button className={`rounded-xl ${style.skeletonImage}`} active />
      <Skeleton.Button className={style.skeletonFigureName} active />
    </li>
  );
};

export default RoleItemSkeleton;
