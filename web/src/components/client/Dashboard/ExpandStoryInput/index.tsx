/**
 * ai扩写故事
 */

import { aierhubFetchEventSourceWithAuth } from "./../../../../api/aierhubFetch";
import { Button, Form, Input, App } from "antd";
import arrowRightActiveIcon from "./../../../../../assets/images/icons/arrow_right_active.svg";
import aiExtensionBtnIcon from "./../../../../../assets/images/pages/workspace/ai_extension_btn_icon.svg";
import aiExtensionBtnIconWhite from "./../../../../../assets/images/pages/workspace/ai_extension_btn_icon_white.svg";
import refreshIcon from "./../../../../../assets/images/pages/workspace/refresh_icon.svg";
import {
  CreateNewContexts,
  ICreateNewContexts,
} from "./../../../../contexts/create-new-contexts";

import React, { useContext, useRef, useEffect } from "react";
import style from "./style.module.css";
import { useTranslation } from "react-i18next";
import { IUserContexts, UserContexts } from "./../../../../contexts/user-contexts";
import userApi from "./../../../../api/userApi";


interface IProps {}

const { TextArea } = Input;

const ExpandStoryInput: React.FC<IProps> = ({}: IProps) => {
  const { t } = useTranslation();
  const { message: messageApi } = App.useApp();
  const [firstExpand, setFirstExpand] = React.useState<boolean>(true);
  const createNewContexts: ICreateNewContexts =
    useContext<ICreateNewContexts>(CreateNewContexts);
   const userContexts: IUserContexts =React.useContext<IUserContexts>(UserContexts);


  // 使用 useRef 保存 AbortController 实例
  const abortControllerRef = useRef<AbortController | null>(null);
  
  // 组件卸载时取消所有进行中的请求
  useEffect(() => {
    return () => {
      if (abortControllerRef.current) {
        abortControllerRef.current.abort();
      }
    };
  }, []);

  const onOriginStoryTextChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    createNewContexts.setOriginStoryText(e.target.value);
  };
  const onExpandedStoryTextChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    createNewContexts.setExpandedStoryText(e.target.value);
  };
  const expandStory = async () => {
    if (userContexts.isAuthenticated) {
      const data = await userApi.getUserInfo();
      if (!data.success) return;
      userContexts.setUserInfo(data.result.data);
      if(data.result?.data?.credits < 1){
        messageApi.error(t("common_error_noCredits"));
        return;
      }
    }else{
      messageApi.error(t("common_error_noLogin"));
      return;
    }

    const inputContent = createNewContexts.originStoryText.trim().replace(/\s+/g, ' ');

    if (inputContent.length < 6) {
      messageApi.warning(t("expand_story_input_min_length_warning"));
      return;
    }

    // 如果有正在进行的请求，先取消
    if (abortControllerRef.current) {
      abortControllerRef.current.abort();
    }
    
    // 创建新的 AbortController
    abortControllerRef.current = new AbortController();
    const signal = abortControllerRef.current.signal;

    setFirstExpand(false);
    createNewContexts.setExpandedStoryText("");
    createNewContexts.setProjectInfoFold(true);
    createNewContexts.setIsExpandingStory(true);
    try {
      // 使用封装的函数替代原来的fetchEventSource，并添加signal参数
      await aierhubFetchEventSourceWithAuth(`/api/storyboard/create/expand_write`, {
        method: "POST",
        signal, // 添加 signal 参数
        body: JSON.stringify({ text: createNewContexts.originStoryText }),
        onmessage(ev) {
          if (ev.data === "Complete") {
            createNewContexts.setIsExpandingStory(false);
            return;
          }else{
            const data = JSON.parse(ev.data);
            createNewContexts.setExpandedStoryText((prev) => prev + data.text);
          }
        },
        onopen: async (response) => {
          if (!response.ok) {
            createNewContexts.setIsExpandingStory(false);
            messageApi.error(`${t("common_error_requestFailed")}: ${response.status}`);
          }
          return Promise.resolve();
        },
        onerror(err) {
          console.error("SSE Error:", err);
          throw err;
        },
        onclose: () => {
          // 连接关闭时的安全重置
          if (createNewContexts.isExpandingStory) {
            createNewContexts.setIsExpandingStory(false);
          }
          return;
        }
      });
    } catch (error) {
      console.error("Expand story error:", error);
      createNewContexts.setIsExpandingStory(false);
      if (error instanceof Error && error.name !== 'AbortError') {
        console.log(error.message);
        messageApi.error(t("common_error_dataReceive"));
      }
    } finally {
      if (abortControllerRef.current) {
        abortControllerRef.current.abort();
      }
      // 请求完成后清除 AbortController 引用
      abortControllerRef.current = null;
    }
  };
  return (
    <div
      className={`mt-4 flex w-full space-x-2 ${style.expandStoryInputWrapper}`}
    >
      <div
        className={
          createNewContexts.isExpandingStory
            ? "min-h-[60px] min-w-[300px] place-items-center bg-white p-1 text-black relative border rounded-lg h-[430px] w-1/2 flex items-start"
            : `relative border rounded-lg h-[430px] w-${
                createNewContexts.projectInfoFold ? "1/2" : "full"
              }`
        }
        style={
          createNewContexts.isExpandingStory
            ? ({ "--border-radius": "8px" } as React.CSSProperties)
            : {}
        }
      >
        {createNewContexts.isExpandingStory ? (
          <div
            className="before:bg-shine-size before:absolute before:inset-0 before:aspect-square before:size-full before:rounded-[--border-radius] before:p-[--border-width] before:will-change-[background-position] before:content-[''] before:![-webkit-mask-composite:xor] before:![mask-composite:exclude] before:[background-image:--background-radial-gradient] before:[background-size:300%_300%] before:[mask:--mask-linear-gradient] motion-safe:before:animate-shine"
            style={
              {
                "--border-width": "1px",
                "--border-radius": "8px",
                "--duration": "14s",
                "--mask-linear-gradient":
                  "linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0)",
                "--background-radial-gradient":
                  "radial-gradient(transparent,transparent, #A07CFE,#FE8FB5,#FFBE7B,transparent,transparent)",
              } as React.CSSProperties
            }
          />
        ) : null}
        <TextArea
          maxLength={1000}
          value={createNewContexts.originStoryText}
          onChange={onOriginStoryTextChange}
          style={{ height: 360, resize: "none" }}
          placeholder={t("expand_story_input_placeholder")}
          className="min-h-[360px] resize-none border-none shadow-none py-2 whitespace-pre-line"
        />
        <Button
          type="primary"
          size="large"
          className={`absolute bottom-3 right-3 left-3 ${
            createNewContexts.isExpandingStory ? "border-none" : ""
          }`}
          icon={
            <img
              src={
                createNewContexts.isExpandingStory
                  ? aiExtensionBtnIconWhite
                  : firstExpand
                  ? aiExtensionBtnIcon
                  : createNewContexts.projectInfoFold
                  ? refreshIcon
                  : aiExtensionBtnIcon
              }
              alt=""
            />
          }
          onClick={expandStory}
          disabled={createNewContexts.isExpandingStory}
          ghost
        >
          {createNewContexts.isExpandingStory
            ? t("expand_story_input_creating")
            : firstExpand
            ? t("expand_story_input_ai_expand_story")
            : createNewContexts.projectInfoFold
            ? t("expand_story_input_rewrite")
            : t("expand_story_input_continue")}

          {createNewContexts.isExpandingStory ? null : firstExpand ? (
            <img src={arrowRightActiveIcon} alt="" />
          ) : createNewContexts.projectInfoFold ? null : (
            <img src={arrowRightActiveIcon} alt="" />
          )}
        </Button>
        <div className="absolute -bottom-6 right-0 text-gray-500">
          {createNewContexts.originStoryText.length} / 1000
        </div>
      </div>
      {createNewContexts.projectInfoFold ? (
        <div className="relative border rounded-lg h-[430px] w-1/2">
          <Form.Item>
            <TextArea
              value={createNewContexts.expandedStoryText}
              maxLength={6000}
              onChange={onExpandedStoryTextChange}
              style={{ height: 428, resize: "none" }}
              placeholder={t("expand_story_input_expanded_placeholder")}
              className="min-h-[428px] resize-none border-none shadow-none py-2 whitespace-pre-line"
            />
          </Form.Item>
          <div className="absolute -bottom-6 right-0 text-gray-500">
            {createNewContexts.expandedStoryText.length} / 6000
          </div>
        </div>
      ) : null}
    </div>
  );
};

export default ExpandStoryInput;
