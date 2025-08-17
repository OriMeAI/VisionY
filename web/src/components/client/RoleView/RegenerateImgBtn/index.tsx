/**
 * 角色页面
 */

import { LoadingOutlined } from "@ant-design/icons";
import { Button, App } from "antd";
import genImgIcon from "./../../../../../assets/images/pages/roleView/role_gen_img_icon.svg";
import purpleGenImgIcon from "./../../../../../assets/images/pages/roleView/purple_gen_img_icon.svg";
import projectApi from "./../../../../api/projectApi";

import React, { useContext, useState,useRef } from "react";
import {
  IRoleViewContexts,
  RoleViewContexts,
} from "../../../../contexts/role-view-contexts";
import style from "./style.module.css";
import { useTranslation } from "react-i18next";

import {
  aierhubFetchEventSourceWithAuth
} from "./../../../../api/aierhubFetch";

import userApi from "./../../../../api/userApi";
import { IUserContexts, UserContexts } from "./../../../../contexts/user-contexts";

interface IProps {}

const RegenerateImgBtn: React.FC<IProps> = ({}: IProps) => {
  const { t } = useTranslation();
  const { message: messageApi } = App.useApp();
  const roleViewContexts: IRoleViewContexts = useContext<IRoleViewContexts>(RoleViewContexts);
  // 重新生成图片，正在生成中
  const [imageRegenerating, setImageRegenerating] = useState<boolean>(false);

  // 添加 AbortController 引用
  const abortControllerRef = useRef<AbortController | null>(null);

  const userContexts: IUserContexts =React.useContext<IUserContexts>(UserContexts);

  const regenerateImage = async () => {

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

    if (imageRegenerating) {
      messageApi.info(t("regenerateImg_button_generating"));
      return;
    }

    setImageRegenerating(true);

    // 如果有正在进行的请求，先取消
    if (abortControllerRef.current) {
      abortControllerRef.current.abort();
      abortControllerRef.current = null;
    }

      // 创建新的 AbortController
      abortControllerRef.current = new AbortController();
      const signal = abortControllerRef.current.signal;

      const figureExampleUrl = "";
      const projectId = roleViewContexts.projectId;
      const figureName = roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex].figureName;
      const figureDesc = roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex].figureDesc;
      const roleId = roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex].roleId;

      try {
        // 使用封装的函数替代原来的fetchEventSource，并添加signal参数
        await aierhubFetchEventSourceWithAuth(
          `/api/storyboard/role/regenerate?projectId=${projectId}&roleId=${roleId}&figureName=${figureName}&figureDesc=${figureDesc}&figureExampleUrl=${figureExampleUrl}`,
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
                    setImageRegenerating(false);
                  }else{
                    const data = JSON.parse(ev.data);

                    let newRoleList = roleViewContexts.roleList;
                    newRoleList[roleViewContexts.checkedRoleItemIndex].url =data.url;
                    newRoleList[roleViewContexts.checkedRoleItemIndex].figureName = data.figureName;
                    newRoleList[roleViewContexts.checkedRoleItemIndex].figureDesc = data.figureDesc;
                    roleViewContexts.setRoleList([...newRoleList]);
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
                setImageRegenerating(false);
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
        console.error("generate role error:", error);
        setImageRegenerating(false);
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
    <Button
      size="large"
      className={`px-8 my-6 ${
        imageRegenerating ? style.regeneratingBtn : ""
      } group`}
      onClick={regenerateImage}
      disabled={roleViewContexts.roleList.length === 0}
      ref={roleViewContexts.tourRef2}
    >
      {imageRegenerating ? (
        <LoadingOutlined color="#ffffff" />
      ) : (
        <div className="relative w-6 h-6 flex items-center justify-center">
          <img
            src={genImgIcon}
            alt={t("regenerateImg_button_alt")}
            className="absolute inset-0 m-auto transition-opacity duration-200 group-hover:opacity-0"
          />
          <img
            src={purpleGenImgIcon}
            alt={t("regenerateImg_button_alt")}
            className="absolute inset-0 m-auto opacity-0 transition-opacity duration-200 group-hover:opacity-100"
          />
        </div>
      )}

      <span>
        {imageRegenerating
          ? t("regenerateImg_button_generating")
          :(
            roleViewContexts.roleList[roleViewContexts.checkedRoleItemIndex]?.url
              ? t("regenerate_img_button_text")
              : t("generate_img_button_text")
          ) 
        }
      </span>
    </Button>
  );
};

export default RegenerateImgBtn;
