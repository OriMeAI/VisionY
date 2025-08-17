// 工具栏
export enum ToolName {
  // Pointer = "pointer",
  Gripper = "gripper",
  Brush = "brush",
  Eraser = "eraser",
  Enlarge = "enlarge",
  Lessen = "lessen",
}

// 缩放类型
export enum ScaleChangeType {
  Enlarge,
  Lessen,
}

// 写故事输入类型
export enum WriteStoryInputType {
  AiExtension = "AiExtension",
  InputYourStory = "InputYourStory",
  UploadScript = "UploadScript",
}

export enum StoryScriptType {
  AI_GENERATED = 1,    // AI扩展生成
  MANUAL_INPUT = 2,    // 手动输入故事
  FILE_UPLOAD = 3,      // 文件上传剧本
  Empty = 0     // 空项目
}

// 当前画布宽高以小的一边为准
export enum MinSide {
  Width,
  Height,
}

// 文件类型
export enum FileType {
  Docx = "docx",
  Xlsx = "xlsx",
  Txt = "txt",
}

// 项目详情页tab类型
export enum DetailTabType {
  Script,
  Role,
  FilmTable,
  Storyboard,
  VisualView
}

// StoryHeadId
export enum StoryHeadIdType {
  // 镜号
  BoardNumber = 2,
  // 画面
  Picture = 3,
  // 画面描述
  PictureDesc = 4,
  // 台词
  Lines = 10,
  // 主要人物
  MainFigure = 7,
  // 景别
  Scene = 5,
  // 相机角度
  CameraAngle = 9,
  // 镜头类型
  ShotType = 13,
  // 时长
  Duration = 6,
  //背景描述
  BackgroundDesc = 158,
  // 角色描述
  RoleDesc = 159,
  // 其它描述
  OtherDesc = 160,
}

// 会员类型
export enum MemberType {
  MONTHLY = "MONTHLY",
  ANNUAL = "ANNUAL",
}

export enum PayType {
  Wechat = "Wechat",
  Alipay = "Alipay",
}
// 重绘状态
export enum RepaintStatus {
  UnStart,
  Rendering,
  Success,
  Loading
}
