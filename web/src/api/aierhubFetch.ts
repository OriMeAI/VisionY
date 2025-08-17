import { fetchEventSource } from "@microsoft/fetch-event-source";
import userHelper from "../libs/user-helper";
import authService from "../libs/auth-service";
// @ts-ignore
import netErrorLanguage from "../i18n/net-i18n";
import { getMessageApi } from './messageApi';
import { trackEvent, trackPageView, setUserProperties } from '../libs/amplitude';

//API 地址
export const host = process.env.API_URL;

const getTranslation = (key: string) => {
  const language = localStorage.getItem("language") || "en-US";
  netErrorLanguage.changeLanguage(language);
  return netErrorLanguage.t(key);
};

export type Result = {
  success: boolean;
  result: any;
};

interface EventSourceOptions {
  method?: string;
  headers?: Record<string, string>;
  body?: string;
  onmessage?: (ev: { event:string, data: string }) => void;
  onerror?: (err: Error) => void;
  onopen?: (response: Response) => Promise<void>;
  onclose?: () => void;
  signal?: AbortSignal;
}

/**
 * 封装的 fetchEventSource 方法，自动添加用户 token
 * @param url 请求地址
 * @param options 请求选项
 */
export const aierhubFetchEventSourceWithAuth = async (
  apiPath: string,
  options: EventSourceOptions
) => {

  trackEvent('api_fetch', {
    api_path: apiPath,
    method: options.method,
  });

  const messageApi = getMessageApi();
  // 获取用户信息和 token
  const authInfo = userHelper.getLocalUserInfo();

  // 修正 token 格式，移除多余的换行符
  const token = authInfo?.state.token ? authInfo.state.token.trim() : null;

  // 获取当前语言设置
  const language = localStorage.getItem("language") || "en";

  // 合并请求头，添加授权信息和语言设置
  const headers = {
    "Content-Type": "application/json",
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
    "Accept-Language": language,
    ...options.headers,
  };

  // 调用原始 fetchEventSource 方法
  return fetchEventSource(`${host}${apiPath}`, {
    method: options.method,
    headers,
    body: options.body,
    signal: options.signal,
    openWhenHidden: true, // 页面隐藏时保持连接
    onclose: options.onclose,
    // 自定义处理 onmessage，只传递 message 类型的事件
    onmessage: (event) => {
      if(event.event === "heartbeat"){
        console.log("SSE heartbeat");
        return
      }        
      if (options.onmessage) {
        options.onmessage(event);
      }
    },
    // 添加默认错误处理
    onerror: (err) => {
      if (options.onerror) options.onerror(err);
    },
    // 确保 onopen 返回 Promise<void>
    onopen: options.onopen
      ? options.onopen
      : async (response) => {
          if (response.ok) return Promise.resolve();
        },
  });
};

export async function aierhubGet(apiPath: string): 
Promise<Result> {

  trackEvent('api_get', {
    api_path: apiPath,
  });

  const messageApi = getMessageApi();
  const authInfo = userHelper.getLocalUserInfo();
  const authorization = `
Bearer ${authInfo?.state.token}`;
  const language = localStorage.getItem("language") || "en";
  let headersObj: any = {};
  if (authInfo?.state.token) {
    headersObj = {
      ...headersObj,
      authorization,
    };
  }
  if (language) {
    headersObj = {
      ...headersObj,
      "Accept-Language": language,
    };
  }
  try {
    const res = await fetch(`${host}${apiPath}`, {
      method: "GET",
      headers: headersObj,
    });
    return parseResult(res);
  } catch (error) {
    console.error("aierhubGet", error);
    return {
      success: false,
      result: null,
    };
  }
}

