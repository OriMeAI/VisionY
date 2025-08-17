/**
 * 故事板页面
 */
import {
  closestCenter,
  DndContext,
  DragEndEvent,
  DragOverlay,
  PointerSensor,
  useDndMonitor,
  useSensor,
  useSensors,
} from "@dnd-kit/core";
import { restrictToParentElement } from "@dnd-kit/modifiers";
import { arrayMove, SortableContext } from "@dnd-kit/sortable";
import { App } from "antd";
import { isString } from "lodash";
import React, { lazy, Suspense, useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import dashboardApi from "../../../../api/dashboardApi";
import projectApi from "../../../../api/projectApi";
import {
  StoryboardCopyPayload,
  StoryboardDeletePayload,
  StoryboardSortPayload,
} from "../../../../libs/interfaces";
import { StoryboardShot } from "../../../../types/storyboard";
import { BoardItemPreview } from "../BoardItem/BoardItemPreview";
import BoardItem from "./../BoardItem";
import { trackEvent, trackPageView, setUserProperties } from '../../../../libs/amplitude';

interface IProps {}

const DnDDragOverlay = (props: { storyboardTableData: StoryboardShot[] }) => {
  const { storyboardTableData } = props;

  const [activeId, setActiveId] = useState<string | null>(null);
  const [height, setHeight] = useState(0);
  const [width, setWidth] = useState(0);
  useDndMonitor({
    onDragStart(event) {
      setActiveId(event.active.id.toString());
      const div = document.getElementById(`boardItem-${event.active.id}`);
      const rect = div?.getBoundingClientRect();
      if (rect) {
        setHeight(rect.height);
        setWidth(rect.width);
      }
    },
  });

  return (
    <DragOverlay dropAnimation={null}>
      <BoardItemPreview
        boardItem={
          isString(activeId)
            ? storyboardTableData.find((i) => i.shot_id === activeId)
            : null
        }
        itemIndex={
          isString(activeId)
            ? storyboardTableData.findIndex((i) => i.shot_id === activeId)
            : null
        }
        bodyList={storyboardTableData}
        height={height}
        width={width}
      ></BoardItemPreview>
    </DragOverlay>
  );
};

const BoardList: React.FC<IProps> = ({}: IProps) => {
  const { projectId } = useParams<{ projectId: string }>();
  const [storyboardTableData, setStoryboardTableData] = React.useState<
    StoryboardShot[]
  >([]);
  const { message: messageApi } = App.useApp();
  // 通过项目id获取故事板列表信息(与分镜表一致)
  useEffect(() => {
    (async () => {
      const data = await projectApi.getStoryboardListById(projectId);
      setStoryboardTableData(data.result.data);
    })();
  }, []);
  const sensors = useSensors(useSensor(PointerSensor, {}));

  const onDragEnd = async ({ active, over }: DragEndEvent) => {
    console.log("active", active, typeof active.id, typeof over?.id);
    console.log("over", over);
    if (active.id !== over?.id) {
      // 直接在这里实现排序逻辑，不再调用单独的函数
      const storyboardSortPayload: StoryboardSortPayload = {
        projectId: projectId,
        currentId: active.id.toString(),
        targetId: over?.id.toString(),
      };
      const res = await dashboardApi.storyboardSort(storyboardSortPayload);
      if (res.success && res.result?.code === 0) {
        //服务器处理完毕数据，本地再做修改
        setStoryboardTableData((prevState) => {
          const activeIndex = prevState.findIndex(
            (record) => record.shot_id === active?.id
          );
          const overIndex = prevState.findIndex(
            (record) => record.shot_id === over?.id
          );
          return arrayMove(prevState, activeIndex, overIndex);
        });
      } else {
        messageApi.error(res.result?.msg);
      }
    }
  };

  const onAdd = async (obj: StoryboardShot) => {
    const storyboardCopyPayload: StoryboardCopyPayload = {
      projectId: projectId,
      storyboardId: obj.shot_id,
    };
    const res = await dashboardApi.storyboardCopy(storyboardCopyPayload);
    if (res.success && res.result?.code === 0) {
      setStoryboardTableData((prevState) => {
        const index = prevState.findIndex(
          (item) => item.shot_id === obj.shot_id
        );
        if (index === -1) return prevState;

        // 修改这里：将新数据插入到 index 之前
        return [
          ...prevState.slice(0, index), // 获取 index 之前的所有元素
          res.result.data, // 插入新元素
          ...prevState.slice(index), // 获取从 index 开始的所有元素（包括原 index 位置的元素）
        ];
      });
      messageApi.success(res.result?.msg);
    } else {
      messageApi.error(res.result?.msg);
    }
  };

  const onDelete = async (id: string) => {
    //需要等待服务器处理完毕数据，本地再做修改
    const storyboardDeletePayload: StoryboardDeletePayload = {
      projectId: projectId,
      storyboardId: id,
    };
    const res = await dashboardApi.storyboardDelete(storyboardDeletePayload);
    if (res.success && res.result?.code === 0) {
      setStoryboardTableData((prevState) => {
        return prevState?.filter((item) => item.shot_id !== id);
      });
      messageApi.success(res.result?.msg);
    } else {
      messageApi.error(res.result?.msg);
    }
  };

  return (
    <div>
      {/* <div style={{ height: "calc(100vh - 72px)", overflowY: 'auto' }}> */}
      <div className="bg-gray-100">
        <div className="py-6 relative">
          <div
            className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 
                  2xl:grid-cols-5 3xl:grid-cols-6 4xl:grid-cols-8 5xl:grid-cols-10 6xl:grid-cols-12 gap-6 px-6"
          >
            <DndContext
              collisionDetection={closestCenter}
              modifiers={[restrictToParentElement]}
              sensors={sensors}
              onDragEnd={onDragEnd}
            >
              <SortableContext
                items={storyboardTableData.map((i) => i.shot_id)}
              >
                <>
                  {storyboardTableData.map(
                    (item: StoryboardShot, index: number) => (
                      <Suspense
                        key={`board_item_suspense_${item.shot_id}_${index}`}
                      >
                        <BoardItem
                          key={`board_item_${item.shot_id}_${index}`}
                          boardItem={item}
                          itemIndex={index}
                          bodyList={storyboardTableData}
                          projectId={projectId}
                          onAdd={onAdd}
                          onDelete={onDelete}
                        />
                      </Suspense>
                    )
                  )}
                </>
              </SortableContext>
              <DnDDragOverlay
                storyboardTableData={storyboardTableData}
              ></DnDDragOverlay>
            </DndContext>
          </div>
        </div>
      </div>
      {/* </div> */}
    </div>
  );
};

export default BoardList;
