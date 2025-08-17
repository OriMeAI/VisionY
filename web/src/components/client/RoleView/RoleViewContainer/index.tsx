/**
 * 角色页面容器
 */

import { Spin, App } from "antd";
import loadingIcon from "./../../../../../assets/images/layout/loading_icon.svg";
import { aierhubFetchEventSourceWithAuth } from "./../../../../api/aierhubFetch";

import React, { useContext, useEffect, useRef } from "react";
import { createPortal } from "react-dom";
import { useTranslation } from "react-i18next";
import {
  DetailContexts,
  IDetailContexts,
} from "../../Common/DetailContainer/contexts/detail-contexts";
import ModalBase from "../../Common/ModalBase";
import {
  IRoleViewContexts,
  RoleViewContexts,
} from "../../../../contexts/role-view-contexts";
import RoleItemAdd from "../RoleItemAdd";
import roleViewStore from "../roleViewStore";
import tourHelper from "./../../../../libs/tour-helper";
import style from "./style.module.css";

import RoleItemEdit from "../RoleItemEdit";
import RoleList from "../RoleList";

import userApi from "./../../../../api/userApi";
import { IUserContexts, UserContexts } from "./../../../../contexts/user-contexts";


interface IProps {}

const RoleViewContainer: React.FC<IProps> = ({}: IProps) => {
  const { t } = useTranslation();
  const { message: messageApi } = App.useApp();
  const roleViewContexts: IRoleViewContexts =
    useContext<IRoleViewContexts>(RoleViewContexts);
  const detailContexts: IDetailContexts =
    useContext<IDetailContexts>(DetailContexts);
  const [loading, setLoading] = React.useState<boolean>(true);

  // 添加 AbortController 引用
  const abortControllerRef = useRef<AbortController | null>(null);
  const [roleGenerateLoadingText, setRoleGenerateLoadingText] = React.useState<string>(t("roleView_loading_title"));
  const userContexts: IUserContexts =React.useContext<IUserContexts>(UserContexts);
  

  // 组件卸载时取消所有进行中的请求
  useEffect(() => {
    return () => {
      if (abortControllerRef.current) {
        abortControllerRef.current.abort();
        abortControllerRef.current = null;
      }
    };
  }, []);

  // 通过项目id获取角色列表
  useEffect(() => {
    (async () => {

      if (userContexts.isAuthenticated) {
        const data = await userApi.getUserInfo();
        if (!data.success) return;
        userContexts.setUserInfo(data.result.data);
        if(data.result?.data?.credits < 1){
          messageApi.error(t("common_error_noCredits"));
          // return;
        }
      }else{
        messageApi.error(t("common_error_noLogin"));
        return;
      }

      if (!detailContexts.projectItemObj) {
        return;
      }

      // 如果有正在进行的请求，先取消
      if (abortControllerRef.current) {
        abortControllerRef.current.abort();
      }

      if (detailContexts.projectItemObj.hasRole) {
        await roleViewStore.getRoleList(roleViewContexts, () => {
          setLoading(false);
        });
      } else {
        // 创建新的 AbortController
        abortControllerRef.current = new AbortController();
        const signal = abortControllerRef.current.signal;

        try {
          // 使用封装的函数并添加signal参数
          await aierhubFetchEventSourceWithAuth(
            `/api/storyboard/create/role?projectId=${roleViewContexts.projectId}`,
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
                    }
                    else if (ev.data === "Complete") {
                      (async () => {
                        await roleViewStore.getRoleList(roleViewContexts, () => {
                          setLoading(false);
                          const roleTourShown = tourHelper.getLocalRoleTourShown();
                          if (!roleTourShown) {
                            roleViewContexts.setIsTourOpen(true);
                            tourHelper.setLocalRoleTourShown("false");
                          }
                        });
                      })();
                      messageApi.success(t("roles_created_success"));
                      return;
                    }
                   else{
                      const data = JSON.parse(ev.data);
                      roleViewContexts.setRoleList((prev) => {
                        return [
                          ...prev,
                          {
                            figureName: data.figureName,
                            url: data.url,
                            roleId: data.id,
                            figureDesc: data.figureDesc,
                          },
                        ];
                      });
                    }

                    break;
                  case "progress":
                    setRoleGenerateLoadingText(ev.data);
                    break;
                  case "warning":
                    messageApi.warning(ev.data);
                    break;
                  case "error":
                    messageApi.error(ev.data);
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
          console.error("角色生成出错:", error);
          setLoading(false);
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
      }
    })();

    // 组件卸载或依赖变化时清理
    return () => {
      if (abortControllerRef.current) {
        abortControllerRef.current.abort();
        abortControllerRef.current = null;
      }
    };
  }, [detailContexts.projectItemObj]);
  return (
    <Spin spinning={detailContexts.projectItemObj?.hasRole && loading}>
      <div
        className="flex py-6 px-6 space-x-6 w-[1200px] h-[948px] mx-auto"
      >
        <div className="w-[400px] p-6 rounded-lg flex-shrink-0 bg-white">
          <div className="w-full flex justify-between items-center mb-6">
            <h2 className="text-lg font-semibold">{t("roleView_title")}</h2>
            <RoleItemAdd />
          </div>
          {/* <Suspense
            fallback={
              <div className="flex items-center justify-center h-full">
                <Spin />
              </div>
            }
          >
            <RoleList loading={loading} roleList={roleViewContexts.roleList} />
          </Suspense> */}
          <RoleList loading={loading} roleList={roleViewContexts.roleList} />
        </div>
        {/* <Suspense
          fallback={
            <div className="flex items-center justify-center h-full">
              <Spin />
            </div>
          }
        >
          <RoleItemEdit loading={loading} />
        </Suspense> */}
        <RoleItemEdit loading={loading} />
        {!detailContexts.projectItemObj?.hasRole ? (
          <>
            {createPortal(
              <ModalBase
                // wrapperClassName={style.loadingModal}
                open={loading && !detailContexts.projectItemObj?.hasRole}
                width={380}
                height={undefined}
                showFooter={false}
                footer={null}
                closable={false}
              >
                {/* <div className="transform -translate-x-1/2 -translate-y-1/2"> */}
                <div className="animate-enter max-w-md w-full bg-white shadow-2xl rounded-lg pointer-events-auto flex-col ring-1 ring-black ring-opacity-5">
                  <div className="flex-1 p-4">
                    <div className="flex items-start">
                      <div className="border p-2 rounded-lg">
                        <img
                          className="animate-spin"
                          src={loadingIcon}
                          alt="loading"
                        />
                      </div>
                      <div className="ml-4 flex-1">
                        <p className="text-sm font-medium text-gray-900">
                          {roleGenerateLoadingText} <span className={style.dotsAnimation}></span>
                        </p>
                        <p className="mt-1 text-sm text-gray-500">
                          {t("storyboard_table_loading_message")}
                          <br />
                          {t("storyboard_table_loading_warning")}
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
                {/* </div> */}
              </ModalBase>,
              document.body
            )}
          </>
        ) : null}
      </div>
      {/* </div> */}
      {/* </div> */}
    </Spin>
  );
};

export default RoleViewContainer;
