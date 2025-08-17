import { message } from 'antd';

// 创建全局变量
declare global {
  var globalMessageApi: any;
}

// 初始化全局变量
if (typeof window !== 'undefined') {
  window.globalMessageApi = message;
}

export const setMessageApi = (api: any) => {
  window.globalMessageApi = api;
};

export const getMessageApi = () => {
  return window.globalMessageApi || message;
}; 