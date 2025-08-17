/**
 * 画面
 */

import { Button, message, Spin, Tag, Tooltip, App } from "antd";
import genImgIcon from "./../../../../../assets/images/pages/boardView/gen_img_icon.svg";
import genImgIconHover from "./../../../../../assets/images/pages/boardView/gen_img_icon_hover.svg";
import hdHoverIcon from "./../../../../../assets/images/pages/boardView/hd_hover_icon.svg";
import hdIcon from "./../../../../../assets/images/pages/boardView/hd_icon.svg";
import previewIcon from "./../../../../../assets/images/pages/boardView/preview_icon.svg";
import previewIconHover from "./../../../../../assets/images/pages/boardView/preview_icon_hover.svg";
import userApi from "./../../../../api/userApi";
import { IUserContexts, UserContexts } from "./../../../../contexts/user-contexts";

import { ShotResource, StoryboardShot } from "./../../../../types/storyboard";

import React, { useContext, useEffect, useState,useRef } from "react";
import { createPortal } from "react-dom";
import { useTranslation } from "react-i18next"; // 添加 useTranslation 导入
import {
  DetailContexts,
  IDetailContexts,
} from "../DetailContainer/contexts/detail-contexts";
import ImagePreview from "../ImagePreview";
import PartialRedrawBtn from "../PartialRedrawBtn";
import StoryboardImgHistory from "../StoryboardImgHistory";
import StoryboardReplaceImg from "../StoryboardReplaceImg";

import {
  aierhubFetchEventSourceWithAuth
} from "./../../../../api/aierhubFetch";

interface IProps {
  boardItem: StoryboardShot;
  isEdit?: boolean;
  isRegenerating: boolean;
  setBoardLoadingText: (boardId:string,loadingText: string) => void;
  setBoardIsRegenerating: (boardId:string,isRegenerating: boolean) => void;
  setBoardShotResource: (boardId:string,resourceObj: ShotResource) => void;
}

// 定义预览图片项的接口
interface PreviewImageItem {
  id: string;
  src: string;
  alt?: string;
}

