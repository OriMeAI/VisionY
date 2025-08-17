/**
 * 视觉模式
 */
import { Avatar, Spin, Tag, App } from "antd";
import React, { useEffect, useRef, useState } from "react";
import { useTranslation } from "react-i18next";
import CellMainFigure from "./../../../../components/client/Common/CellMainFigure";
import {
  Dialogue,
  SceneDescription,
  ShotResource,
  StoryboardShot,
} from "./../../../../types/storyboard";
import DialogueBox from "./components/DialogueBox";
import PlaybackControls from "./components/PlaybackControls";
import ShotInfo from "./components/ShotInfo";
import {
  getNextShot,
  getPrevShot,
  getRoleImageUrl,
} from "./utils/storyboardUtils";

import { PlaybackSpeed } from "./components/PlaybackControls";
import StoryboardEditBtns from "./../../../../components/client/Common/StoryboardEditBtns";

// 镜头之间的过渡时间（秒）
const TRANSITION_DURATION = 0.3;

//播放单条对话的时间
const DIALOGUE_PLAYBACK_DURATION = 1.0;

// 定义当前镜头状态接口
interface CurrentShotState {
  index: number;
  data: StoryboardShot | null;
}

interface IProps {
  tableData: StoryboardShot[];
}

const VisualModeContainer: React.FC<IProps> = ({ tableData }: IProps) => {
  const { t } = useTranslation(); // 添加 useTranslation hook
  const { message: messageApi } = App.useApp();
  const [storyboardData, setStoryboardData] = useState<StoryboardShot[]>([]);

  // 使用复合状态替换原来的两个状态
  const [currentShot, setCurrentShot] = useState<CurrentShotState>({
    index: 0,
    data: null
  });
  
  const [isPlaying, setIsPlaying] = useState<boolean>(false);
  const [playbackSpeed, setPlaybackSpeed] = useState<PlaybackSpeed>(1);
  const [isDialogueVisible, setIsDialogueVisible] = useState<boolean>(true);
  const [isTransitioning, setIsTransitioning] = useState<boolean>(false);

  const [backgroundDesc, setBackgroundDesc] = React.useState<SceneDescription>(
    currentShot.data?.scene_description
  );

  const [currentDialogues, setCurrentDialogues] = React.useState<Dialogue[]>([]);
  const [dialogueBoxContent, setDialogueBoxContent] = React.useState<Dialogue[]>([]);

  // 编辑图片
  const [isRegenerating, setIsRegenerating] = useState<boolean>(false);
  const [loadingText, setLoadingText] = useState<string>(
    t("generating_high_definition_image")
  );

  const setBoardLoadingText = (boardId:string,loadingText: string) => {
    // setLoadingText(loadingText);
  }

  const setBoardIsRegenerating = (boardId:string,isRegenerating: boolean) => {
    // setIsRegenerating(isRegenerating);
  }
  const setBoardShotResource = (boardId:string,resourceObj: ShotResource) => {
    // setResourceObj(resourceObj);
  }

  const playbackTimerRef = useRef<number | null>(null);

  // 加载故事板数据
  useEffect(() => {
    setStoryboardData(tableData);
    if (tableData.length > 0) {
      setCurrentShot({
        index: 0,
        data: tableData[0]
      });
    }else{
      setCurrentShot({
        index: 0,
        data: null
      });
    }
  }, [tableData]);

  // 获取当前镜头的播放时长（秒）
  const getShotDuration = (shot: StoryboardShot | null): number => {
    let dialogueDuration = 0; // 默认3秒

    // 根据对话长度估算时长
    if (shot && shot.dialogues && shot.dialogues.length > 0) {
      // 每个对话至少3秒，每10个字符增加1秒
      shot.dialogues.forEach((dialogue) => {
        const contentLength = dialogue.content.length;
        if(contentLength > 0 ){
          dialogueDuration += DIALOGUE_PLAYBACK_DURATION;
        }
      });
    }

    if(dialogueDuration > 0){
      return dialogueDuration;
    }else{
      return 3;// 默认3秒
    }
  };

  // 自动播放功能
  useEffect(() => {
    if (isPlaying) {
      // 清除之前的定时器
      if (playbackTimerRef.current !== null) {
        window.clearTimeout(playbackTimerRef.current);
      }

      // 计算播放时长（基于镜头时长和播放速度）
      const baseDuration = getShotDuration(currentShot.data);
      // 添加过渡时间到调整后的时长
      const adjustedDuration = (baseDuration / playbackSpeed + TRANSITION_DURATION / playbackSpeed) * 1000;

      // 设置新的定时器
      playbackTimerRef.current = window.setTimeout(() => {
        const nextShotIndex = getNextShot(storyboardData, currentShot.index);
        if (nextShotIndex !== null) {
          // 显示黑色幕布过渡
          setIsTransitioning(true);
          // 延迟切换镜头，等待黑色幕布显示
          setTimeout(() => {
            setCurrentShot({
              index: nextShotIndex,
              data: storyboardData[nextShotIndex]
            });
            // 延迟隐藏黑色幕布，等待新镜头加载
            setTimeout(() => {
              setIsTransitioning(false);
            }, 300);
          }, 300);
        } else {
          // 如果已经是最后一个镜头，停止播放
          setIsPlaying(false);
          messageApi.success(t("stop_playback"))
        }
      }, adjustedDuration);
    }

    // 组件卸载时清除定时器
    return () => {
      if (playbackTimerRef.current !== null) {
        window.clearTimeout(playbackTimerRef.current);
      }
    };
  }, [isPlaying, currentShot, playbackSpeed, storyboardData]);

  // 处理播放/暂停
  const handlePlayPause = () => {
    const nextShotIndex = getNextShot(storyboardData, currentShot.index);

    if(nextShotIndex === null){
      setIsPlaying(false);
      messageApi.info(t("already_last_shot"))
      return;
    }

    setIsPlaying((prev) => !prev);
  };

  const handleSetCurrentShot = (shotIndex: number) => {
    if(shotIndex === currentShot.index){
      return;
    }
    //停止自动播放
    setIsPlaying(false);

    if (shotIndex !== null) {
      // 显示黑色幕布过渡
      setIsTransitioning(true);
      // 延迟切换镜头，等待黑色幕布显示
      setTimeout(() => {
        setCurrentShot({
          index: shotIndex,
          data: storyboardData[shotIndex]
        });
        // 延迟隐藏黑色幕布，等待新镜头加载
        setTimeout(() => {
          setIsTransitioning(false);
        }, 300);
      }, 300);
    };
  };

  // 判断是否为第一个镜头
  const isPreviousDisabled = () => {
    return currentShot.index <= 0;
  };

  // 处理上一个镜头
  const handlePrevious = () => {
    //停止自动播放
    setIsPlaying(false);
    const prevShotIndex = getPrevShot(storyboardData, currentShot.index);
    if (prevShotIndex !== null) {
      // 显示黑色幕布过渡
      setIsTransitioning(true);
      // 延迟切换镜头，等待黑色幕布显示
      setTimeout(() => {
        setCurrentShot({
          index: prevShotIndex,
          data: storyboardData[prevShotIndex]
        });
        // 延迟隐藏黑色幕布，等待新镜头加载
        setTimeout(() => {
          setIsTransitioning(false);
        }, 300);
      }, 300);
    };
  };

  // 判断是否为最后一个镜头
  const isNextDisabled = () => {
    const lastShotIndex = storyboardData.length - 1;
    return currentShot.index === lastShotIndex;
  };

  // 处理下一个镜头
  const handleNext = () => {
    //停止自动播放
    setIsPlaying(false);

    const nextShotIndex = getNextShot(storyboardData, currentShot.index);
    if (nextShotIndex !== null) {
      // 显示黑色幕布过渡
      setIsTransitioning(true);
      // 延迟切换镜头，等待黑色幕布显示
      setTimeout(() => {
        setCurrentShot({
          index: nextShotIndex,
          data: storyboardData[nextShotIndex]
        });
        // 延迟隐藏黑色幕布，等待新镜头加载
        setTimeout(() => {
          setIsTransitioning(false);
        }, 300);
      }, 300);
    }
  };

  // 处理速度变化
  const handleSpeedChange = (speed: PlaybackSpeed) => {
    setPlaybackSpeed(speed);
  };

  // 处理对话框显示切换
  const handleToggleDialogue = () => {
    setIsDialogueVisible((prev) => !prev);
  };

  useEffect(() => {
    // 过滤出 content 不为空的对话
    const validDialogues = currentDialogues.filter(dialogue => dialogue.content !== '');
    setDialogueBoxContent(validDialogues);
  }, [currentDialogues]);

  useEffect(() => {
    setBackgroundDesc(currentShot.data?.scene_description);
    setCurrentDialogues(currentShot.data ? currentShot.data.dialogues || [] : []);
  }, [currentShot.data]);
  
  // 将 handleBoardItemChange 定义为单独的函数
  const handleBoardItemChange = (updatedBoardItem: StoryboardShot) => {
    return;
  };

  const setShotResource = (newResource: ShotResource) => {
    return;
  };

  if (!currentShot.data) return null;

  return (
    <div
      id="app-container"
      className="min-w-[622px] overflow-auto"
    >
      <main
        id="app-main"
        className="max-w-[1535px] container mx-auto my-6 p-6 overflow-x-hidden bg-white rounded-lg"
      >
        <div
          id="app-content"
          className="flex flex-col lg:flex-row lg:justify-between lg:space-x-6"
        >

          {/* 中间播放区域 */}
          <div id="playback-area" className="lg:w-[80%] w-full overflow-x-auto">
            {currentShot.data ? (
              <div id="shot-container">
                {/* 镜头画面区域 */}
                <div
                  id="shot-display"
                  className="bg-gray-100 rounded shadow-md overflow-hidden mb-4 relative flex flex-col"
                >
                  {/* 镜头图片 */}
                  <div
                    id="shot-screen"
                    className="w-full flex items-center justify-center relative p-4 min-h-[400px] bg-black"
                  >
                    <div
                      id="shot-image-container"
                      className="w-full min-h-[400px] overflow-hidden"
                    >
                      {/* 黑色幕布过渡效果 */}
                      <div
                        id="black-curtain"
                        className={`absolute inset-0 bg-black z-20 transition-opacity duration-300 ${
                          isTransitioning
                            ? "opacity-100"
                            : "opacity-0 pointer-events-none"
                        }`}
                      />
                      {currentShot.data && (
                        <Spin tip={loadingText} spinning={isRegenerating}>
                          <img
                            id="shot-image"
                            src={currentShot.data.shot_resource.shot_resource_url}
                            alt={`${t("shot")} ${currentShot.index + 1}`}
                            className="w-full min-h-[400px] object-contain shadow-md transform  aspect-[16/9]"
                          />
                          {/* 对话框 - 移动到图片容器内部并设置为绝对定位 */}
                          <div
                            id="dialogue-box-area"
                            className="absolute bottom-0 left-0 right-0 z-10"
                          >
                            <DialogueBox
                              dialogues={dialogueBoxContent}
                              isVisible={isDialogueVisible}
                              currentShot={currentShot.data}
                              autoPlay={isPlaying}
                              autoPlayInterval={ DIALOGUE_PLAYBACK_DURATION / playbackSpeed * 1000}
                            />
                          </div>

                          {currentShot.data.shot_resource.is_HD ? (
                            <Tag
                              className="absolute bottom-2 right-0 border-none"
                              style={{
                                background: "rgba(0, 0, 0, 0.4)",
                                backdropFilter: "blur(2px)",
                                color: "rgb(255, 255, 255)",
                              }}
                            >
                              HD
                            </Tag>
                          ) : null}
                          <StoryboardEditBtns
                            boardItem={currentShot.data}
                            isEdit={false}
                            isRegenerating={isRegenerating}
                            setBoardLoadingText={setBoardLoadingText}
                            setBoardIsRegenerating={setBoardIsRegenerating}
                            setBoardShotResource={setBoardShotResource}
                          />
                        </Spin>
                      )}
                    </div>
                  </div>
                  {/* 播放控制 */}
                  <div id="playback-controls-area">
                    <PlaybackControls
                      boardItem={currentShot.data}
                      isPlaying={isPlaying}
                      playbackSpeed={playbackSpeed}
                      onPlayPause={handlePlayPause}
                      onPrevious={handlePrevious}
                      onNext={handleNext}
                      onSpeedChange={handleSpeedChange}
                      isPreviousDisabled={isPreviousDisabled()}
                      isNextDisabled={isNextDisabled()}
                      isDialogueVisible={isDialogueVisible}
                      onToggleDialogue={handleToggleDialogue}
                    />
                  </div>
                </div>

                {/* 镜头信息 */}
                <div id="shot-info-section">
                  <ShotInfo
                    shot={currentShot.data}
                    currentSceneShots={storyboardData}
                    currentShotIndex={currentShot.index}
                    onSelectShot={(shotIndex) => handleSetCurrentShot(shotIndex)}
                  />
                </div>
              </div>
            ) : null}
          </div>

          {/* 右侧镜头详情区域 */}
          {currentShot.data && (
            <div
              id="shot-details-sidebar"
              className="lg:w-1/5 w-full lg:sticky mt-4 lg:mt-0 lg:self-start"
            >
              <div
                id="shot-details-container"
                className="bg-gray-100 rounded p-4"
              >
                <div
                  id="shot-details-header"
                  className="flex justify-between items-center"
                >
                  <h3
                    id="shot-details-title"
                    className="text-lg font-medium text-gray-800"
                  >
                    {t("scene_description")}
                  </h3>
                </div>
                <div
                  id="shot-details-content"
                  className="mt-2 space-y-2 overflow-x-auto"
                >
                  <div className="cursor-default">
                    <div id="shot-background-info">
                      <span className="text-gray-600">
                        {t("scene_background")}：
                      </span>
                      <br/>
                      <span>{backgroundDesc?.background || t("none")}</span>
                    </div>

                    {backgroundDesc?.characters &&
                      backgroundDesc.characters.length > 0 && (
                        <div
                          id="character-actions-container"
                          className="mt-3"
                        >
                          <h4
                            id="character-actions-title"
                            className="text-gray-600 mb-1"
                          >
                            {t("character_action_and_emotion")}:
                          </h4>
                          <div
                            id="character-actions-list"
                            className="space-y-1"
                          >
                            {backgroundDesc.characters.map(
                              (character, index) => (
                                <div
                                  id={`character-action-item-${index}`}
                                  key={index}
                                  className="flex flex-col items-start mb-3"
                                >
                                  <div
                                    id={`character-action-content-${index}`}
                                    className="w-full"
                                  >
                                    <div className="flex items-center mb-1">
                                      <div
                                        className="flex-shrink-0 mr-2"
                                        id={`character-action-avatar-${index}`}
                                      >
                                        {getRoleImageUrl(character.role_id, currentShot.data) ? (
                                          <Avatar
                                            className="w-6 h-6 avatar-top-image"
                                            src={getRoleImageUrl(character.role_id, currentShot.data)}
                                          />
                                        ) : (
                                          <Avatar
                                            className="w-6 h-6 avatar-top-image"
                                          />
                                        )}
                                      </div>
                                      <span
                                        id={`character-action-name-${index}`}
                                        className="font-medium"
                                      >
                                        {character.role_name}:
                                      </span>
                                    </div>
                                    <div>
                                      <span
                                        id={`character-action-emotion-${index}`}
                                        className="break-words whitespace-normal text-gray-700"
                                      >
                                        {character.action_and_emotion ||
                                          t("none")}
                                      </span>
                                    </div>
                                  </div>
                                </div>
                              )
                            )}
                          </div>
                        </div>
                      )}
                  </div>
                  {/* 添加主要人物区域 */}
                  <div id="main-characters-container" className="mt-3 mb-4">
                    <h4
                      id="main-characters-title"
                      className="text-lg font-medium text-gray-800 mb-3"
                    >
                      {t("main_characters")}
                    </h4>

                    <div className="flex items-center flex-start">
                      <CellMainFigure
                        boardItem={currentShot.data}
                        handleBoardItemChange={handleBoardItemChange}
                        isEdit={false}
                      />
                    </div>
                  </div>
                  {/* 镜头信息 */}
                  <div id="shot_info" className="mt-3 mb-4">
                    <h4
                      id="main-characters-title"
                      className="text-lg font-medium text-gray-800 mb-3"
                    >
                      {t("shot_info")}
                    </h4>
                  </div>
                  <div
                    id="shot-technical-info"
                    className="grid grid-cols-1 gap-2"
                  >
                    <div id="shot-size-info">
                      <div className="flex justify-between items-center">
                        <span className="text-gray-600">
                          {t("storyboard_shot_size")}:
                        </span>
                        <span>{currentShot.data.shot_size?.value}</span>
                      </div>
                    </div>
                    <div id="camera-angle-info">
                      <div className="flex justify-between items-center">
                        <span className="text-gray-600">
                          {t("camera_angle")}：
                        </span>
                        <span>
                          {currentShot.data?.camera_angle.value}
                        </span>
                      </div>
                    </div>
                    <div id="shot-type-info">
                      <div className="flex justify-between items-center">
                        <span className="text-gray-600">
                          {t("shot_type")}：
                        </span>
                        <span>{currentShot.data?.shot_type.value}</span>
                      </div>
                    </div>
                    <div id="shot-duration-info">
                      <div className="flex justify-between items-center">
                        <span className="text-gray-600">
                          {t("storyboard_duration")}：
                        </span>
                        <span>{currentShot.data?.shot_time.value}{t("seconds")}</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      </main>
    </div>
  );
};

export default VisualModeContainer;