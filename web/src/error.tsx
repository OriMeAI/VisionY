// src/error.tsx
import "@ant-design/v5-patch-for-react-19";
import { App, ConfigProvider } from "antd";
import enUS from "antd/locale/en_US";
import jaJP from "antd/locale/ja_JP";
import { default as zhCN } from "antd/locale/zh_CN";
import zhTW from "antd/locale/zh_TW";
import React, { useEffect } from "react";
import ReactDOM from "react-dom/client";
import { IntlProvider } from "react-intl";
import { setMessageApi } from "./api/messageApi";
import "./globals.css";
import "./i18n/error-i18n"; // 引入i18n配置
import { LANGUAGE } from "./libs/global-config";
import { ANT_DESIGN_TOKEN } from "./styles/ant-design-token";
import NotFound from "./components/NotFound";
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
    //   <NotFound />
    // </Suspense>
    <NotFound />
  );
};

const MainApp: React.FC = () => {
  const language = getBrowserLanguage();

  useEffect(() => {
    // 初始化 Amplitude
    initAmplitude();
    // 追踪页面浏览
    trackPageView('Error');
  }, []);

  return (
    <IntlProvider
      locale={language}
      messages={messages[language as keyof typeof messages] as any}
    >
      <ConfigProvider locale={antdLocale[language] || enUS} theme={ANT_DESIGN_TOKEN}>
        <App>
          <AppContent />
        </App>
      </ConfigProvider>
    </IntlProvider>
  );
};

ReactDOM.createRoot(
  document.getElementById("error_root") as HTMLElement
).render(<MainApp />);