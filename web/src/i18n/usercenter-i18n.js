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

import enUserCenter from "./locales/en/usercenter.json";
import jaUserCenter from "./locales/ja/usercenter.json";
import zhCNUserCenter from "./locales/zh-CN/usercenter.json";
import zhTWUserCenter from "./locales/zh-TW/usercenter.json";

// 这里之所以不import { LANGUAGE } from '../libs/constants.ts'，是因为会有循环引用的问题
const language = localStorage.getItem("language");
i18n.use(initReactI18next).init({
  resources: {
    en: {
      common: {
        ...enUserCenter,
        ...enExtra,
        ...enBase,
      },
    },
    ja: {
      common: {
        ...jaUserCenter,
        ...jaExtra,
        ...jaBase,
      },
    },
    "zh-CN": {
      common: {
        ...zhCNUserCenter,
        ...zhCNExtra,
        ...zhCNBase,
      },
    },
    "zh-TW": {
      common: {
        ...zhTWUserCenter,
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
  ns: ["common"],
});

export default i18n;
