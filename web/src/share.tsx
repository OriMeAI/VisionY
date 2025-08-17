// src/share.tsx
import "@ant-design/v5-patch-for-react-19";
import { App, ConfigProvider } from "antd";
import enUS from "antd/locale/en_US";
import jaJP from "antd/locale/ja_JP";
import { default as zhCN } from "antd/locale/zh_CN";
import zhTW from "antd/locale/zh_TW";
import userApi from "./api/userApi";
import React, { useEffect } from "react";
import ReactDOM from "react-dom/client";
import { IntlProvider } from "react-intl";
import { BrowserRouter } from "react-router-dom";
import { setMessageApi } from "./api/messageApi";
import Share from "./components/ShareContent";
import { IUserContexts, UserContexts } from "./contexts/user-contexts";
import "./globals.css";
import "./i18n/project-i18n"; // 引入i18n配置
import { LANGUAGE } from "./libs/global-config";
import { UserInfoType } from "./libs/interfaces";
import userHelper from "./libs/user-helper";
import { ANT_DESIGN_TOKEN } from "./styles/ant-design-token";

import { GoogleOAuthProvider } from '@react-oauth/google';
import { GOOGLE_CLIENT_ID } from "./libs/global-config";
import { initAmplitude, trackPageView } from './libs/amplitude';

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

// AppContent 组件
const AppContent: React.FC = () => {
  const { message: messageApi } = App.useApp();

  // 初始化全局 message API
  useEffect(() => {
    setMessageApi(messageApi);
  }, [messageApi]);

  return (
    // <Suspense
    //   fallback={
    //     <div className="flex items-center justify-center w-screen h-screen">
    //       <Spin />
    //     </div>
    //   }
    // >
    //   <Share />
    // </Suspense>
    <Share />
  );
};

// 主应用组件
const ShareApp: React.FC = () => {
  const [userInfo, setUserInfo] = React.useState<UserInfoType>();
  const [isAuthenticated, setIsAuthenticated] = React.useState<boolean>(false);
  const [isShowLoginModal, setIsShowLoginModal] = React.useState(false);

  useEffect(() => {
    // 初始化 Amplitude
    initAmplitude();
    // 追踪页面浏览
    trackPageView('Share');
  }, []);

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
    }),
    [userInfo, isAuthenticated, isShowLoginModal]
  );

  const language = getBrowserLanguage();

  return (
    <IntlProvider
      locale={language}
      messages={messages[language as keyof typeof messages] as any}
    >
      <ConfigProvider locale={antdLocale[language] || enUS} theme={ANT_DESIGN_TOKEN}>
        <GoogleOAuthProvider clientId={GOOGLE_CLIENT_ID}>
          <App>
            <BrowserRouter>
              <UserContexts.Provider value={value as IUserContexts}>
                <AppContent />
              </UserContexts.Provider>
            </BrowserRouter>
          </App>
        </GoogleOAuthProvider>
      </ConfigProvider>
    </IntlProvider>
  );
};

ReactDOM.createRoot(document.getElementById("share_root") as HTMLElement).render(
  <ShareApp />
);