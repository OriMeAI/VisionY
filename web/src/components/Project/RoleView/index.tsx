/**
 * 角色页面
 */

import { Spin } from "antd";
import React, { lazy, Suspense } from "react";
import { useParams } from "react-router-dom";
import DetailContainer from "../DetailContainer";
import style from "./style.module.css";
import RoleViewContent from "../../client/RoleView/RoleViewContent";

interface IProps {}

const RoleView: React.FC<IProps> = ({}: IProps) => {
  const { projectId } = useParams<{ projectId: string }>();

  return (
    <div className={style.roleViewWrapper}>
      <DetailContainer projectId={projectId}>
        <RoleViewContent />
      </DetailContainer>
    </div>
  );
};

export default RoleView;
