import React, { useEffect, useRef, useState } from "react";
import { useTranslation } from "react-i18next";
import { StoryboardShot } from "./../../../../../types/storyboard";
import { Button, Popconfirm, App } from "antd";

interface ShotInfoProps {
  shot: StoryboardShot;
  currentSceneShots?: StoryboardShot[];
  currentShotIndex?: number;
  onSelectShot?: (shotIndex: number) => void;
}

// 可排序的镜头项组件
const SortableShotItem = ({
  shot,
  index,
  isCurrentShot,
  onSelectShot,
  selectedShotRef,
  t,
}: {
  shot: StoryboardShot;
  index: number;
  isCurrentShot: boolean;
  onSelectShot?: (index: number) => void;
  selectedShotRef: React.RefObject<HTMLDivElement>;
  t: any;
  disabled?: boolean;
}) => {
  const shotResource = shot.shot_resource;
  const shotNumber = `${index + 1}`;

  return (
    <div
      className={`mb-2 rounded overflow-hidden bg-gray-100 ${
        isCurrentShot
          ? "shadow-md border-2 border-primary scale-105"
          : "border border-gray-200 hover:border-primary-light"
      }`}
    >
      {/* 镜头缩略图 - 移到底部 */}
      <div
        id={`shot-item-${index}`}
        className="cursor-pointer transition-all duration-200 w-32 h-18 overflow-hidden relative bg-black"
        onClick={() => onSelectShot && onSelectShot(index)}
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
  currentSceneShots = [],
  currentShotIndex,
  onSelectShot,
}) => {
  const { t } = useTranslation();
  const { message: messageApi } = App.useApp();
  // 创建对选中镜头项的引用
  const selectedShotRef = useRef<HTMLDivElement>(null);

  // 添加本地状态来管理排序
  const [localShots, setLocalShots] =
    useState<StoryboardShot[]>(currentSceneShots);
  // 当外部传入的shots变化时，更新本地状态
  useEffect(() => {
    setLocalShots(currentSceneShots);
  }, [currentSceneShots]);

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
                    selectedShotRef={selectedShotRef}
                    t={t}
                  />
                );
              })}
            </div>
          </div>
        </div>
      )}

      {/* 镜头详情已移至App.tsx中的右侧区域 */}
    </div>
  );
};

export default ShotInfo;
