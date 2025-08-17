import { StoryboardShot } from "./../../../../../types/storyboard";
import React from "react";
import { useTranslation } from "react-i18next";

export type PlaybackSpeed = 0.5 | 1 | 2;

interface PlaybackControlsProps {
  openDialogueEditModal?: () => void;
  boardItem: StoryboardShot;
  isPlaying: boolean;
  playbackSpeed: PlaybackSpeed;
  onPlayPause: () => void;
  onPrevious: () => void;
  onNext: () => void;
  onSpeedChange: (speed: PlaybackSpeed) => void;
  isPreviousDisabled?: boolean;
  isNextDisabled?: boolean;
  isDialogueVisible?: boolean;
  onToggleDialogue?: () => void;
}

const PlaybackControls: React.FC<PlaybackControlsProps> = ({
  openDialogueEditModal,
  isPlaying,
  playbackSpeed,
  onPlayPause,
  onPrevious,
  onNext,
  onSpeedChange,
  isPreviousDisabled = false,
  isNextDisabled = false,
  isDialogueVisible = true,
  onToggleDialogue = () => {},
}) => {
  const { t } = useTranslation();
  return (
    <div
      id="playback-controls-wrapper"
      className="flex flex-wrap md:flex-nowrap items-center space-x-0 md:space-x-3 px-5 py-4 gap-3 bg-gray-100 bg-opacity-90 rounded-lg shadow-sm"
    >
      {/* 播放速度选择 - 左侧 */}
      <div
        id="playback-speed-controls"
        className="flex items-center space-x-2 justify-start flex-1"
      >
        <span
          id="playback-speed-label-desktop"
          className="text-xs text-gray-600 hidden sm:inline"
        >
          {t("playback_speed")}
        </span>
        <span
          id="playback-speed-label-mobile"
          className="text-xs text-gray-600 sm:hidden"
        >
          {t("playback_speed")}
        </span>
        {[0.5, 1, 2].map((speed) => (
          <button
            id={`playback-speed-${speed}`}
            key={speed}
            className={`px-2.5 py-1.5 rounded-md text-xs transition-all ${
              playbackSpeed === speed
                ? "bg-primary text-white"
                : "bg-gray-200 hover:bg-gray-300 text-gray-700 hover:shadow-md"
            }`}
            onClick={() => onSpeedChange(speed as PlaybackSpeed)}
          >
            {speed}x
          </button>
        ))}
      </div>

      {/* 播放控制区域 - 中间 */}
      <div
        id="playback-navigation-controls"
        className="flex items-center justify-center space-x-3 flex-1"
      >
        {/* 上一个镜头按钮 */}
        <button
          id="previous-shot-btn"
          className={`p-2.5 rounded-full transition-all ${
            isPreviousDisabled
              ? "bg-gray-300 text-gray-400 cursor-not-allowed"
              : "bg-gray-200 hover:bg-gray-300 text-gray-700 hover:shadow-md"
          }`}
          onClick={onPrevious}
          disabled={isPreviousDisabled}
          aria-label={t("previous_shot")}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-5 w-5"
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

        {/* 播放/暂停按钮 */}
        <button
          id="play-pause-btn"
          className="bg-primary p-3.5 rounded-full transition-all hover:shadow-md text-white"
          onClick={onPlayPause}
          aria-label={isPlaying ? t("pause") : t("play")}
        >
          {isPlaying ? (
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M10 9v6m4-6v6m7-3a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
          ) : (
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"
              />
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
          )}
        </button>

        {/* 下一个镜头按钮 */}
        <button
          id="next-shot-btn"
          className={`p-2.5 rounded-full transition-all ${
            isNextDisabled
              ? "bg-gray-300 text-gray-400 cursor-not-allowed"
              : "bg-gray-200 hover:bg-gray-300 text-gray-700 hover:shadow-md"
          }`}
          onClick={onNext}
          disabled={isNextDisabled}
          aria-label={t("next_shot")}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-5 w-5"
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

      {/* 对话框显示控制 - 右侧 */}
      <div
        id="dialogue-visibility-controls"
        className="flex items-center justify-end flex-1"
      >
        <button
          id="toggle-dialogue-btn"
          className={`flex items-center space-x-1 px-3 py-1.5 rounded-md text-xs transition-all ${
            isDialogueVisible
              ? "bg-primary text-white"
              : "bg-gray-200 hover:bg-gray-300 text-gray-700 hover:shadow-md"
          }`}
          onClick={onToggleDialogue}
          aria-label={isDialogueVisible ? t("hide_dialogue") : t("show_dialogue")}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-4 w-4 mr-1"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            {isDialogueVisible ? (
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M3.98 8.223A10.477 10.477 0 001.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.45 10.45 0 0112 4.5c4.756 0 8.773 3.162 10.065 7.498a10.523 10.523 0 01-4.293 5.774M6.228 6.228L3 3m3.228 3.228l3.65 3.65m7.894 7.894L21 21m-3.228-3.228l-3.65-3.65m0 0a3 3 0 10-4.243-4.243m4.242 4.242L9.88 9.88"
              />
            ) : (
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"
              />
            )}
          </svg>
          <span>{isDialogueVisible ? t("hide") : t("show")}</span>
        </button>
      </div>
    </div>
  );
};

export default PlaybackControls;
