/**
 * 分镜表页面
 */

import { Spin } from "antd";
import React, { lazy, Suspense } from "react";
import { useParams } from "react-router-dom";
import DetailContainer from "../DetailContainer";
import TableViewContent from "../../client/TableView/TableViewContent";

interface IProps {}

const TableView: React.FC<IProps> = ({}: IProps) => {
  const { projectId } = useParams<{ projectId: string }>();

  return (
    <DetailContainer projectId={projectId}>
      {/* <Suspense
        fallback={
          <div className="flex items-center justify-center h-full">
            <Spin />
          </div>
        }
      >
        <TableViewContent />
      </Suspense> */}
      <TableViewContent />
    </DetailContainer>
  );
};

export default TableView;
