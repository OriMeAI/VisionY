import i18n from "i18next";
import { initReactI18next } from "react-i18next";

import enBase from "./locales/en/base.json";
import jaBase from "./locales/ja/base.json";
import zhCNBase from "./locales/zh-CN/base.json";
import zhTWBase from "./locales/zh-TW/base.json";

import enExtra from "./locales/en/extra.json";
import jaExtra from "./locales/ja/extra.json";
import zhCNExtra from "./locales/zh-CN/extra.json";
import zhTWExtra from "./locales/zh-TW/extra.json";

import enWorkspace from "./locales/en/workspace.json";
import jaWorkspace from "./locales/ja/workspace.json";
import zhCNWorkspace from "./locales/zh-CN/workspace.json";
import zhTWWorkspace from "./locales/zh-TW/workspace.json";

// 这里之所以不import { LANGUAGE } from '../libs/constants.ts'，是因为会有循环引用的问题
const language = localStorage.getItem("language");
i18n.use(initReactI18next).init({
  resources: {
    en: {
      common: {
        ...enWorkspace,
        ...enExtra,
        ...enBase, 
      },
    },
    ja: {
      common: {
        ...jaWorkspace,
        ...jaExtra,
        ...jaBase,
      },
    },
    "zh-CN": {
      common: {
        ...zhCNWorkspace,
        ...zhCNExtra,
        ...zhCNBase,
      },
    },
    "zh-TW": {
      common: {
        ...zhTWWorkspace,
        ...zhTWExtra,
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
