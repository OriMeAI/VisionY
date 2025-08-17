// src/project.tsx
import "@ant-design/v5-patch-for-react-19";
import { App, ConfigProvider, Spin } from "antd";
import enUS from "antd/locale/en_US";
import jaJP from "antd/locale/ja_JP";
import { default as zhCN } from "antd/locale/zh_CN";
import zhTW from "antd/locale/zh_TW";
import React, { lazy, Suspense, useContext, useEffect } from "react";
import ReactDOM from "react-dom/client";
import { IntlProvider } from "react-intl";
import {
  BrowserRouter,
  Route,
  Routes,
  useLocation,
  useParams,
} from "react-router-dom";
import projectApi from "./api/projectApi";
import userApi from "./api/userApi";
import {
  DetailContexts,
  IDetailContexts,
} from "./components/client/Common/DetailContainer/contexts/detail-contexts";
import CommonLoginModal from "./components/common/CommonLoginModal";
import { IUserContexts, UserContexts } from "./contexts/user-contexts";
import "./globals.css";
import "./i18n/project-i18n"; // 引入i18n配置
import authService from "./libs/auth-service";
import { ERROR_MSG_404, LANGUAGE } from "./libs/global-config";
import { ProjectItemObj, UserInfoType } from "./libs/interfaces";
import userHelper from "./libs/user-helper";
import { ANT_DESIGN_TOKEN } from "./styles/ant-design-token";
import SafeImage from "./components/common/SafeImage";
import { IModalContexts, ModalContexts } from "./contexts/modal-contexts";
import CreditsModal from "./components/common/CreditsModal";
import MembershipModal from "./components/common/MembershipModal";

import { GoogleOAuthProvider } from "@react-oauth/google";
// import { PayPalScriptProvider } from "@paypal/react-paypal-js";
import { GOOGLE_CLIENT_ID } from "./libs/global-config";

import { initAmplitude, trackPageView } from './libs/amplitude';

import { setMessageApi } from "./api/messageApi";
window.SafeImage = SafeImage;

const ScriptView = lazy(() => import("./components/Project/ScriptView"));
const TableView = lazy(() => import("./components/Project/TableView"));
const RoleView = lazy(() => import("./components/Project/RoleView"));
const BoardView = lazy(() => import("./components/Project/BoardView"));
const VisualMode = lazy(() => import("./components/Project/VisualMode"));

// 定义 SUPPORTED_LANGUAGES 的类型
const SUPPORTED_LANGUAGES = {
  'en-US': { value: 'en', label: 'English' },
  'zh-CN': { value: 'cn', label: '简体中文' },
  'zh-TW': { value: 'tw', label: '繁體中文' },
  'ja-JP': { value: 'ja', label: '日本語' },
} as const;

type LanguageCode = keyof typeof SUPPORTED_LANGUAGES;

// 获取用户的语言设置
const getBrowserLanguage = (): LanguageCode => {
  const savedLanguage = localStorage.getItem(LANGUAGE) as LanguageCode | null;
  if (savedLanguage && SUPPORTED_LANGUAGES[savedLanguage]) {
    return savedLanguage;
  }
  const browserLang = navigator.language || (navigator as any).userLanguage;
  if (SUPPORTED_LANGUAGES[browserLang as LanguageCode]) {
    return browserLang as LanguageCode;
  }
  return 'en-US';
};

// 根据语言设置加载对应的 Ant Design 语言包和翻译
const antdLocale = {
  'en-US': enUS,
  'zh-CN': zhCN,
  'zh-TW': zhTW,
  'ja-JP': jaJP,
};

const messages = {
  'en-US': enUS,
  'zh-CN': zhCN,
  'zh-TW': zhTW,
  'ja-JP': jaJP,
};

