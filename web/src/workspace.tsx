// src/workspace.tsx
import "@ant-design/v5-patch-for-react-19";
import { ConfigProvider, App, Spin} from "antd";
import enUS from "antd/locale/en_US";
import jaJP from "antd/locale/ja_JP";
import { default as zhCN } from "antd/locale/zh_CN";
import zhTW from "antd/locale/zh_TW";
import React, { useEffect, Suspense } from "react";
import ReactDOM from "react-dom/client";
import { IntlProvider } from "react-intl";
import userApi from "./api/userApi";
import { setMessageApi } from "./api/messageApi";
import CommonLoginModal from "./components/common/CommonLoginModal";
import UpgradeModal from "./components/common/UpgradeModal";
import CreditsModal from "./components/common/CreditsModal";
import MembershipModal from "./components/common/MembershipModal";
import {
  DashboardContexts,
  IDashboardContexts,
} from "./contexts/dashboard-contexts";
import { IModalContexts, ModalContexts } from "./contexts/modal-contexts";
import { IUserContexts, UserContexts } from "./contexts/user-contexts";
import "./globals.css";
import "./i18n/workspace-i18n"; // 引入i18n配置
import { UserInfoType } from "./libs/interfaces";
import userHelper from "./libs/user-helper";
import { ANT_DESIGN_TOKEN } from "./styles/ant-design-token";
import { LANGUAGE } from "./libs/global-config";
import { BrowserRouter } from "react-router-dom";

import { GoogleOAuthProvider } from '@react-oauth/google';
// import { PayPalScriptProvider } from "@paypal/react-paypal-js";
import { GOOGLE_CLIENT_ID } from "./libs/global-config";

import { initAmplitude, trackPageView } from './libs/amplitude';

import Workspace from "./components/Workspace";

import SafeImage from "./components/common/SafeImage";
window.SafeImage = SafeImage;

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

// 创建一个内部组件来使用 App.useApp
const AppContent: React.FC = () => {
  const { message: messageApi } = App.useApp();

  // 初始化全局 message API
  useEffect(() => {
    setMessageApi(messageApi);
  }, [messageApi]);

  const [userInfo, setUserInfo] = React.useState<UserInfoType>();
  const [isAuthenticated, setIsAuthenticated] = React.useState<boolean>(false);

  const [isShowLoginModal, setIsShowLoginModal] = React.useState(false);
  //是否显示购买 google login 的 loading
  const [isShowLoginModelLoading, setIsShowLoginModelLoading] = React.useState(false);

  const [isShowUpgradeModal, setIsShowUpgradeModal] = React.useState(false);

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

  const userValue = React.useMemo(
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

  const dashboardValue = React.useMemo(
    () => ({
      isShowUpgradeModal,
      setIsShowUpgradeModal,
    }),
    [isShowUpgradeModal]
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

  return (
    <UserContexts.Provider value={userValue as IUserContexts}>
      <ModalContexts.Provider value={payValue as IModalContexts}>
        <DashboardContexts.Provider
          value={dashboardValue as IDashboardContexts}
        >
          {/* 全局 Loading Spin */}
          {(isShowLoginModelLoading || isShowCreditsLoading || isShowMembershipLoading) && (
            <div className="fixed inset-0 bg-white bg-opacity-50 flex items-center justify-center z-[60]">
              <Spin />
            </div>
          )}

          {/* <Suspense
            fallback={
              <div className="flex items-center justify-center w-screen h-screen">
                <Spin />
              </div>
            }
          >
            <Workspace />
          </Suspense> */}
          <Workspace />
          <UpgradeModal />
          <CommonLoginModal />
          <CreditsModal />
          <MembershipModal />
        </DashboardContexts.Provider>
      </ModalContexts.Provider>
    </UserContexts.Provider>
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

const MainApp: React.FC = () => {

  // 在应用启动时初始化 Amplitude
  useEffect(() => {
    initAmplitude();
    // 追踪页面浏览
    trackPageView('Workspace');
  }, []);

  const language = getBrowserLanguage();
  // const paypalClientId = getPayPalClientId();

  return (
    <IntlProvider
      locale={language}
      messages={messages[language as keyof typeof messages] as any}
    >
      <ConfigProvider theme={ANT_DESIGN_TOKEN} locale={antdLocale[language] || enUS}>
        <GoogleOAuthProvider clientId={GOOGLE_CLIENT_ID}>
          {/* <PayPalScriptProvider options={{ clientId: paypalClientId }}> */}
            <App>
              <BrowserRouter>
                <AppContent />
              </BrowserRouter>
            </App>
          {/* </PayPalScriptProvider> */}
        </GoogleOAuthProvider>
      </ConfigProvider>
    </IntlProvider>
  );
};

ReactDOM.createRoot(document.getElementById("workspace_root")!).render(
  <MainApp />
);