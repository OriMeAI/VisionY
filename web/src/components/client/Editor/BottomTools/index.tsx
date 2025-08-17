/**
 * 重绘工具栏
 */

import { Button, Input, Space, App } from "antd";
import React, { RefObject, useContext, useState, useRef } from "react";
import { useTranslation } from "react-i18next";
import {
  DetailContexts,
  IDetailContexts,
} from "../../Common/DetailContainer/contexts/detail-contexts";

import {
  EditorContexts,
  IEditorContexts,
} from "./../../../../contexts/editor-contexts";
import { RepaintStatus } from "./../../../../libs/enums";
import style from "./style.module.css";

import { ImageGenerateHistoryItem } from "../../../../libs/interfaces";
import userApi from "./../../../../api/userApi";
import { IUserContexts, UserContexts } from "./../../../../contexts/user-contexts";

import {
  aierhubFetchEventSourceWithAuth,
} from "./../../../../api/aierhubFetch";

interface IBottomToolsProps {
  originStageRef: RefObject<any>;
  originImgSrc: string;
  originImageWidth: RefObject<number>;
  originImageHeight: RefObject<number>;
  onRepaintSuccess?: (historyItems: ImageGenerateHistoryItem[]) => void;
  storyboardId: string;
  lines: any[];
}

const BottomTools: React.FC<IBottomToolsProps> = ({
  originStageRef,
  originImgSrc,
  originImageWidth,
  originImageHeight,
  onRepaintSuccess,
  storyboardId,
  lines,
}: IBottomToolsProps) => {
  const { t } = useTranslation();
  const { message: messageApi } = App.useApp();
  const detailContexts: IDetailContexts =
    useContext<IDetailContexts>(DetailContexts);
  const editorContexts: IEditorContexts =
    useContext<IEditorContexts>(EditorContexts);
  const [imgPrompts, setImgPrompts] = useState<string>("");
  const [isRepainting, setIsRepainting] = useState<boolean>(false);
  const userContexts: IUserContexts =React.useContext<IUserContexts>(UserContexts);

      // 添加 AbortController 引用
    const abortControllerRef = useRef<AbortController | null>(null);

  const onImgPromptsChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setImgPrompts(e.target.value);
  };

  const onRepaintBtnClick = async () => {
    //允许用户全局编辑
    // if (!lines || (Array.isArray(lines) && lines.length === 0)) {
    //   messageApi.info(t("no_lines_warning"));
    //   return;
    // }
    setIsRepainting(true);
    editorContexts.setRepaintStatus(RepaintStatus.Rendering);
    
    // 将stage的宽高和缩放比例设置与原图的宽高一致，以使得最终生成的黑白图的宽高与原图一致
    const originStage = originStageRef.current;
    const originStageWidth = originStage.width();
    const originStageHeight = originStage.height();
    originStage.width(originImageWidth.current / 2);
    originStage.height(originImageHeight.current / 2);
    originStage.scale({
      x: originImageWidth.current / 2 / originStageWidth,
      y: originImageHeight.current / 2 / originStageHeight,
    });

    // 使用 requestAnimationFrame 确保渲染完成
    requestAnimationFrame(() => {
      requestAnimationFrame(async () => {
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

        // 执行画布数据获取和处理
        try {

          var hasMaskData = false
          // 获取第一个 Layer 子节点的 Canvas 对象
          const layer = originStage.findOne("Layer");
          const canvas = layer.getCanvas();

          // 获取 Canvas 对象的 2D 绘图上下文
          const ctx = canvas.getContext("2d");

          const maskImgData = ctx.getImageData(0, 0, canvas.width, canvas.height);

          //修改蒙版的逻辑，启用红色，透明度设定为153/255 = 0.6
          for (var i = 0; i < maskImgData.data.length; i += 4) {
            if (maskImgData.data[i + 3] > 0) {
              maskImgData.data[i] = 255;
              maskImgData.data[i + 1] = 0;
              maskImgData.data[i + 2] = 0;
              maskImgData.data[i + 3] = 153;
              hasMaskData = true
            } else {
              maskImgData.data[i] = 0;
              maskImgData.data[i + 1] = 0;
              maskImgData.data[i + 2] = 0;
              maskImgData.data[i + 3] = 0;
            }
          }
          ctx.putImageData(maskImgData, 0, 0);
          // 导出黑白图像
          const blackAndWhiteDataURL = canvas.toDataURL({
            mimeType: "image/png",
            quality: 1,
          });
          // 成功导出黑白图像后将stage还原到原始尺寸，以便后续用画笔绘制时候能与页面中画笔的路径一致
          originStage.width(originStageWidth);
          originStage.height(originStageHeight);
          originStage.scale({
            x: originStageWidth / (originImageWidth.current / 2),
            y: originStageHeight / (originImageHeight.current / 2),
          });
          console.log("blackAndWhiteDataURL", blackAndWhiteDataURL);
          // 在这里可以将 blackAndWhiteDataURL 保存到文件或进行其他操作

          // 如果有正在进行的请求，先取消
          if (abortControllerRef.current) {
            abortControllerRef.current.abort();
            abortControllerRef.current = null;
          }

          // 创建新的 AbortController
          abortControllerRef.current = new AbortController();
          const signal = abortControllerRef.current.signal;

          const projectId = detailContexts.projectItemObj?.id
          const originImgUrl = originImgSrc
          const originImgWidth = originImageWidth.current
          const originImgHeight = originImageHeight.current
          const maskData = hasMaskData ? blackAndWhiteDataURL : ""

          // 使用封装的函数替代原来的fetchEventSource，并添加signal参数
          await aierhubFetchEventSourceWithAuth(
            `/api/storyboard/shot/repaint`,
            {
              // method: "GET", 数据过长 改为 post
              method: "POST",
              body: JSON.stringify({
                projectId,
                originImgUrl,
                originImgWidth,
                originImgHeight,
                imgPrompts,
                maskData,
                storyboardId
              }),
              signal, // 添加 signal 参数
              onmessage(ev) {
                switch (ev.event) {
                  case "message":
                    // 处理连接成功消息
                    if (ev.data === "Connection successful") {
                      console.log("SSE Connection successful");
                      return;
                    }else if (ev.data === "Complete") {
                      setImgPrompts("");
                      editorContexts.setRepaintStatus(RepaintStatus.Success);
                    }else{
                      onRepaintSuccess && onRepaintSuccess(JSON.parse(ev.data));
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
                  editorContexts.setRepaintStatus(RepaintStatus.Success);
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

          // const res = await editorApi.repaintShot({
          //   projectId: detailContexts.projectItemObj?.id,
          //   originImgUrl: originImgSrc,
          //   originImgWidth: originImageWidth.current,
          //   originImgHeight: originImageHeight.current,
          //   imgPrompts,
          //   maskData: hasMaskData ? blackAndWhiteDataURL : "",
          //   storyboardId: storyboardId,
          // });
          // editorContexts.setRepaintStatus(RepaintStatus.Success);
          // if (res.success && res.result?.code === 0) {
          //   if (res.result?.data) {
          //     setImgPrompts("");
          //     messageApi.success(res.result.msg);
          //     onRepaintSuccess && onRepaintSuccess(res.result.data);
          //   }
          // } else {
          //   if (res.result?.msg) {
          //     messageApi.error(res.result.msg);
          //   }
          // }
        }catch (error) {
            console.error("generate shot error:", error);
            if (error instanceof Error && error.name !== "AbortError") {
              console.log(error.message);
              messageApi.error(t("common_error_dataReceive"));
            } 
        }finally {
          setIsRepainting(false);
        }
      });
    });
  };
  return (
    <div className={`${style.bottomTools} left-1/2`}>
      <Space>
        <Input
          value={imgPrompts}
          placeholder={t("enter_description")}
          className={style.textInput}
          onChange={onImgPromptsChange}
          disabled={isRepainting}
        />
        <Button
          type="primary"
          disabled={!imgPrompts || isRepainting}
          block
          className={`${style.repaintBtn}`}
          onClick={onRepaintBtnClick}
        >
          {t("repaint")}
        </Button>
      </Space>
    </div>
  );
};

export default BottomTools;
