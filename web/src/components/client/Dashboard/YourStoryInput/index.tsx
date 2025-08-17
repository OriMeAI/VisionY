/**
 * 输入你的故事
 */

import {
  CreateNewContexts,
  ICreateNewContexts,
} from "./../../../../contexts/create-new-contexts";
import arrowTopRightActiveIcon from "./../../../../../assets/images/icons/arrow_top_right_active.svg";
import foldIcon from "./../../../../../assets/images/icons/fold_icon.svg";
import unfoldIcon from "./../../../../../assets/images/icons/unfold_icon.svg";
import { Button, Form, Input } from "antd";
import { useTranslation } from "react-i18next";
import projectApi from "./../../../../api/projectApi";


import React, { useContext, useState, useEffect, lazy, Suspense } from "react";
import style from "./style.module.css";

interface IProps {}

const { TextArea } = Input;
const YourStoryInput: React.FC<IProps> = ({}: IProps) => {
  const { t } = useTranslation();

  const [storiesList, setStoriesList] = useState<any[]>([]);

  useEffect(() => {
    (async () => {
      const data = await projectApi.getProjectStories();
      
      if (data.success) {
        setStoriesList(data.result?.data);
      }
    })();
  }, []);

  const [isFold, setIsFold] = useState<boolean>(false);
  const createNewContexts: ICreateNewContexts =
    useContext<ICreateNewContexts>(CreateNewContexts);
  const onFoldIconClick = () => {
    setIsFold(!isFold);
  };
  const onYourStoryTextChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    createNewContexts.setYourStoryText(e.target.value);
  };
  return (
    <div className={style.yourStoryInputWrapper}>
      <Form.Item>
        <div className="mt-4 relative border rounded-lg h-[430px]">
          <TextArea
            value={createNewContexts.yourStoryText}
            maxLength={15000}
            onChange={onYourStoryTextChange}
            style={{ height: 390, resize: "none" }}
            placeholder={t("your_story_input_placeholder")}
            className="resize-none border-none shadow-none py-2"
          />

          <div
            className={`bg-background rounded-lg absolute bottom-0 left-0 right-0 overflow-hidden transition-all duration-300`}
            style={{ height: isFold ? 40 : 184 }}
          >
            <div
              className="h-10 flex justify-between items-center px-3 cursor-pointer"
              onClick={onFoldIconClick}
            >
              <span className="text-slate-600">{t("your_story_input_no_idea_prompt")}</span>
              <img src={isFold ? unfoldIcon : foldIcon} alt="" />
            </div>
            <div className="px-3 space-y-1 pb-1" style={{ opacity: 1 }}>
              {Array.isArray(storiesList) &&
              storiesList.length > 0
                ? storiesList.map(
                    (templateItem: any, templateIndex: number) => {
                      return (
                        <Button
                          key={`template_item_${templateItem.id}_${templateIndex}`}
                          className="border border-gray-300 px-3 py-2 flex items-center bg-white rounded-lg w-full"
                          onClick={() => {
                            createNewContexts.setYourStoryText(
                              templateItem.content
                            );
                            setIsFold(true);
                          }}
                        >
                          <img src={arrowTopRightActiveIcon} alt="" />
                          <p className="truncate ">{templateItem.title}</p>
                        </Button>
                      );
                    }
                  )
                : null}
            </div>
          </div>
          <div className="absolute -bottom-6 right-0 text-gray-500">
            {createNewContexts.yourStoryText.length} / 15000 {t("your_story_input_character_count")}
          </div>
        </div>
      </Form.Item>
    </div>
  );
};

export default YourStoryInput;
