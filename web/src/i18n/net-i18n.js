import i18next from "i18next";

const enError = {
    "server_inner_error": "Server inner error",
    "unauthorized_error": "Unauthorized",
    "forbidden_error": "Forbidden",
    "not_found_error": "Not found",
    "method_not_allowed_error": "Method not allowed",
}

const jaError = {
    "server_inner_error": "サーバー内部エラー",
    "unauthorized_error": "認証されていません",
    "forbidden_error": "アクセスが禁止されています",
    "not_found_error": "見つかりません",
    "method_not_allowed_error": "許可されていないメソッド",
  }

  const zhCNError = {
    "server_inner_error": "服务器内部错误",
    "unauthorized_error": "登录后才可访问",
    "forbidden_error": "禁止访问",
    "not_found_error": "未找到",
    "method_not_allowed_error": "方法不被允许"
  }

  const zhTWError = {
    "server_inner_error": "伺服器內部錯誤",
    "unauthorized_error": "未授權",
    "forbidden_error": "禁止訪問",
    "not_found_error": "未找到",
    "method_not_allowed_error": "方法不被允許"
  }

// 创建独立实例
const netErrorLanguage = i18next.createInstance();

netErrorLanguage.init({
  resources: {
    en: {
      net: enError,
    },
    ja: {
      net: jaError,
    },
    "zh-CN": {
      net: zhCNError,
    },
    "zh-TW": {
      net: zhTWError,
    },
  },
  lng: localStorage.getItem("language") || "en",
  fallbackLng: "en",
  defaultNS: "net",
  debug: false,
  interpolation: {
    escapeValue: false,
  },
  ns: ["net"],
});

export default netErrorLanguage;