export async function aierhubPost(
  apiPath: string,
  headers: object = {},
  body: object = {}
): Promise<Result> {
  trackEvent('api_post', {
    api_path: apiPath,
  });

  const messageApi = getMessageApi();
  const authInfo = userHelper.getLocalUserInfo();
  const authorization = `
Bearer ${authInfo?.state.token}`;

  const language = localStorage.getItem("language") || "en";
  let headersObj: any = {
    ...headers,
    Accept: "application/json",
    "Content-Type": "application/json",
  };
  if (authInfo?.state.token) {
    headersObj = {
      ...headersObj,
      authorization,
    };
  }
  if (language) {
    headersObj = {
      ...headersObj,
      "Accept-Language": language,
    };
  }
  try {
    const res = await fetch(`${host}${apiPath}`, {
      method: "POST",
      headers: headersObj,
      body: JSON.stringify(body),
    });
    return parseResult(res);
  } catch (error) {
    console.error("aierhubPost", error);
    return {
      success: false,
      result: null,
    };
  }
}

export async function aierhubFetchFile(
  apiPath: string,
  headers: object = {},
  body: object = {}
): Promise<Result> {
  trackEvent('api_fetch_file', {
    api_path: apiPath,
    method: 'POST',
  });

  const messageApi = getMessageApi();
  const authInfo = userHelper.getLocalUserInfo();
  const authorization = `
Bearer ${authInfo?.state.token}`;

  const language = localStorage.getItem("language") || "en";
  let headersObj: any = {
    ...headers,
    "Content-Type": "application/json",
  };
  if (authInfo?.state.token) {
    headersObj = {
      ...headersObj,
      authorization,
    };
  }
  if (language) {
    headersObj = {
      ...headersObj,
      "Accept-Language": language,
    };
  }
  try {
    const res = await fetch(`${host}${apiPath}`, {
      method: "POST",
      headers: headersObj,
      body: JSON.stringify(body),
    });
    
    // 检查响应状态
    if (!res.ok) {
      console.error("aierhubFetchFile", res.statusText);
      return {
        success: false,
        result: null,
      };
    }
    
    // 尝试不同的大小写形式
    const contentDisposition = res.headers.get('Content-Disposition');
    let filename = 'download';
    
    if (contentDisposition) {
      // 解析文件名
      const filenameRegex = /filename\*=UTF-8''([^;]+)/;
      const matches = filenameRegex.exec(contentDisposition);
      if (matches && matches[1]) {
        // 解码URL编码的文件名
        filename = decodeURIComponent(matches[1]);
      }
    }

    console.log("contentDisposition", contentDisposition); // 打印文件名，用于调试
    console.log("filename", filename); // 打印文件名，用于调试
    
    // 将响应转换为Blob
    const blob = await res.blob();
    
    // 创建一个临时URL
    const url = window.URL.createObjectURL(blob);
    
    // 创建一个隐藏的a标签用于下载
    const a = document.createElement('a');
    a.style.display = 'none';
    a.href = url;
    a.download = filename;
    
    // 添加到文档并触发点击
    document.body.appendChild(a);
    a.click();
    
    // 清理
    window.URL.revokeObjectURL(url);
    document.body.removeChild(a);
    
    return {
      success: true,
      result: { filename },
    };

  } catch (error) {
    console.error("aierhubFetchFile", error);
    return {
      success: false,
      result: null,
    };
  }
}

export async function parseResult(res: Response): Promise<Result> {
  const messageApi = getMessageApi();
  try {
    if (!res.ok) {
      if (res.status === 401) {
        // message.error(getTranslation("unauthorized_error"));
        // 使用认证服务执行登出
        await authService.logout();
      } else if (res.status === 403) {
        messageApi.error(getTranslation("forbidden_error"));
      } else if (res.status === 404) {
        messageApi.error(getTranslation("not_found_error"));
      } else if (res.status === 500) {
        messageApi.error(getTranslation("server_inner_error"));
      } else {
        messageApi.error(`${getTranslation("method_not_allowed_error")}: ${res.statusText}`);
      }
      return {
        success: false,
        result: null,
      };
    }
    const result = await res.json();
    return {
      success: res.ok,
      result,
    };
  } catch (error) {
    console.error("parseResult", error);
    return {
      success: false,
      result: null,
    };
  }
}
