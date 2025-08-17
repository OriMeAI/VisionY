import { DetailTabType } from "./enums";
import layers2Icon from "./../../assets/images/pages/usercenter/layers2_icon.svg";
import layersIcon from "./../../assets/images/pages/usercenter/layers_icon.svg";
import usersIcon from "./../../assets/images/pages/usercenter/users_icon.svg";
import zapIcon from "./../../assets/images/pages/usercenter/zap_icon.svg";
import VisionYLogo from "./../../home/static/assets/visiony_logo_transparent_180.svg";
import VisionYDarkLogo from "./../../home/static/assets/visiony_logo_transparent_180.svg";

export const ANTD_COLOR_PRIMARY = "#7E2FFF";

export const LANGUAGE = "language";
export const ERROR_MSG_404 = "errorMsg404";
export const AUTH = "auth";
export const ROLE_TOUR_SHOWN = "roleTourShown";
export const TABLE_TOUR_SHOWN = "tableTourShown";

//google client id
export const GOOGLE_CLIENT_ID = process.env.GOOGLE_CLIENT_ID;

// logo base64
export const LOGO_BASE64_SRC_DARK = VisionYDarkLogo

export const LOGO_BASE64_SRC_LIGHT = VisionYLogo

// 路由与tab映射
export const LINK_BG_COLOR_MAPS = {
  scriptview: "rgb(249 250 251)",
  roleview: "rgb(249 250 251)",
  tableview: "#ffffff",
  boardview: "rgb(243 244 246)",
  visualview: "#ffffff",
};

// tab与路由映射
export const TAB_LINK_MAPS = {
  [DetailTabType.Script]: `scriptviewold`,
  [DetailTabType.Role]: `roleviewold`,
  [DetailTabType.FilmTable]: `tableviewold`,
  [DetailTabType.Storyboard]: `boardviewold`,
  [DetailTabType.VisualView]: `visualmodeold`,
};

// tab与路由映射
export const TAB_LINK_MAPS_NEW = {
  [DetailTabType.Script]: `scriptview`,
  [DetailTabType.Role]: `roleview`,
  [DetailTabType.FilmTable]: `tableview`,
  [DetailTabType.Storyboard]: `boardview`,
  [DetailTabType.VisualView]: `visualview`,
};
// 路由与tab映射
export const LINK_TAB_MAPS = {
  scriptviewold: DetailTabType.Script,
  roleviewold: DetailTabType.Role,
  tableviewold: DetailTabType.FilmTable,
  boardviewold: DetailTabType.Storyboard,
  visualmodeold: DetailTabType.VisualView,
};

// 订阅会员icon映射
export const PLAN_ICON_MAPS = {
  Zap: zapIcon,
  Layers2: layers2Icon,
  Layers: layersIcon,
  Users: usersIcon,
};
