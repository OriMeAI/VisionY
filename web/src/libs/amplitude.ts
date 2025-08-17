import amplitude from 'amplitude-js';
// Amplitude API Key - 请替换为您的实际 API Key
const AMPLITUDE_API_KEY = process.env.AMPLITUDE_API_KEY;

// 初始化 Amplitude
export const initAmplitude = () => {
  amplitude.getInstance().init(AMPLITUDE_API_KEY, undefined, {
    // 配置选项
    includeUtm: true,
    includeReferrer: true,
    includeFbclid: true,
    includeGclid: true,
    saveEvents: true,
    savedMaxCount: 1000,
    forceHttps: true,
    trackingOptions: {
      city: true,
      country: true,
      carrier: false,
      device_manufacturer: false,
      device_model: false,
      dma: false,
      ip_address: false,
      language: true,
      os_name: true,
      os_version: false,
      platform: true,
      region: true,
      version_name: false
    }
  });
};

// 设置用户ID
export const setUserId = (userId: string) => {
  amplitude.getInstance().setUserId(userId);
};

// 设置用户属性
export const setUserProperties = (properties: Record<string, any>) => {
  amplitude.getInstance().setUserProperties(properties);
};

// 追踪事件
export const trackEvent = (eventName: string, eventProperties?: Record<string, any>) => {
  amplitude.getInstance().logEvent(eventName, eventProperties);
};

// 追踪页面浏览
export const trackPageView = (pageName: string, properties?: Record<string, any>) => {
  amplitude.getInstance().logEvent('page_viewed', {
    page_name: pageName,
    ...properties
  });
};

// 导出 amplitude 实例以备高级用法
export { amplitude };