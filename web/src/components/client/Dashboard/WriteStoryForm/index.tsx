/**
 * 写故事表单
 */

import {
  CreateNewContexts,
  ICreateNewContexts,
} from "./../../../../contexts/create-new-contexts";
import { WriteStoryInputType } from "./../../../../libs/enums";
import { Segmented } from "antd";
import { useTranslation } from "react-i18next";
import React, { useContext } from "react";
import style from "./style.module.css";

import ExpandStoryInput from "../ExpandStoryInput";
import ScriptUpload from "../ScriptUpload";
import YourStoryInput from "../YourStoryInput";

interface IProps {}

const WriteStoryForm: React.FC<IProps> = ({}: IProps) => {
  const { t } = useTranslation();
  const createNewContexts: ICreateNewContexts =
    useContext<ICreateNewContexts>(CreateNewContexts);
  const onSegmentedChange = (value: WriteStoryInputType) => {
    createNewContexts.setWriteStoryInputType(value);
  };
  const writeStoryInputNodeMap = {
    [WriteStoryInputType.AiExtension]: (<ExpandStoryInput />),
    [WriteStoryInputType.InputYourStory]: (<YourStoryInput />),
    [WriteStoryInputType.UploadScript]: (<ScriptUpload />),
  };
  return (
    <div className={style.writeStoryFormWrapper}>
      <Segmented
        size="large"
        options={[
          {
            label: (
              <div className="flex items-center justify-center h-full w-full">
                <span className="font-semibold bg-gradient-to-r from-[#7873f5] to-[#ec77ab] bg-clip-text text-transparent overflow-hidden whitespace-nowrap text-ellipsis text-center">
                  {t("write_story_form_ai_extension")}
                </span>
              </div>
            ),
            value: WriteStoryInputType.AiExtension,
          },
          { 
            label: (
              <div className="flex items-center justify-center h-full w-full">
                <span className="overflow-hidden whitespace-nowrap text-ellipsis text-center">
                  {t("write_story_form_input_your_story")}
                </span>
              </div>
            ),
            value: WriteStoryInputType.InputYourStory,
            disabled: createNewContexts.isExpandingStory
          },
          { 
            label: (
              <div className="flex items-center justify-center h-full w-full">
                <span className="overflow-hidden whitespace-nowrap text-ellipsis text-center">
                {t("write_story_form_upload_script")}
                </span>
              </div>
            ),
            value: WriteStoryInputType.UploadScript,
            disabled: createNewContexts.isExpandingStory
          },
        ]}
        onChange={onSegmentedChange}
      />
      {writeStoryInputNodeMap[createNewContexts.writeStoryInputType]}
    </div>
  );
};

export default WriteStoryForm;
