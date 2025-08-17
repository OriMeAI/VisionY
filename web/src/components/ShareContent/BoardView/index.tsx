/**
 * 故事板页面
 */

import React from "react";

import { StoryboardShot } from "./../../../types/storyboard";
import BoardItem from "./BoardItem";

interface IProps {
  tableData: StoryboardShot[];
  isNew?: boolean;
}

const BoardView: React.FC<IProps> = ({ tableData, isNew }: IProps) => {
  return (
    <div className={isNew ? "mt-0" : "mt-[72px]"}>
      <div style={{ height: isNew ? 'calc(100vh - 144px)' : 'calc(100vh - 72px)',overflowY: 'auto' }}>
        <div className="bg-gray-100">
          <div className="py-6 relative">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 
                  2xl:grid-cols-5 3xl:grid-cols-6 4xl:grid-cols-8 5xl:grid-cols-10 6xl:grid-cols-12 gap-6 px-6">
              {Array.isArray(tableData) && tableData.length > 0
                ? tableData.map((item: StoryboardShot, index: number) => (
                    <BoardItem
                      key={`board_item_${item.shot_id}_${index}`}
                      boardItem={item}
                      itemIndex={index}
                    />
                  ))
                : null}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default BoardView;