// 创建一个路由组件来处理具体的内容
const RouteContent: React.FC = () => {
  const { id, projectId } = useParams<{ id: string; projectId: string }>();
  const location = useLocation();
  const [projectItemObj, setProjectItemObj] = React.useState<ProjectItemObj>();
  const [showRightPanel, setShowRightPanel] = React.useState<boolean>(false);

  useEffect(() => {
    if (!id && !projectId) return;

    (async () => {
      const paramId = id || projectId;
      const data = await projectApi.getProjectById(paramId);
      if (data.success && data.result?.code === 0) {
        setProjectItemObj(data.result.data);
        // 如果是项目页，并且没有角色，跳转到角色页，否则跳转到分镜表页面
        if (
          data.result.data &&
          location.pathname.includes("/project") &&
          !location.pathname.includes("/scriptview") &&
          !location.pathname.includes("/roleview") &&
          !location.pathname.includes("/tableview") &&
          !location.pathname.includes("/boardview") &&
          !location.pathname.includes("/visualview")
        ) {
          if (data.result.data.hasShot) {
            window.location.href = `/project/${data.result.data.id}/tableview`;
          } else {
            window.location.href = `/project/${data.result.data.id}/roleview`;
          }
        }
      } else if (data.result?.code === 403) {
        localStorage.setItem(ERROR_MSG_404, data.result.msg);
        window.location.href = "/workspace";
      }
    })();
  }, [id, projectId]);

  const detailValue = React.useMemo(
    () => ({
      projectItemObj,
      setProjectItemObj,
      showRightPanel,
      setShowRightPanel,
    }),
    [projectItemObj, showRightPanel]
  );

  // 根据路径渲染对应组件
  const renderComponent = () => {
    // 检查是否是有效的项目路由
    const projectRoutePattern =
      /^\/project\/[a-zA-Z0-9]+(\/(scriptview|roleview|tableview|boardview|visualview))?$/;
    const isValidRoute = projectRoutePattern.test(location.pathname);

    if (!isValidRoute) {
      window.location.href = "/workspace";
      return null;
    }

    if (location.pathname.includes("/project") && !projectItemObj) {
      return (
        <div className="flex items-center justify-center w-screen h-screen">
          <Spin />
        </div>
      );
    }
    if (location.pathname.includes("/scriptview")) {
      return (
        <Suspense
          fallback={
            <div className="flex items-center justify-center w-screen h-screen">
              <Spin />
            </div>
          }
        >
          <ScriptView />
        </Suspense>
      );
    }
    if (location.pathname.includes("/roleview")) {
      return (
        <Suspense
          fallback={
            <div className="flex items-center justify-center w-screen h-screen">
              <Spin />
            </div>
          }
        >
          <RoleView />
        </Suspense>
      );
    }
    if (location.pathname.includes("/tableview")) {
      return (
        <Suspense
          fallback={
            <div className="flex items-center justify-center w-screen h-screen">
              <Spin />
            </div>
          }
        >
          <TableView />
        </Suspense>
      );
    }
    if (location.pathname.includes("/boardview")) {
      return (
        <Suspense
          fallback={
            <div className="flex items-center justify-center w-screen h-screen">
              <Spin />
            </div>
          }
        >
          <BoardView />
        </Suspense>
      );
    }
    if (location.pathname.includes("/visualview")) {
      return (
        <Suspense
          fallback={
            <div className="flex items-center justify-center w-screen h-screen">
              <Spin />
            </div>
          }
        >
          <VisualMode />
        </Suspense>
      );
    }
    return null;
  };

  return (
    <DetailContexts.Provider value={detailValue as IDetailContexts}>
      <CommonLoginModal />
      {renderComponent()}
    </DetailContexts.Provider>
  );
};

// AppContent 组件
const AppContent: React.FC = () => {
  const { message: messageApi } = App.useApp();

  // 初始化全局 message API
  useEffect(() => {
    setMessageApi(messageApi);
  }, [messageApi]);

  const userContexts = useContext<IUserContexts>(UserContexts);

  useEffect(() => {
    authService.registerLogoutCallback(() => {
      userContexts.setIsAuthenticated(false);
      userContexts.setUserInfo(undefined);
      window.location.href = "/workspace";
    });
  }, [userContexts]);

  return (
    <Routes>
      <Route path="project/:projectId" element={<RouteContent />} />
      <Route path="project/:projectId/scriptview" element={<RouteContent />} />
      <Route path="project/:projectId/roleview" element={<RouteContent />} />
      <Route path="project/:projectId/tableview" element={<RouteContent />} />
      <Route path="project/:projectId/boardview" element={<RouteContent />} />
      <Route path="project/:projectId/visualview" element={<RouteContent />} />
      <Route path="*" element={<RouteContent />} />
    </Routes>
  );
};

// 添加环境检测函数
// const getPayPalClientId = () => {
//   const hostname = window.location.hostname;
  
