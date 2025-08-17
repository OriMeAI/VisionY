import i18n from "i18next";
import { initReactI18next } from "react-i18next";

import enBase from "./locales/en/base.json";
import jaBase from "./locales/ja/base.json";
import zhCNBase from "./locales/zh-CN/base.json";
import zhTWBase from "./locales/zh-TW/base.json";

import enIndex from "./locales/en/index.json";
import jaIndex from "./locales/ja/index.json";
import zhCNIndex from "./locales/zh-CN/index.json";
import zhTWIndex from "./locales/zh-TW/index.json";

// 这里之所以不import { LANGUAGE } from '../libs/constants.ts'，是因为会有循环引用的问题
const language = localStorage.getItem("language");
i18n.use(initReactI18next).init({
  resources: {
    en: {
      common: { 
        ...enIndex,
        ...enBase,
      },
    },
    ja: {
      common: { 
        ...jaIndex,
        ...jaBase,
      },
    },
    "zh-CN": {
      common: { 
        ...zhCNIndex,
        ...zhCNBase,
      },
    },
    "zh-TW": {
      common: { 
        ...zhTWIndex,
        ...zhTWBase, 
      },
    },
  },
  lng: language || "en",
  fallbackLng: "en",
  defaultNS: "common",
  debug: false,
  interpolation: {
    escapeValue: false,
  },
  ns: [
    "common",
  ],
});

export default i18n;
