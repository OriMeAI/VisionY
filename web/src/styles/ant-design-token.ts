import { ANTD_COLOR_PRIMARY } from "../libs/global-config";

/** Antd 主题变量 */
export const ANT_DESIGN_TOKEN = {
    /** 全局token */
    token: {
      colorPrimary: ANTD_COLOR_PRIMARY,
      colorLink: ANTD_COLOR_PRIMARY,
      colorLinkHover: ANTD_COLOR_PRIMARY,
      colorLinkActive: ANTD_COLOR_PRIMARY,
      colorPrimaryHover: ANTD_COLOR_PRIMARY,
      colorTextHover: ANTD_COLOR_PRIMARY,
      colorBorderHover: ANTD_COLOR_PRIMARY
    },
    components: {
      Layout: {
        
      },
      Menu: {},
      Input: {
        colorPrimary: ANTD_COLOR_PRIMARY,
        borderColor: ANTD_COLOR_PRIMARY,
      },
      Checkbox: {
        colorPrimary: ANTD_COLOR_PRIMARY,
        borderColor: ANTD_COLOR_PRIMARY,
      },
      Modal: {
        contentBg: "#ffffff",
        colorPrimary: ANTD_COLOR_PRIMARY,
        colorPrimaryHover: ANTD_COLOR_PRIMARY,
        colorTextHover: ANTD_COLOR_PRIMARY,
        colorBorderHover: ANTD_COLOR_PRIMARY,
        titleFontSize: 16,
        titleLineHeight: 24,
        padding: 24,
        paddingContentHorizontal: 24,
        paddingContentVertical: 24,
        margin: 0,
        borderRadiusLG: 8,
        Button: {
          colorPrimary: ANTD_COLOR_PRIMARY,
          colorPrimaryHover: "#6941c6",
          colorPrimaryActive: "#5925dc",
          colorBorder: "#d0d5dd",
          colorText: "#344054",
          colorBgContainer: "#ffffff",
          colorBorderHover: ANTD_COLOR_PRIMARY,
          colorTextHover: ANTD_COLOR_PRIMARY,
        }
      },
    },
  };
  