import React from "react";

import { useTranslation } from "react-i18next";
import StoryboardPictureDescEdit from "../StoryboardPictureDescEdit";
import {
  SceneDescription,
  StoryboardShot,
} from "./../../../../types/storyboard";

interface IProps {
  boardItem: StoryboardShot;
  isEdit?: boolean;
}

const StoryboardPictureDesc: React.FC<IProps> = ({
  boardItem,
  isEdit = true,
}: IProps) => {
  const { t } = useTranslation();
  const [isModalOpen, setIsModalOpen] = React.useState<boolean>(false);
  const [backgroundDesc, setBackgroundDesc] = React.useState<SceneDescription>(
    boardItem.scene_description
  );

  const showModal = () => {
    setIsModalOpen(true);
  };

  return (
    <>
      <ul
        onClick={isEdit ? showModal : undefined}
        className={`text-left px-[11px] py-1 rounded-lg h-[184px] w-full overflow-y-auto${
          isEdit ? " hover:bg-white hover:cursor-pointer" : " cursor-default"
        }`}
      >
        <li className="mb-3">
          <span className="text-gray-400">{t("background")}：</span>
          <span>{backgroundDesc?.background}</span>
        </li>
        {backgroundDesc?.characters?.map((item, index) => {
          return (
            <li key={`roleDesc-${index}`} className="mb-3">
              <span className="text-gray-400">{item.role_name}：</span>
              <span>{item.action_and_emotion}</span>
            </li>
          );
        })}
      </ul>
      <StoryboardPictureDescEdit
        boardId={boardItem.shot_id}
        isModalOpen={isModalOpen}
        setIsModalOpen={setIsModalOpen}
        backgroundDesc={backgroundDesc}
        setBackgroundDesc={setBackgroundDesc}
      />
    </>
  );
};

export default StoryboardPictureDesc;
