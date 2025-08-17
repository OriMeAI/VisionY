/**
 * 视觉模式
 */
import { Avatar, message, Spin, Tag, App } from "antd";
import React, { useEffect, useRef, useState,Suspense } from "react";
import { useTranslation } from "react-i18next";
import { useParams } from "react-router-dom";
import dashboardApi from "./../../../../api/dashboardApi";
import projectApi from "./../../../../api/projectApi";
import CellInputNumber from "./../../../../components/client/Common/CellInputNumber";
import CellMainFigure from "./../../../../components/client/Common/CellMainFigure";
import CellSelect from "./../../../../components/client/Common/CellSelect";
import StoryboardDialoguesEdit from "./../../../../components/client/Common/StoryboardDialoguesEdit";
import StoryboardEditBtns from "./../../../../components/client/Common/StoryboardEditBtns";
import StoryboardPictureDescEdit from "./../../../../components/client/Common/StoryboardPictureDescEdit";
import {
  StoryboardCopyPayload,
  StoryboardDeletePayload,
} from "./../../../../libs/interfaces";
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

// 镜头之间的过渡时间（秒）
const TRANSITION_DURATION = 0.3;
//播放单条对话的时间
const DIALOGUE_PLAYBACK_DURATION = 1.0;

// 定义当前镜头状态接口
interface CurrentShotState {
  index: number;
  data: StoryboardShot | null;
}

//定义每个board的状态
interface BoardState {
  boardId: string;
  loadingText: string;
  isRegenerating: boolean;
}

interface IProps {}

