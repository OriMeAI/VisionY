import React from "react";
import { useTranslation } from "react-i18next";
import StoryboardDialoguesEdit from "../StoryboardDialoguesEdit";
import { Dialogue, StoryboardShot } from "./../../../../types/storyboard";
import { Flex, Input, App } from "antd";

interface IProps {
  boardItem: StoryboardShot;
  isEdit?: boolean;
}

const StoryboardDialogues: React.FC<IProps> = ({
  boardItem,
  isEdit = true,
}: IProps) => {
  const [isModalOpen, setIsModalOpen] = React.useState<boolean>(false);
  const [dialogues, setDialogues] = React.useState<Dialogue[]>(boardItem.dialogues || []);
  const { message: messageApi } = App.useApp();

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
        {dialogues?.map((item, index) => {
          return (
            <li key={`dialogue-${index}`} className="mb-3">
              <span className="text-gray-400">{item.role_name}：</span>
              <span>{item.content}</span>
            </li>
          );
        })}
      </ul>

      <StoryboardDialoguesEdit
        boardItem={boardItem}
        isModalOpen={isModalOpen}
        setIsModalOpen={setIsModalOpen}
        dialogues={dialogues}
        setDialogues={setDialogues}
      />
    </>
  );
};

export default StoryboardDialogues;
