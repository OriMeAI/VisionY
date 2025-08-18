/**
 * 预览页面（不可编辑）
 */
import React, { lazy, Suspense, useEffect } from "react";
import { useParams } from "react-router-dom";
import { Spin } from "antd";
import ProjectInfo from "../../client/ScriptView/ProjectInfo";
import shareApi from "../../../api/shareApi";
import { DetailTabType } from "../../../libs/enums";
import { ProjectItemObj, RoleItemObj } from "../../../libs/interfaces";
import { StoryboardShot } from "../../../types/storyboard";

// 懒加载子组件
const BoardView = lazy(() => import("../../ShareContent/BoardView"));
const RoleView = lazy(() => import("../../ShareContent/RoleView"));
const TableView = lazy(() => import("../../ShareContent/TableView"));
const VisualMode = lazy(() => import("../VisualMode"));

interface IProps {
  currSegment: DetailTabType;
  templateProjectItem: ProjectItemObj;
}

const ShareProjectContent: React.FC<IProps> = ({
  currSegment,
  templateProjectItem,
}: IProps) => {

  const [projectId, setProjectId] = React.useState<string>();
  const [templateShootTableData, setTemplateShootTableData] = React.useState<StoryboardShot[]>();
  const [roleList, setRoleList] = React.useState<RoleItemObj[]>([]);

useEffect(() => {
  if (!templateProjectItem?.id) return;
  
  const loadData = async () => {
    const projectId = templateProjectItem.id;
    setProjectId(projectId);
    
    const [roleData, shotData] = await Promise.all([
      shareApi.getTemplateRoleById(projectId),
      shareApi.getTemplateShootById(projectId)
    ]);
    
    setRoleList(roleData.result?.data);
    setTemplateShootTableData(shotData.result?.data);
  };
  
  loadData();
}, [templateProjectItem?.id]);

  return (
    <>
      {currSegment === DetailTabType.Script && templateProjectItem ? (
        <ProjectInfo content={templateProjectItem?.content} />
      ) : null}
      {currSegment === DetailTabType.Role && roleList ? (
        <Suspense
          fallback={
            <div className="flex items-center justify-center h-full">
              <Spin />
            </div>
          }
        >
          <RoleView
            id={projectId}
            roleList={roleList}
            setRoleList={setRoleList}
            isNew={true}
          />
        </Suspense>
      ) : null}
      {currSegment === DetailTabType.FilmTable && templateShootTableData ? (
        <Suspense
          fallback={
            <div className="flex items-center justify-center h-full">
              <Spin />
            </div>
          }
        >
          <TableView tableData={templateShootTableData} isNew={true} />
        </Suspense>
      ) : null}
      {currSegment === DetailTabType.Storyboard && templateShootTableData ? (
        <Suspense
          fallback={
            <div className="flex items-center justify-center h-full">
              <Spin />
            </div>
          }
        >
          <BoardView tableData={templateShootTableData} isNew={true} />
        </Suspense>
      ) : null}
      {currSegment === DetailTabType.VisualView && templateShootTableData ? (
        <Suspense
          fallback={
            <div className="flex items-center justify-center h-full">
              <Spin />
            </div>
          }
        >
          <VisualMode tableData={templateShootTableData} />
        </Suspense>
      ) : null}
    </>
  );
};

export default ShareProjectContent;