//   // 如果是localhost或开发环境，使用sandbox
//   if (hostname === 'localhost' || hostname === '127.0.0.1' || hostname.includes('localhost')) {
//     return PAYPAL_CLIENT_ID_SANDBOX;
//   }
  
//   // 如果是visiony.ai正式域名，使用正式环境
//   if (hostname === 'visiony.ai' || hostname.includes('visiony.ai')) {
//     return PAYPAL_CLIENT_ID;
//   }
  
//   // 默认使用sandbox（安全起见）
//   return PAYPAL_CLIENT_ID_SANDBOX;
// };

// 主应用组件
const MainApp: React.FC = () => {
  // const paypalClientId = getPayPalClientId();

  // 在应用启动时初始化 Amplitude
  useEffect(() => {
    initAmplitude();
    // 追踪页面浏览
    trackPageView('Project');
  }, []);

  const [userInfo, setUserInfo] = React.useState<UserInfoType>();
  const [isAuthenticated, setIsAuthenticated] = React.useState<boolean>(false);
  const [isShowLoginModal, setIsShowLoginModal] = React.useState(false);

    //是否显示购买 google login 的 loading
  const [isShowLoginModelLoading, setIsShowLoginModelLoading] = React.useState(false);

  //是否显示购买 credits 的 modal
  const [isShowCreditsModal, setIsShowCreditsModal] = React.useState(false);
  //是否显示购买 credits 的 loading
  const [isShowCreditsLoading, setIsShowCreditsLoading] = React.useState(false);

  //是否显示购买 membership 的 modal
  const [isShowMembershipModal, setIsShowMembershipModal] = React.useState(false);
  //是否显示购买 membership 的 loading
  const [isShowMembershipLoading, setIsShowMembershipLoading] = React.useState(false);

  // 获取用户信息
  useEffect(() => {
    (async () => {
      const authInfo = userHelper.getLocalUserInfo();
      setIsAuthenticated(authInfo?.state.isAuthenticated);
      if (authInfo?.state.isAuthenticated) {
        const data = await userApi.getUserInfo();
        if (!data.success) return;
        setUserInfo(data.result?.data);
      }
    })();
  }, []);

  const value = React.useMemo(
    () => ({
      userInfo,
      setUserInfo,
      isAuthenticated,
      setIsAuthenticated,

      isShowLoginModal,
      setIsShowLoginModal,
      isShowLoginModelLoading,
      setIsShowLoginModelLoading,
    }),
    [userInfo, isAuthenticated, isShowLoginModal]
  );
  const payValue = React.useMemo(
    () => ({
      isShowCreditsModal,
      setIsShowCreditsModal,
      isShowCreditsLoading,
      setIsShowCreditsLoading,

      isShowMembershipModal,
      setIsShowMembershipModal,
      isShowMembershipLoading,
      setIsShowMembershipLoading,
    }),
    [isShowCreditsModal, isShowMembershipModal]
  );

  const language = getBrowserLanguage();

  return (
    <IntlProvider
      locale={language}
      messages={messages[language as keyof typeof messages] as any}
    >
      <ConfigProvider locale={antdLocale[language] || enUS} theme={ANT_DESIGN_TOKEN}>
        <GoogleOAuthProvider clientId={GOOGLE_CLIENT_ID}>
          {/* <PayPalScriptProvider options={{ clientId: paypalClientId }}> */}
            <App>
              <BrowserRouter>
                <UserContexts.Provider value={value as IUserContexts}>
                  <ModalContexts.Provider value={payValue as IModalContexts}>
                    {/* 全局 Loading Spin */}
                    {(isShowCreditsLoading || isShowMembershipLoading) && (
                      <div className="fixed inset-0 bg-white bg-opacity-50 flex items-center justify-center z-[60]">
                        <Spin />
                      </div>
                    )}
                    <AppContent />
                    <CreditsModal />
                    <MembershipModal />
                  </ModalContexts.Provider>
                </UserContexts.Provider>
              </BrowserRouter>
            </App>
          {/* </PayPalScriptProvider> */}
        </GoogleOAuthProvider>
      </ConfigProvider>
    </IntlProvider>
  );
};

ReactDOM.createRoot(document.getElementById("project_root") as HTMLElement).render(
  <MainApp />
);