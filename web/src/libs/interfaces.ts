import { ToolName } from "./enums";

// 更新分镜表参数
import { CameraAngle, Dialogue, MainCharacter, SceneDescription, ShotResource, ShotTime, ShotType, ShotSize, StoryboardShot } from '../types/storyboard';

export interface ImageSize {
  width: number;
  height: number;
}
export interface RepaintPayload {
  projectId: string;
  originImgUrl: string;
  originImgWidth: number,
  originImgHeight: number,
  imgPrompts: string;
  maskData: string;
  storyboardId: string;
}

export interface CreateProjectPayload {
  file?: File;
  content?: string;
  name: string;
  storyBoardType: number;
  scriptType: number;
  aspectRatio: string;
}

// 获取角色列表参数
export interface GetRoleListPayload {
  projectId: string;
}

// 重新生成图片参数
// export interface RegenerateRolePayload {
//   figureExampleUrl: string | null;
//   projectId: string;
//   figureName: string;
//   figureDesc: string;
//   roleId: string;
// }

export interface updateDefaultHistoryTarget {
  id?: string;
  figureName?: string;
  url?: string;
  mainFigureUrl?: string;
  figureExampleUrl?: string[];
}

// 保存历史形象参数
export interface updateDefaultHistoryPayload {
  projectId: string;
  targetId: string;
  roleId: string;
}

// 删除角色参数
export interface deleteRolePayload {
  projectId: string;
  roleId: string;
}

// 删除上传人脸参考图
export interface deleteRoleExamplePayload {
  projectId: string;
  roleId: string;
}
// 上传高清图片
export interface generateHighDefinitionImagePayload {
  projectId: string;
  storyboardId: string;
}
// 重新生成图片参数
// export interface regenerateShotImagePayload {
//   storyboardId: string;
// }
// 重新生成图片状态参数
export interface regenerateImageStatusPayload {
  projectId: string;
  storyboardId: string;
  type: number;
}
// 重新生成图片状态
export interface regenerateImageStatus {
  projectId: string;
  storyboardId: string;
  status: string;
  resultUrl: string | null;
  queuePosition: number;
}
// 上传人脸参考图
export interface uploadExampleFigurePayload {
  projectId: string;
  fileData: string;
  fileName: string;
}
export interface scriptToShotPayload {
  id: string;
  name: string;
  type: number;
  storyBoardType: number;
  storyBoardTypeDesc: string | null;
  pictureSize: string;
  cover: string | null;
  scriptType: number;
  hasShot: boolean;
  hasRole: boolean;
  hasStoryboard: boolean;
  updateTime: string;
  content: string;
  hasAuth: boolean;
  imgWidth: number;
  imgHeight: number;
}
// 重新生成图片参数
export interface RegenerateRoleResult {
  faceCropImgUrl: string;
  faceSwapImgUrl: string;
  figureDesc: string;
  figureName: string;
}
export interface AddRolePayload {
  projectId: string;
}
export interface CopyRolePayload {
  projectId: string;
  roleId?: string;
}

// 获取最近使用的角色列表参数（分页）
export interface GetRecentRoleListPayload {
  pageSize: number;
  pageNum: number;
  figureName: string;
}

// 最近使用的角色列表项数据
export interface RecentRoleItemObj {
  id: string;
  cnDesc: string;
  figureName: string;
  url: string;
  gender: string;
}

// 项目数量
export interface ProjectBenefitType {
  totalCount: number;
  usedCount: number;
}
// 项目列表
export interface ProjectListType {
  current: number;
  pages: number;
  records: ProjectItemObj[];
  size: number;
  total: number;
}

// 项目列表项数据
export interface ProjectItemObj {
  content: string;
  cover: string | null;
  hasAuth: boolean;
  hasRole: boolean;
  hasShot: boolean;
  hasStoryboard: boolean;
  id: string;
  imgHeight: number;
  imgWidth: number;
  name: string;
  pictureSize: string;
  scriptType: number;
  storyBoardType: number;
  storyBoardTypeDesc: string | null;
  type: number;
  updateTime: string;
}

// 角色列表项数据
export interface RoleItemObj {
  age?: number | null;
  enDesc?: string | null;
  figureDesc?: string;
  figureExampleUrl?: string[];
  figureName: string;
  gender?: string | null;
  loraId?: string;
  mainFigureUrl?: string;
  roleId?: string;
  url: string;
  voice?: string | null;
}
// 角色列表项数据
export interface ImagePreviewItemObj {
  alt: string;
  id: string;
  src: string;
}

export interface StoryboardItemBodyItem {
  cols: StoryboardItemBodyCol[];
  id: string;
  storyBoardNumber: number;
}

