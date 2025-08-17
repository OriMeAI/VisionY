/**
 * 剧本页面
 */

import { Spin } from "antd";
import React, { lazy, Suspense } from "react";
import { useParams } from "react-router-dom";
import DetailContainer from "../DetailContainer";

// 懒加载子组件
const ProjectInfoContainer = lazy(
  () => import("../../client/ScriptView/ProjectInfoContainer")
);

interface IProps {}

const ScriptView: React.FC<IProps> = ({}: IProps) => {
  const { projectId } = useParams<{ projectId: string }>();

  return (
    <DetailContainer projectId={projectId}>
      <Suspense
        fallback={
          <div className="flex items-center justify-center h-full">
            <Spin />
          </div>
        }
      >
        <ProjectInfoContainer />
      </Suspense>
    </DetailContainer>
  );
};

export default ScriptView;
