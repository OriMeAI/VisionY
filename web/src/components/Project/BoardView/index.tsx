/**
 * 故事板页面
 */
import React from "react";
import { useParams } from "react-router-dom";
import DetailContainer from "../DetailContainer";
import BoardList from "../../client/BoardView/BoardList";

interface IProps {}

const BoardView: React.FC<IProps> = ({}: IProps) => {
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
        <BoardList />
      </Suspense> */}
      <BoardList />
    </DetailContainer>
  );
};

export default BoardView;
