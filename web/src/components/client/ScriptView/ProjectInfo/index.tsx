/**
 * 剧本页面
 */

import React, { useState } from "react";
import { DndContext } from "@dnd-kit/core";
import { SortableContext, arrayMove } from "@dnd-kit/sortable";
import SortableItem from "./SortableItem";

interface IProps {
  content: string; // 项目内容
}

const ProjectInfo: React.FC<IProps> = ({ content }: IProps) => {
  const [items, setItems] = useState(["item1", "item2", "item3"]);

  const handleDragEnd = (event: any) => {
    const { active, over } = event;
    if (active.id !== over.id) {
      setItems((items) => {
        const oldIndex = items.indexOf(active.id);
        const newIndex = items.indexOf(over.id);
        return arrayMove(items, oldIndex, newIndex); // 使用 arrayMove 更新数组顺序
      });
    }
  };
  return (
    // <div className="h-full" style={{ height: "calc(100vh - 144px)", overflowY: "auto" }}>
      <div>
        {/* <DndContext onDragEnd={handleDragEnd}>
        <SortableContext items={items}>
          {items.map((id) => (
            <SortableItem key={id} id={id} />
          ))}
        </SortableContext>
      </DndContext> */}
        <div className="bg-background">
          <div
            className="px-8 py-6"
          >
            <div>
              <div className="bg-background">
                <div className="px-8">
                  <div className="w-[700px] mx-auto whitespace-pre p-6 text-wrap bg-white rounded-lg">
                    {content}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    // </div>
  );
};

export default ProjectInfo;