// 故事板表格数据（分镜表数据与故事板一样）
export interface StoryboardTableData {
  message: string | null;
  body: StoryboardItemBodyItem[];
  header: StoryboardItemHeaderCol[];
  clientId: string | null;
  taskId: string | null;
}

export interface StoryboardItemBodyCol {
  colName: string;
  storyHeadId: number;
  cellValue: string;
  cellValueType: string;
  cellId: string;
}
export interface StoryboardShotDetailItem {
  id: string;
  storyboardId: string;
  storyBoardHeadId: number;
  cellValue: string;
  cellValueType: string;
  storyBoardHeadName: string;
}

export interface StoryboardItemHeaderCol {
  id: number;
  readOnly: boolean;
  name: string;
  cellValueType: string;
  priority: number;
}

export interface RoleImageHistoryItem {
  id: string;
  url: string;
  mainFigureUrl: string;
  figureExampleUrl: string[];
  figureName: string;
  figureDesc: string;
  selected: boolean;
  roleId: string;
}

// TODO: 此处数据和roleList和表格主要人物都不匹配，不知道数据来源在哪里
export interface MainFigureItem {
  figureName: string;
  mainFigureUrl: string;
  roleId: string;
  loraId?: string;
  figureDesc?: string;
  enDesc?: string;
  url?: string;
  gender?: string;
  age?: number;
  voice?: string;
  figureExampleUrl?: string[];
  selected?: boolean;
}

// 查看图片生成历史
export interface ImageGenerateHistoryItem {
  id: string;
  projectId: string;
  storyboardId: string;
  selected: boolean;
  url: string;
}

// 查看图片生成历史参数
export interface ImageGenerateHistoryItemPayload {
  projectId: string;
  storyboardId: string;
}

// 应用历史图片参数
export interface ApplyHistoryImagePayload {
  projectId: string;
  storyboardId: string;
  targetId: string;
}

// 替换图片参数
export interface ReplaceImagePayload {
  shotId: string;
  projectId: string;
  fileData: string;
  fileName: string;
}

// 画布工具栏列表项
export interface EditorToolItem {
  id: number;
  icon: string;
  hoverIcon: string;
  activeIcon: string;
  tip: string;
  name: ToolName;
}

// 统计数据
export interface StatDataType {
  imgCount: string;
  projectCount: string;
}

// 案例展示列表项
export interface TemplateItem {
  id: string;
  storyBoardType: string;
  name: string;
  cover: string;
  coverTitle: string;
  intro: string;
  updateTime: string;
}

export interface FeaturesExtItem {
  title: string;
  desc: string;
}

// 订阅方案列表项
export interface PlanItemType {
  cycle: string;
  description: string;
  features: string[];
  featuresExt: FeaturesExtItem[];
  icon: string;
  id: number;
  name: string;
  price: string;
  strikePrice: string;
}

export interface PlanBenefitTimePeriodType {
  desc: string;
  name: string;
  price: string;
}
export interface PlanBenefitType {
  face_swap_count: number;
  resource_generation_credits: number;
  project_content_length: number;
  project_count: number;
}
// 购买生图次数
export interface CreditsItemType {
  id: number;
  name: string;
  code: string;
  icon: string | null;
  price: string;
  addonType: string;
  isFirstRecharge: boolean;
  addonValue: number;
  description: string;
}

// 全部订阅方案表格数据列表项
export interface PlanBenefitItemType {
  featuresExt: FeaturesExtItem[];
  planId: number;
  benefit: PlanBenefitType;
  annual: PlanBenefitTimePeriodType;
  monthly: PlanBenefitTimePeriodType;
}
// 订阅支付详情
export interface PlanDetailType {
  addonFeatures: string[] | null;
  addonValue: string | null;
  cycle: string;
  description: string;
  features: string[];
  icon: string;
  id: number;
  name: string;
  price: string;
}

// 会员权益
// export interface MemberBenefitType {
//   imgToVideoRemainingCount: number;
//   imgRemainingCount: number;
//   projectContentLength: number;
// }

// 用户信息
export interface UserInfoType {
  name: string;
  avatar: string;
  planId: number;
  planName: string;
  planExpiryTime: string;
  credits: number;
}

// 会员权益信息
export interface SubscriptionBenefitType {
  endTime: string | null;
  featuresExt: FeaturesExtItem[];
  planId: number;
  remainingCount: number;
  startTime: string | null;
  subPlanName: string | null;
  totalCount: number;
  userId: number;
}

// 获取充值记录参数
export interface GetRechargeRecordPayload {
  pageSize: number;
  pageNum: number;
  rechargeStatus: string;
}

