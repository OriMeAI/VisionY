// 公共路由配置（正则表达式）
export const validRoutes = [
  "/",
  "/workspace",
  /^\/project\/[a-f0-9]{32}\/scriptview$/,
  /^\/project\/[a-f0-9]{32}\/roleview$/,
  /^\/project\/[a-f0-9]{32}\/tableView$/,
  /^\/project\/[a-f0-9]{32}\/boardview$/,
  /^\/share\/[a-f0-9]{32}$/,
  "/usercenter",
  "/termsofuse",
  "/privacypolicy",
  "/aboutus",
];
