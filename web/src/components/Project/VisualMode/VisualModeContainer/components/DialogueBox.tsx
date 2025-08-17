import React, { useEffect, useState } from "react";
import { Dialogue } from "./../../../../../types/storyboard";
import { useTranslation } from "react-i18next";
import { getRoleImageUrl } from "../utils/storyboardUtils";
import { Avatar } from "antd";

interface DialogueBoxProps {
  dialogues: Dialogue[];
  isVisible: boolean;
  currentShot?: any; // 添加当前镜头数据，用于获取角色资源URL
  autoPlay?: boolean; // 是否自动播放对话
  autoPlayInterval?: number; // 自动播放间隔时间(毫秒)
}

const DialogueBox: React.FC<DialogueBoxProps> = ({
  dialogues,
  isVisible,
  currentShot,
  autoPlay = false,
  autoPlayInterval = 3000,
}) => {
  const { t } = useTranslation();
  const [currentDialogueIndex, setCurrentDialogueIndex] = useState<number>(0);

  // 自动播放对话的定时器
  useEffect(() => {
    let timer: NodeJS.Timeout | null = null;

    if (autoPlay && isVisible && dialogues && dialogues.length > 1) {
      timer = setInterval(() => {
        goToNextDialogue();
      }, autoPlayInterval);
    }

    return () => {
      if (timer) clearInterval(timer);
    };
  }, [autoPlay, isVisible, dialogues, currentDialogueIndex, autoPlayInterval]);

  // 当对话列表变化时，重置当前索引
  useEffect(() => {
    // 立即重置索引，确保在渲染前更新
    setCurrentDialogueIndex(0);
  }, [dialogues]);

  // 确保currentDialogueIndex不会超出dialogues的范围
  useEffect(() => {
    if (
      dialogues &&
      dialogues.length > 0 &&
      currentDialogueIndex >= dialogues.length
    ) {
      setCurrentDialogueIndex(0);
    }
  }, [dialogues, currentDialogueIndex]);

  if (!dialogues || dialogues.length === 0) return null;

  // 切换到下一条对话
  const goToNextDialogue = () => {
    if (dialogues.length <= 1 || currentDialogueIndex === dialogues.length - 1)
      return;

    setCurrentDialogueIndex((prevIndex) => prevIndex + 1);
  };

  // 切换到上一条对话
  const goToPrevDialogue = () => {
    if (dialogues.length <= 1 || currentDialogueIndex === 0) return;

    setCurrentDialogueIndex((prevIndex) => prevIndex - 1);
  };

  // 安全地获取当前对话，确保索引在有效范围内
  const safeIndex =
    dialogues && dialogues.length > 0
      ? Math.min(currentDialogueIndex, dialogues.length - 1)
      : 0;
  const currentDialogue =
    dialogues && dialogues.length > 0 ? dialogues[safeIndex] : null;

  // 如果没有有效的对话数据或对话框不可见，返回空
  if (!currentDialogue || !isVisible) return null;

  return (
    <div
      id="dialogue-box-container"
      className="relative px-3 pb-3 w-[85%] max-w-3xl mx-auto z-10 opacity-100 fade-in"
    >
      {/* 简化后的对话框结构 */}
      <div
        id="dialogue-box"
        className="flex items-start bg-gray-800 bg-opacity-85 p-5 rounded-lg shadow-lg text-white backdrop-blur-sm border border-gray-700 min-h-[100px]"
      >
        {/* 只在非旁白角色时显示头像 */}
        {currentDialogue.role_id &&
          currentDialogue.role_id !== "voiceover" && (
            <div id="character-avatar-container" className="flex-shrink-0 mr-4">
              {getRoleImageUrl(currentDialogue.role_id, currentShot) ? (
                <Avatar
                  className="w-14 h-14 rounded-full object-cover border-2 border-primary-light shadow-md avatar-top-image"
                  src={getRoleImageUrl(currentDialogue.role_id, currentShot)}
                />
              ) : (
                <Avatar
                  className="w-14 h-14 rounded-full object-cover border-2 border-primary-light shadow-md avatar-top-image"
                />
              )}
            </div>
          )}

        {/* 对话内容区域 */}
        <div
          id="dialogue-content-area"
          className="flex-1 flex flex-col justify-center"
        >
          <div className="flex justify-between items-center mb-1">
            <div id="role-name" className="font-semibold text-primary-light">
              {currentDialogue.role_name}
            </div>
            <div
              id="dialogue-nav-container"
              className="flex items-center space-x-2"
            >
              <button
                id="prev-dialogue-btn"
                className={`bg-gray-700 text-white rounded-full p-1 transition-all ${
                  currentDialogueIndex === 0 || dialogues.length <= 1
                    ? "opacity-30 cursor-not-allowed"
                    : "hover:bg-gray-600 opacity-70 hover:opacity-100"
                }`}
                onClick={goToPrevDialogue}
                aria-label={t("dialogue_box_previous")}
                disabled={currentDialogueIndex === 0 || dialogues.length <= 1}
              >
                <svg
                  id="prev-dialogue-icon"
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-4 w-4"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M15 19l-7-7 7-7"
                  />
                </svg>
              </button>

              <div
                id="dialogue-counter"
                className="text-xs text-white bg-gray-700 px-2 py-1 rounded-full opacity-70"
              >
                {currentDialogueIndex + 1} / {dialogues.length}
              </div>

              <button
                id="next-dialogue-btn"
                className={`bg-gray-700 text-white rounded-full p-1 transition-all ${
                  currentDialogueIndex === dialogues.length - 1 ||
                  dialogues.length <= 1
                    ? "opacity-30 cursor-not-allowed"
                    : "hover:bg-gray-600 opacity-70 hover:opacity-100"
                }`}
                onClick={goToNextDialogue}
                aria-label={t("dialogue_box_next")}
                disabled={
                  currentDialogueIndex === dialogues.length - 1 ||
                  dialogues.length <= 1
                }
              >
                <svg
                  id="next-dialogue-icon"
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-4 w-4"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M9 5l7 7-7 7"
                  />
                </svg>
              </button>
            </div>
          </div>
          <div id="dialogue-text">{currentDialogue.content}</div>
        </div>
      </div>
    </div>
  );
};

export default DialogueBox;
