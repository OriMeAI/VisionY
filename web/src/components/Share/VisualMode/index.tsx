/**
 * 视觉模式页面
 */

import { StoryboardShot } from "./../../../types/storyboard";
import VisualModeContainer from "./VisualModeContainer";
import React from "react";

interface IProps {
  tableData: StoryboardShot[];
}

const VisualMode: React.FC<IProps> = ({tableData}: IProps) => {
  return (
    <>
      {/* <Suspense
        fallback={
          <div className="flex items-center justify-center h-full">
            <Spin />
          </div>
        }
      >
        <VisualModeContainer tableData={tableData} />
      </Suspense> */}
      <VisualModeContainer tableData={tableData} />
    </>
  );
};

export default VisualMode;
