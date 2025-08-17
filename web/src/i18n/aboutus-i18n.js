import i18n from "i18next";
import { initReactI18next } from "react-i18next";

import enBase from "./locales/en/base.json";
import jaBase from "./locales/ja/base.json";
import zhCNBase from "./locales/zh-CN/base.json";
import zhTWBase from "./locales/zh-TW/base.json";

import enAboutUs from "./locales/en/aboutus.json";
import jaAboutUs from "./locales/ja/aboutus.json";
import zhCNAboutUs from "./locales/zh-CN/aboutus.json";
import zhTWAboutUs from "./locales/zh-TW/aboutus.json";

// 这里之所以不import { LANGUAGE } from '../libs/constants.ts'，是因为会有循环引用的问题
const language = localStorage.getItem("language");
i18n.use(initReactI18next).init({
  resources: {
    en: {
      common: {
        ...enAboutUs,        
        ...enBase, 
      },
    },
    ja: {
      common: {
        ...jaAboutUs,
        ...jaBase, 
      },
    },
    "zh-CN": {
      common: {
        ...zhCNAboutUs,
        ...zhCNBase, 
      },
    },
    "zh-TW": {
      common: {
        ...zhTWAboutUs,
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
