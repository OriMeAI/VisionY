import {
  closestCenter,
  DndContext,
  DragEndEvent,
  DragOverlay,
  DragStartEvent,
  KeyboardSensor,
  PointerSensor,
  useSensor,
  useSensors,
} from "@dnd-kit/core";
import {
  restrictToHorizontalAxis,
  restrictToParentElement,
} from "@dnd-kit/modifiers";
import {
  arrayMove,
  horizontalListSortingStrategy,
  SortableContext,
  sortableKeyboardCoordinates,
  useSortable,
} from "@dnd-kit/sortable";
import { CSS } from "@dnd-kit/utilities";
import { App, Button, Popconfirm } from "antd";
import React, { useEffect, useRef, useState } from "react";
import { useTranslation } from "react-i18next";
import deleteIcon from "./../../../../../../assets/images/icons/delete_icon.svg";
import copyIcon from "./../../../../../../assets/images/pages/boardView/copy_icon.svg";
import sortIcon2 from "./../../../../../../assets/images/pages/boardView/sort_icon_2.svg";
import dashboardApi from "./../../../../../api/dashboardApi";
import { StoryboardSortPayload } from "./../../../../../libs/interfaces";
import { StoryboardShot } from "./../../../../../types/storyboard";

interface ShotInfoProps {
  projectId: string;
  currentShots: StoryboardShot[];
  currentShotIndex: number;
  onSelectShot: (shotIndex: number) => void;
  onCopyShot: (shot: StoryboardShot) => void;
  onDeleteShot: (shotId: string) => void;
  onReorderShots: (shots: StoryboardShot[]) => void; // 添加拖拽排序回调
}

