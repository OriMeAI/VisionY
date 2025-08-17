/**
 * 剧本页面
 */

import React, { useContext } from "react";
import {
  DetailContexts,
  IDetailContexts,
} from "./../../Common/DetailContainer/contexts/detail-contexts";
import ProjectInfo from "../ProjectInfo";

interface IProps {}

const ProjectInfoContainer: React.FC<IProps> = ({}: IProps) => {
  const detailContexts: IDetailContexts =
    useContext<IDetailContexts>(DetailContexts);
  return (
    // <Suspense fallback={<div className="flex items-center justify-center h-full"><Spin /></div>}>
    //   <ProjectInfo content={detailContexts.projectItemObj?.content} />
    // </Suspense>
    <ProjectInfo content={detailContexts.projectItemObj?.content} />
  );
};

export default ProjectInfoContainer;