const VisualModeContainer: React.FC<IProps> = ({}: IProps) => {
  const { t } = useTranslation(); // 添加 useTranslation hook
  const { projectId } = useParams<{ projectId: string }>();
  const [storyboardData, setStoryboardData] = useState<StoryboardShot[]>([]);

  // 使用复合状态替换原来的单一索引状态
  const [currentShot, setCurrentShot] = useState<CurrentShotState>({
    index: 0,
    data: null,
  });

  const [boardsState, setBoardsState] = React.useState<BoardState[]>([]);

  const [isPlaying, setIsPlaying] = useState<boolean>(false);
  const [playbackSpeed, setPlaybackSpeed] = useState<PlaybackSpeed>(1);
  const [isDialogueVisible, setIsDialogueVisible] = useState<boolean>(true);
  const [isTransitioning, setIsTransitioning] = useState<boolean>(false);

  const [isBackgroundModalOpen, setIsBackgroundModalOpen] =
    React.useState<boolean>(false);
  const [backgroundDesc, setBackgroundDesc] =
    React.useState<SceneDescription>(null);

  const [isModalOpen, setIsModalOpen] = React.useState<boolean>(false);
  const [currentDialogues, setCurrentDialogues] = React.useState<Dialogue[]>(
    []
  );

  const [dialogueBoxContent, setDialogueBoxContent] = React.useState<
    Dialogue[]
  >([]);

  const playbackTimerRef = useRef<number | null>(null);

  const { message: messageApi } = App.useApp();

  useEffect(() => {
    //遍历storyboardData，判断是否存在boardId。如果不存在，则添加。如果存在，则不添加。
    //判断boardsState中的id是否都在storyboardData，如果不在，则需要在boardsState删除。

    // 第一步：添加新的 boardState
    for (let i = 0; i < storyboardData.length; i++) {
      const shot = storyboardData[i];
      const boardId = shot.shot_id;
      const index = boardsState.findIndex((item) => item.boardId === boardId);
      if (index === -1) {
        setBoardsState((prevState) => [
          ...prevState,
          {
            boardId: boardId,
            loadingText: t("generating_high_definition_image"),
            isRegenerating: false,
          },
        ]);
      }
    }

    // 第二步：删除不再存在的 boardState
    if (boardsState.length > 0) {
      setBoardsState((prevState) => {
        return prevState.filter((boardState) => {
          // 检查此 boardState 的 boardId 是否存在于 storyboardData 中
          return storyboardData.some(
            (shot) => shot.shot_id === boardState.boardId
          );
        });
      });
    }
  }, [storyboardData]);

  const setBoardLoadingText = (boardId: string, loadingText: string) => {
    //从boardsState中找到boardId对应的loadingText
    const boardState = boardsState.find((item) => item.boardId === boardId);
    if (boardState) {
      setBoardsState((prevState) => {
        return prevState.map((item) => {
          if (item.boardId === boardId) {
            return { ...item, loadingText: loadingText };
          }
          return item;
        });
      });
    }
  };

  const setBoardIsRegenerating = (boardId: string, isRegenerating: boolean) => {
    //从boardsState中找到boardId对应的isRegenerating
    const boardState = boardsState.find((item) => item.boardId === boardId);
    if (boardState) {
      setBoardsState((prevState) => {
        return prevState.map((item) => {
          if (item.boardId === boardId) {
            return { ...item, isRegenerating: isRegenerating };
          }
          return item;
        });
      });
    }
  };
  const setBoardShotResource = (boardId: string, resource: ShotResource) => {
    setStoryboardData((prevData) => {
      //从storyboardData中找到boardId对应的shot_resource
      // 创建新的 shots 数组，避免直接修改原数组
      const newShots = [...prevData];

      const index = newShots.findIndex((item) => item.shot_id === boardId);
      if (index === -1) {
        return prevData;
      }

      //需要根据当前index来获取
      const newShotResource = { ...newShots[index].shot_resource, ...resource };
      newShots[index].shot_resource = newShotResource;

      return newShots;
    });
  };

  const handleSetCurrentShot = (shotIndex: number) => {
    if (shotIndex === currentShot.index) {
      return;
    }
    // 显示黑色幕布过渡
    setIsTransitioning(true);
    // 延迟切换镜头，等待黑色幕布显示
    setTimeout(() => {
      setCurrentShot({
        index: shotIndex,
        data: storyboardData[shotIndex],
      });
      // 延迟隐藏黑色幕布，等待新镜头加载
      setTimeout(() => {
        setIsTransitioning(false);
      }, 300);
    }, 300);
  };

  // 加载故事板数据
  useEffect(() => {
    (async () => {
      const data = await projectApi.getStoryboardListById(projectId);
      setStoryboardData(data.result.data);
    })();
  }, []);

  useEffect(() => {
    if (storyboardData.length > 0) {
      if (currentShot.data === null) {
        //刚加载
        setCurrentShot({
          index: 0,
          data: storyboardData[0],
        });
      } else {
        let newShotIndex = 0;
        //需要重新获取index
        const index = storyboardData.findIndex(
          (item) => item.shot_id === currentShot.data?.shot_id
        );
        if (index !== -1) {
          newShotIndex = index;
        } else {
          //这里是删除镜头
          // 否则选择前一个镜头
          newShotIndex = currentShot.index === 0 ? 0 : currentShot.index - 1;
        }
        setCurrentShot({
          index: newShotIndex,
          data: storyboardData[newShotIndex],
        });
      }
    } else {
      setCurrentShot({
        index: 0,
        data: null,
      });
    }
  }, [storyboardData]);

  // 获取当前镜头的播放时长（秒）
  const getShotDuration = (shot: StoryboardShot | null): number => {
    let dialogueDuration = 0; // 默认3秒

    // 根据对话长度估算时长
    if (shot && shot.dialogues && shot.dialogues.length > 0) {
      // 每个对话至少3秒，每10个字符增加1秒
      shot.dialogues.forEach((dialogue) => {
        const contentLength = dialogue.content.length;
        if (contentLength > 0) {
          dialogueDuration += DIALOGUE_PLAYBACK_DURATION;
        }
      });
    }

    if (dialogueDuration > 0) {
      return dialogueDuration;
    } else {
      return 3; // 默认3秒
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
      const adjustedDuration =
        (baseDuration / playbackSpeed + TRANSITION_DURATION / playbackSpeed) *
        1000;

      // 设置新的定时器
      playbackTimerRef.current = window.setTimeout(() => {
        const nextShot = getNextShot(storyboardData, currentShot.index);
        if (nextShot) {
          // 显示黑色幕布过渡
          setIsTransitioning(true);
          // 延迟切换镜头，等待黑色幕布显示
          setTimeout(() => {
            setCurrentShot({
              index: nextShot,
              data: storyboardData[nextShot],
            });
            // 延迟隐藏黑色幕布，等待新镜头加载
            setTimeout(() => {
              setIsTransitioning(false);
            }, 300);
          }, 300);
        } else {
          // 如果已经是最后一个镜头，停止播放
          setIsPlaying(false);
          messageApi.success(t("stop_playback"));
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

    if (nextShotIndex === null) {
      setIsPlaying(false);
      messageApi.info(t("already_last_shot"));
      return;
    }

    setIsPlaying((prev) => !prev);
  };

  // 判断是否为第一个镜头
  const isPreviousDisabled = () => {
    return currentShot.index <= 0;
  };

  // 处理上一个镜头
  const handlePrevious = () => {
    setIsPlaying(false);
    const prevShot = getPrevShot(storyboardData, currentShot.index);
    if (prevShot !== null) {
      // 显示黑色幕布过渡
      setIsTransitioning(true);
      // 延迟切换镜头，等待黑色幕布显示
      setTimeout(() => {
        setCurrentShot({
          index: prevShot,
          data: storyboardData[prevShot],
        });
        // 延迟隐藏黑色幕布，等待新镜头加载
        setTimeout(() => {
          setIsTransitioning(false);
        }, 300);
      }, 300);
    }
  };

  // 判断是否为最后一个镜头
  const isNextDisabled = () => {
    const lastShotIndex = storyboardData.length - 1;
    return currentShot.index === lastShotIndex;
  };

  // 处理下一个镜头
  const handleNext = () => {
    setIsPlaying(false);
    const nextShot = getNextShot(storyboardData, currentShot.index);
    if (nextShot) {
      // 显示黑色幕布过渡
      setIsTransitioning(true);
      // 延迟切换镜头，等待黑色幕布显示
      setTimeout(() => {
        setCurrentShot({
          index: nextShot,
          data: storyboardData[nextShot],
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

  const showBackgroundModal = () => {
    setIsBackgroundModalOpen(true);
  };

  // 获取当前对话
  useEffect(() => {
    // 过滤出 content 不为空的对话
    const validDialogues = currentDialogues.filter(
      (dialogue) => dialogue.content !== ""
    );
    setDialogueBoxContent(validDialogues);
  }, [currentDialogues]);

  const updateShotDialogues = (newDialogues: Dialogue[]) => {
    setCurrentDialogues(newDialogues);

    // 更新 storyboardData 中对应镜头的 dialogues
    if (currentShot.data) {
      setStoryboardData((prevData) => {
        // 创建新的 shots 数组，避免直接修改原数组
        const newShots = [...prevData];

        // 更新特定镜头的 dialogues
        newShots[currentShot.index] = {
          ...newShots[currentShot.index],
          dialogues: newDialogues,
        };

        return newShots;
      });
    }
  };

  const updateBackgroundDesc = (desc: SceneDescription) => {
    setBackgroundDesc(desc);

    // 更新 storyboardData 中对应镜头的 dialogues
    if (currentShot.data) {
      setStoryboardData((prevData) => {
        // 创建新的 shots 数组，避免直接修改原数组
        const newShots = [...prevData];

        // 更新特定镜头的 dialogues
        newShots[currentShot.index] = {
          ...newShots[currentShot.index],
          scene_description: desc,
        };

        return newShots;
      });
    }
  };

  useEffect(() => {
    setBackgroundDesc(currentShot.data?.scene_description);
    setCurrentDialogues(
      currentShot.data ? currentShot.data.dialogues || [] : []
    );
  }, [currentShot.data]);

  const openDialogueEditModal = () => {
    setIsModalOpen(true);
  };

  // 将 handleBoardItemChange 定义为单独的函数
  const handleBoardItemChange = (updatedBoardItem: StoryboardShot) => {
    setStoryboardData((prevData) => {
      // 创建新的 shots 数组，避免直接修改原数组
      const newShots = [...prevData];

      const index = newShots.findIndex(
        (item) => item.shot_id === currentShot.data.shot_id
      );
      newShots[index] = updatedBoardItem;

      return newShots;
    });
  };

  const copyShot = async (shot: StoryboardShot) => {
    const storyboardCopyPayload: StoryboardCopyPayload = {
      projectId: projectId,
      storyboardId: shot.shot_id,
    };
    const res = await dashboardApi.storyboardCopy(storyboardCopyPayload);
    if (res.success && res.result?.code === 0) {
      // 复制当前镜头
      setStoryboardData((prevData) => {
        const newData = [...prevData];
        const index = newData.findIndex(
          (item) => item.shot_id === shot.shot_id
        );

        const newShots = [
          ...newData.slice(0, index), // 获取 index 之前的所有元素
          res.result.data, // 插入新元素
          ...newData.slice(index), // 获取从 index 开始的所有元素（包括原 index 位置的元素）
        ];
        return newShots;
      });
      messageApi.success(res.result?.msg);
    } else {
      messageApi.error(res.result?.msg);
    }
  };

  const deleteShot = async (shotId: string) => {
    //需要等待服务器处理完毕数据，本地再做修改
    const storyboardDeletePayload: StoryboardDeletePayload = {
      projectId: projectId,
      storyboardId: shotId,
    };
    const res = await dashboardApi.storyboardDelete(storyboardDeletePayload);
    if (res.success && res.result?.code === 0) {
      setStoryboardData((prevData) => {
        const newData = [...prevData];

        // 删除当前镜头
        const newShots = newData.filter((item) => item.shot_id !== shotId);

        return newShots;
      });

      messageApi.success(res.result?.msg);
    } else {
      messageApi.error(res.result?.msg);
    }
  };

  const reorderShots = (shots: StoryboardShot[]) => {
    // 更新本地状态
    if (shots.length === 0) {
      return;
    }
    setStoryboardData(shots);
  };

  if (!currentShot.data) return null;

  return (
    <div id="app-container" className="min-w-[622px] overflow-auto">
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
                        <Spin
                          tip={
                            boardsState.find(
                              (item) =>
                                item.boardId === currentShot.data.shot_id
                            )?.loadingText || ""
                          }
                          spinning={
                            boardsState.find(
                              (item) =>
                                item.boardId === currentShot.data.shot_id
                            )?.isRegenerating || false
                          }
                          style={{ height: "100%", maxHeight: "none" }} // Override max-height
                        >
                          <img
                            id="shot-image"
                            src={
                              currentShot.data.shot_resource.shot_resource_url
                            }
                            alt={`${t("shot")}_${currentShot.index + 1}`}
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
                              autoPlayInterval={
                                (DIALOGUE_PLAYBACK_DURATION / playbackSpeed) *
                                1000
                              }
                            />
                            <StoryboardDialoguesEdit
                              boardItem={currentShot.data}
                              isModalOpen={isModalOpen}
                              setIsModalOpen={setIsModalOpen}
                              dialogues={currentDialogues}
                              setDialogues={updateShotDialogues}
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
                            isEdit={true}
                            isRegenerating={
                              boardsState.find(
                                (item) =>
                                  item.boardId === currentShot.data.shot_id
                              )?.isRegenerating || false
                            }
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
                      openDialogueEditModal={openDialogueEditModal}
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
                    projectId={projectId}
                    currentShots={storyboardData}
                    currentShotIndex={currentShot.index}
                    onSelectShot={handleSetCurrentShot}
                    onCopyShot={copyShot}
                    onDeleteShot={deleteShot}
                    onReorderShots={reorderShots}
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
              <StoryboardPictureDescEdit
                boardId={currentShot.data.shot_id}
                isModalOpen={isBackgroundModalOpen}
                setIsModalOpen={setIsBackgroundModalOpen}
                backgroundDesc={backgroundDesc}
                setBackgroundDesc={updateBackgroundDesc}
              />
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
                  <div className="cursor-pointer" onClick={showBackgroundModal}>
                    <div id="shot-background-info">
                      <span className="text-gray-600">
                        {t("scene_background")}：
                      </span>
                      <br />
                      <span>{backgroundDesc?.background || t("none")}</span>
                    </div>

                    {backgroundDesc?.characters &&
                      backgroundDesc.characters.length > 0 && (
                        <div
                          id="character-actions-container"
                          className="mt-3 cursor-pointer"
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
                                  className="flex flex-col items-start mb-3 cursor-pointer"
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
                                        <Avatar
                                          className="w-6 h-6 avatar-top-image"
                                          src={getRoleImageUrl(
                                            character.role_id,
                                            currentShot.data
                                          )}
                                        />
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
                        <div className="text-center">
                          <CellSelect
                            cellValue={currentShot.data.shot_size?.value}
                            dataObj={currentShot.data.shot_size}
                            valueKey="shot_size"
                            storyboardId={currentShot.data.shot_id}
                            options={currentShot.data.shot_size.size_values}
                            selectWidth={100}
                          />
                        </div>
                      </div>
                      {/* <span>{currentShotData.shot_size?.value || "无"}</span> */}
                    </div>
                    <div id="camera-angle-info">
                      <div className="flex justify-between items-center">
                        <span className="text-gray-600">
                          {t("camera_angle")}：
                        </span>
                        <div className="text-center">
                          <CellSelect
                            cellValue={currentShot.data.camera_angle?.value}
                            dataObj={currentShot.data.camera_angle}
                            valueKey="camera_angle"
                            storyboardId={currentShot.data.shot_id}
                            options={currentShot.data.camera_angle.angle_values}
                            selectWidth={100}
                          />
                        </div>
                      </div>
                      {/* <span>{currentShotData.camera_angle?.value || "无"}</span> */}
                    </div>
                    <div id="shot-type-info">
                      <div className="flex justify-between items-center">
                        <span className="text-gray-600">
                          {t("shot_type")}：
                        </span>
                        <div className="text-center">
                          <CellSelect
                            cellValue={currentShot.data?.shot_type.value}
                            dataObj={currentShot.data.shot_type}
                            valueKey="shot_type"
                            storyboardId={currentShot.data.shot_id}
                            options={currentShot.data?.shot_type.type_values}
                            selectWidth={100}
                          />
                        </div>
                      </div>
                      {/* <span>{currentShotData.shot_type?.value || "无"}</span> */}
                    </div>
                    <div id="shot-duration-info">
                      <div className="flex justify-between items-center">
                        <span className="text-gray-600">{t("duration")}：</span>
                        <div className="flex justify-end items-center">
                          <CellInputNumber
                            cellValue={currentShot.data?.shot_time.value}
                            dataObj={currentShot.data.shot_time}
                            valueKey="shot_time"
                            storyboardId={currentShot.data.shot_id}
                            inputWidth={78}
                          />
                          <span className="ml-2">{t("seconds")}</span>
                        </div>
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