// 可排序的镜头项组件
const SortableShotItem = ({
  shot,
  index,
  isCurrentShot,
  onSelectShot,
  onCopyShot,
  onDeleteShot,
  selectedShotRef,
  t,
  disabled = false,
  isDraggingId = null,
}: {
  shot: StoryboardShot;
  index: number;
  isCurrentShot: boolean;
  onSelectShot?: (index: number) => void;
  onCopyShot?: (shot: StoryboardShot) => void;
  onDeleteShot?: (shotId: string) => void;
  selectedShotRef: React.RefObject<HTMLDivElement>;
  t: any;
  disabled?: boolean;
  isDraggingId?: string | null;
}) => {
  const shotResource = shot.shot_resource;
  const shotNumber = `${index + 1}`;

  const {
    attributes,
    listeners,
    setNodeRef,
    transform,
    transition,
    isDragging,
  } = useSortable({
    id: shot.shot_id,
    disabled,
  });

  // 如果当前项正在被拖拽，则隐藏原位置的元素
  const isBeingDragged = isDraggingId === shot.shot_id;

  const style = {
    transform: CSS.Transform.toString(transform),
    transition,
    zIndex: isDragging ? 100 : 1,
    opacity: isBeingDragged ? 0 : isDragging ? 0.8 : 1, // 如果是被拖拽的元素，在原位置设为透明
    visibility: isBeingDragged ? ("hidden" as const) : ("visible" as const), // 使用 as const 来指定具体的类型
  };

  return (
    <div
      ref={setNodeRef}
      style={style}
      className={`mb-2 rounded overflow-hidden bg-white cursor-pointer ${
        isCurrentShot
          ? "shadow-md border-2 border-primary scale-105"
          : "border border-gray-200 hover:border-primary-light"
      }`}
      onClick={() => onSelectShot && onSelectShot(index)}
    >
      {/* 操作按钮区域 - 移到顶部 */}
      <div className="flex items-center justify-between px-2 py-1 bg-white">
        <div className="flex items-center">
          <div className="flex items-center">
            <img
              src={sortIcon2}
              alt={t("sort")}
              className="w-4 h-4 mr-1 cursor-move opacity-60 hover:opacity-100"
              {...attributes}
              {...listeners}
            />
            <span className="text-xs text-gray-600">{shotNumber}</span>
          </div>
        </div>
        <div className="flex items-center space-x-1">
          <Button
            type="text"
            size="small"
            className="flex items-center justify-center p-0 min-w-0 w-6 h-6"
            icon={
              <img
                src={copyIcon}
                alt={t("copy")}
                className="w-4 h-4 opacity-60 hover:opacity-100"
              />
            }
            onClick={(e) => {
              e.stopPropagation();
              onCopyShot && onCopyShot(shot);
            }}
          />
          <Popconfirm
            placement="rightTop"
            title={t("shot_info_delete_shot")}
            description={t("shot_info_delete_confirm")}
            trigger="click"
            okText={t("confirm")}
            cancelText={t("cancel")}
            onConfirm={(e) => {
              e.stopPropagation();
              onDeleteShot && onDeleteShot(shot.shot_id);
            }}
          >
            <Button
              type="text"
              size="small"
              className="flex items-center justify-center p-0 min-w-0 w-6 h-6"
              icon={
                <img
                  src={deleteIcon}
                  alt={t("delete")}
                  className="w-4 h-4 opacity-60 hover:opacity-100"
                />
              }
              onClick={(e) => e.stopPropagation()}
            />
          </Popconfirm>
        </div>
      </div>

      {/* 镜头缩略图 - 移到底部 */}
      <div
        id={`shot-item-${index}`}
        className="cursor-pointer transition-all duration-200 w-40 h-20 overflow-hidden relative bg-black"
        ref={isCurrentShot ? selectedShotRef : null}
      >
        <div id={`shot-item-content-${index}`} className="h-full w-full">
          {shotResource && (
            <img
              id={`shot-thumbnail-${index}`}
              src={shotResource.shot_resource_url}
              alt={t("shot_thumbnail_alt", { number: shotNumber })}
              className="w-full h-full object-contain aspect-[3/2]"
            />
          )}
          <div
            id={`shot-label-${index}`}
            className="absolute bottom-0 left-0 right-0 bg-black bg-opacity-75 p-1"
          >
            <div
              id={`shot-number-${index}`}
              className="text-xs font-medium truncate text-center text-white"
            >
              {t("shot_label", { number: shotNumber })}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

const ShotInfo: React.FC<ShotInfoProps> = ({
  projectId,
  currentShots = [],
  currentShotIndex,
  onSelectShot,
  onCopyShot,
  onDeleteShot,
  onReorderShots,
}) => {
  const { t } = useTranslation();
  const { message: messageApi } = App.useApp();
  // 创建对选中镜头项的引用
  const selectedShotRef = useRef<HTMLDivElement>(null);

  // 添加本地状态来管理排序
  const [localShots, setLocalShots] = useState<StoryboardShot[]>(currentShots);
  const [activeId, setActiveId] = useState<string | null>(null);

  // 当外部传入的shots变化时，更新本地状态
  useEffect(() => {
    setLocalShots(currentShots);
  }, [currentShots]);

  // 设置拖拽传感器
  const sensors = useSensors(
    useSensor(PointerSensor, {
      activationConstraint: {
        distance: 5, // 减小触发距离，使拖拽更灵敏
      },
    }),
    useSensor(KeyboardSensor, {
      coordinateGetter: sortableKeyboardCoordinates,
    })
  );

  // 处理拖拽开始
  const handleDragStart = (event: DragStartEvent) => {
    setActiveId(event.active.id as string);
  };

  // 处理拖拽结束事件
  const handleDragEnd = async (event: DragEndEvent) => {
    const { active, over } = event;
    setActiveId(null);

    if (over && active.id !== over.id) {
      // 直接在这里实现排序逻辑，不再调用单独的函数
      const storyboardSortPayload: StoryboardSortPayload = {
        projectId: projectId,
        currentId: active.id.toString(),
        targetId: over?.id.toString(),
      };
      const res = await dashboardApi.storyboardSort(storyboardSortPayload);
      if (res.success && res.result?.code === 0) {
        //服务器处理完毕数据，本地再做修改
        const oldIndex = localShots.findIndex(
          (shot) => shot.shot_id === active.id
        );
        const newIndex = localShots.findIndex(
          (shot) => shot.shot_id === over.id
        );

        if (oldIndex !== -1 && newIndex !== -1) {
          // 更新本地状态
          const newShots = arrayMove(localShots, oldIndex, newIndex);
          setLocalShots(newShots);

          // 调用父组件的回调
          if (onReorderShots) {
            onReorderShots(newShots);
          }
        }
      } else {
        messageApi.error(res.result?.msg);
      }
    }
  };

  // 监听currentShotIndex变化，滚动到选中的镜头
  useEffect(() => {
    if (currentShotIndex !== undefined && selectedShotRef.current) {
      const targetElement = selectedShotRef.current;
      // 根据你的 HTML 结构，滚动容器是 id="scene-shots-scroll" 的 div
      const scrollContainer = document.getElementById('scene-shots-scroll');

      if (targetElement && scrollContainer) {
        const targetRect = targetElement.getBoundingClientRect();
        const containerRect = scrollContainer.getBoundingClientRect();

        // 计算目标元素中心点在容器中应该处于的位置 (容器宽度的一半减去元素宽度的一半)
        const desiredTargetLeftInContainer = (containerRect.width / 2) - (targetRect.width / 2);
        
        // 计算当前目标元素左边缘相对于容器左边缘的实际距离
        const currentTargetLeftInContainer = targetRect.left - containerRect.left;
        
        // 计算需要滚动的差值
        const scrollAmount = currentTargetLeftInContainer - desiredTargetLeftInContainer;
        
        // 使用 scrollTo 方法进行平滑滚动，只改变 left 属性
        scrollContainer.scrollTo({
          left: scrollContainer.scrollLeft + scrollAmount,
          behavior: 'smooth'
          // 不指定 top，这样垂直滚动位置理论上不会被主动改变
        });
      }
    }
  }, [currentShotIndex]);

  // 查找当前活动的镜头
  const activeShot = activeId
    ? localShots.find((shot) => shot.shot_id === activeId)
    : null;
  const activeShotIndex = activeShot ? localShots.indexOf(activeShot) : -1;

  // 在 ShotInfo 组件的 return 部分
  return (
    <div id="shot-info-container" className="bg-gray-100 rounded p-4 mt-4">
      {localShots && localShots.length > 0 && (
        <div id="scene-shots-list-container">
          <h3
            id="scene-shots-title"
            className="text-lg font-medium text-gray-800 mb-3"
          >
            {t("shot_info_shot_list")}
          </h3>

          <div id="scene-shots-scroll" className="overflow-x-auto">
            <DndContext
              sensors={sensors}
              collisionDetection={closestCenter}
              onDragStart={handleDragStart}
              onDragEnd={handleDragEnd}
              modifiers={[restrictToHorizontalAxis, restrictToParentElement]}
            >
              <SortableContext
                items={localShots.map((shot) => shot.shot_id)}
                strategy={horizontalListSortingStrategy}
              >
                <div
                  id="scene-shots-wrapper"
                  className="flex pt-1 px-1 space-x-3 min-w-max"
                >
                  {localShots.map((sceneShot, index) => {
                    const isCurrentShot = index === currentShotIndex;

                    return (
                      <SortableShotItem
                        key={sceneShot.shot_id}
                        shot={sceneShot}
                        index={index}
                        isCurrentShot={isCurrentShot}
                        onSelectShot={onSelectShot}
                        onCopyShot={onCopyShot}
                        onDeleteShot={onDeleteShot}
                        selectedShotRef={selectedShotRef}
                        t={t}
                        isDraggingId={activeId} // 传递当前正在拖拽的ID
                      />
                    );
                  })}
                </div>
              </SortableContext>

              {/* 添加拖拽覆盖层，提升用户体验 */}
              <DragOverlay adjustScale={true}>
                {activeId && activeShot && (
                  <SortableShotItem
                    shot={activeShot}
                    index={activeShotIndex}
                    isCurrentShot={activeShotIndex === currentShotIndex}
                    selectedShotRef={selectedShotRef}
                    t={t}
                    disabled={true}
                  />
                )}
              </DragOverlay>
            </DndContext>
          </div>
        </div>
      )}

      {/* 镜头详情已移至App.tsx中的右侧区域 */}
    </div>
  );
};

export default ShotInfo;
