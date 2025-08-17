/**
 * 视觉模式页面
 */

import React from "react";
import { useParams } from "react-router-dom";
import DetailContainer from "../DetailContainer";
import VisualModeContainer from "./VisualModeContainer";

interface IProps {}

const VisualMode: React.FC<IProps> = ({}: IProps) => {
  const { projectId } = useParams<{ projectId: string }>();
  return (
    <>
      <DetailContainer projectId={projectId}>
        {/* <Suspense fallback={
          <div className="flex items-center justify-center h-full">
            <Spin />
          </div>}>
          <VisualModeContainer />
        </Suspense> */}
        <VisualModeContainer />
      </DetailContainer>
    </>
  );
};

export default VisualMode;
