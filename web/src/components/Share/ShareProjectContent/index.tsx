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
  // 从URL路径中获取ID参数，例如从/share/10011/new中提取10011
  // const { id } = useParams<{ id: string }>();

  // // 修改提取pathId的方式，确保能从/share/10011/new格式中提取到10011
  // const pathSegments = window.location.pathname.split("/").filter(Boolean);
  // const pathId = pathSegments.length >= 2 ? pathSegments[1] : id;

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
      {currSegment === DetailTabType.Role && templateProjectItem ? (
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
      {currSegment === DetailTabType.Storyboard && templateProjectItem ? (
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
      {currSegment === DetailTabType.VisualView && templateProjectItem ? (
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