const StoryboardEditBtns: React.FC<IProps> = React.memo(
  ({
    boardItem,
    isEdit = true,
    isRegenerating,
    setBoardLoadingText,
    setBoardIsRegenerating,
    setBoardShotResource,
  }: IProps) => {
    const { t } = useTranslation(); // 添加 useTranslation hook
    const detailContexts: IDetailContexts = useContext<IDetailContexts>(DetailContexts);

    const { message: messageApi } = App.useApp();

    // 预览图片
    const [previewImageVisible, setPreviewImageVisible] = React.useState<boolean>(false);

    // 使用正确的类型定义
    const [previewImageList, setPreviewImageList] = useState<PreviewImageItem[]>([]);

    // 添加 AbortController 引用
    const abortControllerRef = useRef<AbortController | null>(null);

    const userContexts: IUserContexts =React.useContext<IUserContexts>(UserContexts);


    useEffect(() => {
      if (boardItem.shot_resource) {
        setPreviewImageList([
          {
            id: boardItem.shot_id,
            src: boardItem.shot_resource?.shot_resource_url,
            alt: boardItem.scene_description?.background,
          },
        ]);
      }
    }, [boardItem]);

    const setLoadingText = (loadingText: string) => {
      setBoardLoadingText(boardItem.shot_id,loadingText);
    };

    const setIsRegenerating = (isRegenerating: boolean) => {
      setBoardIsRegenerating(boardItem.shot_id,isRegenerating);
    };
    const setShotResource = (resource: ShotResource) => {
      setBoardShotResource(boardItem.shot_id,resource);
      setPreviewImageList([
        {
          id: boardItem.shot_id,
          src: resource.shot_resource_url,
          alt: boardItem.scene_description?.background,
        },
      ]);
    }

    // 生成高清图片
    const generateHighDefinitionImage = async () => {
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


      setLoadingText(t("generating_high_definition_image")); // 使用 t 函数
      setIsRegenerating(true);


      // 如果有正在进行的请求，先取消
      if (abortControllerRef.current) {
        abortControllerRef.current.abort();
        abortControllerRef.current = null;
      }

        // 创建新的 AbortController
        abortControllerRef.current = new AbortController();
        const signal = abortControllerRef.current.signal;

        try {
          // 使用封装的函数替代原来的fetchEventSource，并添加signal参数
          await aierhubFetchEventSourceWithAuth(
            `/api/storyboard/shot/hd_resolution?projectId=${detailContexts.projectItemObj?.id}&storyboardId=${boardItem.shot_id}`,
            {
              method: "GET",
              signal, // 添加 signal 参数
              onmessage(ev) {
                switch (ev.event) {
                  case "message":
                    // 处理连接成功消息
                    if (ev.data === "Connection successful") {
                      console.log("SSE Connection successful");
                      return;
                    }else if (ev.data === "Complete") {
                      setIsRegenerating(false);
                    }else{
                      setShotResource(JSON.parse(ev.data));
                    }
                  break;
                case "progress":
                  messageApi.success(ev.data);
                  break;
                case "warning":
                  messageApi.warning(ev.data);
                  break;
                case "error":
                  messageApi.error(ev.data);
                  setIsRegenerating(false);
                  //TODO need more friendly function to handle error by soongxl
                  break;
                default:
                  break;
                }
              },
              onerror(err) {
                console.error("SSE Error:", err);
                throw err;
              },
              onclose: () => {
                // 确保在连接关闭时清理资源
                abortControllerRef.current = null;
              },
            }
          );
        } catch (error) {
          console.error("generate shot error:", error);
          setIsRegenerating(false);
          if (error instanceof Error && error.name !== "AbortError") {
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

      // const res = await projectApi.generateHighDefinitionImage({
      //   projectId: detailContexts.projectItemObj?.id,
      //   storyboardId: boardItem.shot_id,
      // });
      
      // setIsRegenerating(false);
      // if (res.success && res.result?.code === 0) {
      //   messageApi.success(res.result.msg);
      //   setShotResource(res.result.data);
      // } else {
      //   if (res.result?.msg) {
      //     messageApi.error(res.result.msg);
      //   }
      // }
    };


    const regenerateShotImage = async () => {
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
      
      setLoadingText(t("image_regenerating")); // 使用 t 函数
      setIsRegenerating(true);

      // 如果有正在进行的请求，先取消
      if (abortControllerRef.current) {
        abortControllerRef.current.abort();
        abortControllerRef.current = null;
      }

        // 创建新的 AbortController
        abortControllerRef.current = new AbortController();
        const signal = abortControllerRef.current.signal;

        try {
          // 使用封装的函数替代原来的fetchEventSource，并添加signal参数
          await aierhubFetchEventSourceWithAuth(
            `/api/storyboard/shot/regenerate?projectId=${detailContexts.projectItemObj?.id}&storyboardId=${boardItem.shot_id}`,
            {
              method: "GET",
              signal, // 添加 signal 参数
              onmessage(ev) {
                switch (ev.event) {
                  case "message":
                    // 处理连接成功消息
                    if (ev.data === "Connection successful") {
                      console.log("SSE Connection successful");
                      return;
                    }else if (ev.data === "Complete") {
                      setIsRegenerating(false);
                    }else{
                      setShotResource(JSON.parse(ev.data));
                    }
                  break;
                case "progress":
                  messageApi.success(ev.data);
                  break;
                case "warning":
                  messageApi.warning(ev.data);
                  break;
                case "error":
                  messageApi.error(ev.data);
                  setIsRegenerating(false);
                  //TODO need more friendly function to handle error by soongxl
                  break;
                default:
                  break;
                }
              },
              onerror(err) {
                console.error("SSE Error:", err);
                throw err;
              },
              onclose: () => {
                // 确保在连接关闭时清理资源
                abortControllerRef.current = null;
              },
            }
          );
        } catch (error) {
          console.error("generate shot error:", error);
          setIsRegenerating(false);
          if (error instanceof Error && error.name !== "AbortError") {
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
      <div className={`group/div ${!isRegenerating ? "" : "hidden"}`}>
        <div className="absolute top-0 left-0 z-[1] w-full h-full opacity-0 transition-opacity duration-200 group-hover/div:opacity-100">
          <div className="absolute top-2 right-2 flex items-center space-x-0.5 2xl:space-x-1">
            {isEdit ? (
              <>
                <Tooltip placement="top" title={t("regenerate")}>
                  <Button
                    icon={
                      <div className="relative w-6 h-6 flex items-center justify-center">
                        <img
                          src={genImgIcon}
                          alt="preview"
                          className="absolute inset-0 m-auto opacity-100 transition-opacity duration-200 group-hover:opacity-0"
                        />
                        <img
                          src={genImgIconHover}
                          alt="preview hover"
                          className="absolute inset-0 m-auto opacity-0 transition-opacity duration-200 group-hover:opacity-100"
                        />
                      </div>
                    }
                    className="bg-white/80 group"
                    onClick={regenerateShotImage}
                  />
                </Tooltip>
                <Tooltip placement="top" title={t("high_definition_image")}>
                  <Button
                    icon={
                      <div className="relative w-6 h-6 flex items-center justify-center">
                        <img
                          src={hdIcon}
                          alt="preview"
                          className="absolute inset-0 m-auto opacity-100 transition-opacity duration-200 group-hover:opacity-0"
                        />
                        <img
                          src={hdHoverIcon}
                          alt="preview hover"
                          className="absolute inset-0 m-auto opacity-0 transition-opacity duration-200 group-hover:opacity-100"
                        />
                      </div>
                    }
                    className="bg-white/80 group"
                    onClick={generateHighDefinitionImage}
                  />
                </Tooltip>
                <PartialRedrawBtn
                  boardId={boardItem.shot_id}
                  setSelectShotResource={setShotResource}
                />

                <StoryboardReplaceImg
                  boardId={boardItem.shot_id}
                  setSelectShotResource={setShotResource}
                  setIsRegenerating={setIsRegenerating}
                  setLoadingText={setLoadingText}
                />
                <StoryboardImgHistory
                  boardId={boardItem.shot_id}
                  setSelectShotResource={setShotResource}
                  setIsRegenerating={setIsRegenerating}
                  setLoadingText={setLoadingText}
                />
              </>
            ) : null}

            {createPortal(
              <ImagePreview
                imageList={previewImageList}
                current={0}
                previewImageVisible={previewImageVisible}
                setPreviewImageVisible={setPreviewImageVisible}
              />,
              document.body
            )}
            <Tooltip placement="top" title={t("view_large_image")}>
              <Button
                icon={
                  <div className="relative w-6 h-6 flex items-center justify-center">
                    <img
                      src={previewIcon}
                      alt="preview"
                      className="absolute inset-0 m-auto opacity-100 transition-opacity duration-200 group-hover:opacity-0"
                    />
                    <img
                      src={previewIconHover}
                      alt="preview hover"
                      className="absolute inset-0 m-auto opacity-0 transition-opacity duration-200 group-hover:opacity-100"
                    />
                  </div>
                }
                className="bg-white/80 group"
                onClick={() => {
                  setPreviewImageVisible(true);
                }}
              />
            </Tooltip>
          </div>
        </div>
      </div>
    );
  }
);

export default StoryboardEditBtns;
