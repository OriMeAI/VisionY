import i18n from "i18next";
import { initReactI18next } from "react-i18next";

const enError = {
  "default_message": "Don't look around, go back",
  "back_to_home": "Back to Home"
};

const jaError = {
  "default_message": "見つかりません。戻ります。",
  "back_to_home": "ホームに戻る"
};

const zhCNError = {
  "default_message": "别找了，回去吧",
  "back_to_home": "回到首页"
};

const zhTWError = {
  "default_message": "別找了，回去吧",
  "back_to_home": "回到首頁"
};

// 这里之所以不import { LANGUAGE } from '../libs/constants.ts'，是因为会有循环引用的问题
const language = localStorage.getItem("language");
i18n.use(initReactI18next).init({
  resources: {
    en: {
      common: enError,
    },
    ja: {
      common: jaError,
    },
    "zh-CN": {
      common: zhCNError,
    },
    "zh-TW": {
      common: zhTWError,
    },
  },
  lng: language || "en",
  fallbackLng: "en",
  defaultNS: "common",
  debug: false,
  interpolation: {
    escapeValue: false,
  },
  ns: ["common"],
});

export default i18n;
