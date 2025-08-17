// src/usercenter.tsx
import "@ant-design/v5-patch-for-react-19";
import { ConfigProvider, App ,Spin} from "antd";
import enUS from "antd/locale/en_US";
import jaJP from "antd/locale/ja_JP";
import { default as zhCN } from "antd/locale/zh_CN";
import zhTW from "antd/locale/zh_TW";
import dayjs from "dayjs";
import "dayjs/locale/en";
import "dayjs/locale/zh-cn";
import React, { useEffect } from "react";
import ReactDOM from "react-dom/client";
import { IntlProvider } from "react-intl";
import { setMessageApi } from "./api/messageApi";
import { IUserContexts, UserContexts } from "./contexts/user-contexts";
import "./globals.css";
import "./i18n/usercenter-i18n"; // 引入i18n配置
import { LANGUAGE } from "./libs/global-config";
import { UserInfoType } from "./libs/interfaces";
import userHelper from "./libs/user-helper";
import { ANT_DESIGN_TOKEN } from "./styles/ant-design-token";
import CommonLoginModal from "./components/common/CommonLoginModal";
import { BrowserRouter } from "react-router-dom";

import { GoogleOAuthProvider } from '@react-oauth/google';
// import { PayPalScriptProvider } from "@paypal/react-paypal-js";
import { GOOGLE_CLIENT_ID } from "./libs/global-config";

import { initAmplitude, trackPageView } from './libs/amplitude';

import Login from "./components/Login";

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

// 设置 dayjs 的语言
const dayjsLocale = {
  'en-US': 'en',
  'zh-CN': 'zh-cn',
  'zh-TW': 'zh-cn', // zh-TW 使用 zh-cn，因为 dayjs 未提供单独的 zh-tw
  'ja-JP': 'ja',
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
  const { message: messageApi } = App.useApp();

  useEffect(() => {
    // 初始化 Amplitude
    initAmplitude();
    // 追踪页面浏览
    trackPageView('Login');
  }, []);

  // 初始化全局 message API
  useEffect(() => {
    setMessageApi(messageApi);
  }, [messageApi]);

  const language = getBrowserLanguage();
  // const paypalClientId = getPayPalClientId();
  // 设置 dayjs 的语言
  dayjs.locale(dayjsLocale[language]);

  const [userInfo, setUserInfo] = React.useState<UserInfoType>();
  const [isAuthenticated, setIsAuthenticated] = React.useState<boolean>(false);

  const [isShowLoginModal, setIsShowLoginModal] = React.useState(false);
  //是否显示购买 google login 的 loading
  const [isShowLoginModelLoading, setIsShowLoginModelLoading] = React.useState(false);

  // 获取用户信息
  React.useEffect(() => {
    const authInfo = userHelper.getLocalUserInfo();
    setIsAuthenticated(authInfo?.state.isAuthenticated);
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
                <UserContexts.Provider value={userValue as IUserContexts}>
                    {/* 全局 Loading Spin */}
                    {(isShowLoginModelLoading) && (
                      <div className="fixed inset-0 bg-white bg-opacity-50 flex items-center justify-center z-[60]">
                        <Spin />
                      </div>
                    )}
                    <Login />
                    <CommonLoginModal />
                </UserContexts.Provider>
              </BrowserRouter>
            </App>
          {/* </PayPalScriptProvider> */}
        </GoogleOAuthProvider>
      </ConfigProvider>
    </IntlProvider>
  );
};

ReactDOM.createRoot(
  document.getElementById("login_root") as HTMLElement
).render(<MainApp />);