// 充值记录
export interface RechargeRecordItemType {
  rechargeTime: string;
  typeDesc: string;
  totalAmount: string;
  orderNo: string;
  rechargeStatus:string,
  rechargeStatusDesc: string;
}

// 充值记录分页列表
export interface RechargeRecordListType {
  current: number;
  pages: number;
  records: RechargeRecordItemType[];
  size: number;
  total: number;
}

// 更新项目
export interface RenameProjectPayload {
  id: string;
  name: string;
}

// 更新角色参数
export interface RenameRolePayload {
  figureName: string;
  projectId: string;
  roleId: string;
}

export interface StoryboardUpdatePayload {
  projectId: string;
  storyboardId: string;
  data: string | Record<string, string|number> | ShotResource | SceneDescription | Dialogue[] | MainCharacter[] | ShotSize | CameraAngle | ShotType | ShotTime;
  updateType: string; // 从data的key中获取
}

// 更新分镜表排序参数
export interface StoryboardSortPayload {
  currentId: string;
  projectId: string;
  targetId: string;
}
// 分镜表增加数据项参数
export interface StoryboardCopyPayload {
  projectId: string;
  storyboardId: string;
}
// 分镜表删除数据项参数
export interface StoryboardDeletePayload {
  projectId: string;
  storyboardId: string;
}

export interface FetchImgPayload {
  projectId: string;
  storyHeadId: number;
  storyboardId: string[];
}
export interface FetchImgItemType {
  storyboardId: string;
  storyHeadId: number;
  cellValue: string;
}
// 角色描述项
export interface RoleDescItemType {
  imgPrompts: string;
  engPrompts: string;
  bboxCoords: number[];
  poseCoords: number[];
  name: string;
  roleId: string;
  bboxModified: boolean;
}

// 角色描述
export interface RoleDescObj {
  characterDetail: RoleDescItemType[];
}

// 画面
export interface PictureObj {
  image: string;
  isHd: boolean;
}
// 背景描述项
export interface BackgroundDescItemType {
  imgPrompts: string;
  engPrompts: string;
  backgroundId: string;
}

// 背景描述
export interface BackgroundDescObj {
  backgroundDetail: BackgroundDescItemType;
}

export interface CustomerLoginBodyState {
  isAuthenticated: boolean;
  token: string;
}
export interface CustomerLoginBody {
  state: CustomerLoginBodyState;
  version: number;
}

export interface UsageRecordPayload {
  pageSize: number;
  pageNum: number;
}

export interface GetObtainedRecordPayload {
  pageSize: number;
  pageNum: number;
}

export interface UsageRecordRecentItemType {
  endTime: string;
  imgRemainingCount: number;
}

export interface CreditsRecordItemType {
  totalCredits: number;
  purchaseCredits: number;
  membershipCredits: number;
  freeCredits: number;
}

export interface UsageRecordDataItemType {
  usedToken: string;
  usedTime: string;
  typeDesc: string;
  creditsSource:string;
  quantity: number;
}

export interface ObtainedRecordDataItemType {
  obtainedTime: string;
  typeDesc: string;
  quantity: number;
}

export interface UsageRecordDataType {
  current: number;
  pages: number;
  records: UsageRecordDataItemType[];
  size: number;
  total: number;
}

export interface UsageRecordData {
  recent: UsageRecordRecentItemType[];
  data: UsageRecordDataType;
}

export interface CreatePrePayWxRes {
  outTradeNo: string;
  payType: string;
  sellId: string;
  tradeNo: string | null;
  tradeStatus: string;
}

//paypal的逻辑
export interface CreatePaypalPaymentPayload{
  itemId: number;
  amount: number;
  returnUrl: string;
  cancelUrl: string;
}

export interface CapturePaypalPaymentPayload{
  PayerID:string;
  token: string;
}

export interface CancelPaypalPaymentPayload{
  token: string;
}


export interface CreatePaypalSubscriptionPayload{
  planId: number;
  returnUrl: string;
  cancelUrl: string;
}

export interface VerifyPaypalSubscriptionPayload{
  subscriptionId: string,
  baToken: string,
  token: string,
}

export interface CancelPaypalSubscriptionPayload{
  subscriptionId: string,
}

//stripe的逻辑
export interface CreateStripePaymentPayload{
  itemId: number;
  amount: number;
  returnUrl: string;
  cancelUrl: string;
}

export interface CaptureStripePaymentPayload{
  token: string;
}

export interface CancelStripePaymentPayload{
  token: string;
}


export interface CreateStripeSubscriptionPayload{
  planId: number;
  returnUrl: string;
  cancelUrl: string;
}

export interface VerifyStripeSubscriptionPayload{
  token: string,
}

export interface CancelStripeSubscriptionPayload{
  token: string,
}


