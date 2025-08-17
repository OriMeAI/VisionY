import i18n from "i18next";
import { initReactI18next } from "react-i18next";

import enBase from "./locales/en/base.json";
import jaBase from "./locales/ja/base.json";
import zhCNBase from "./locales/zh-CN/base.json";
import zhTWBase from "./locales/zh-TW/base.json";

import enUserAgreement from "./locales/en/termsofuse.json";
import jaUserAgreement from "./locales/ja/termsofuse.json";
import zhCNUserAgreement from "./locales/zh-CN/termsofuse.json";
import zhTWUserAgreement from "./locales/zh-TW/termsofuse.json";

// 这里之所以不import { LANGUAGE } from '../libs/constants.ts'，是因为会有循环引用的问题
const language = localStorage.getItem("language");
i18n.use(initReactI18next).init({
  resources: {
    en: {
      common: {
        ...enUserAgreement,
        ...enBase,
      },
    },
    ja: {
      common: {
        ...jaUserAgreement,
        ...jaBase,
      },
    },
    "zh-CN": {
      common: {
        ...zhCNUserAgreement,
        ...zhCNBase,
      },
    },
    "zh-TW": {
      common: {
        ...zhTWUserAgreement,
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
