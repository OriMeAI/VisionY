import { 
  GetRechargeRecordPayload,
  UsageRecordPayload,
  GetObtainedRecordPayload
} from "../libs/interfaces";
import { aierhubGet, aierhubPost, Result } from "./aierhubFetch";

class UserApi {
  constructor() {}

  /**
   * 获取用户信息
   */
  async getUserInfo(): Promise<Result> {
    return await aierhubGet(`/api/user/info`);
  }

  /**
   * 获取积分详情
   */
  async getCreditsRecord(): Promise<Result> {
    return await aierhubGet(`/api/transaction/credits_record`);
  }

  /**
   * 获取积分使用记录
   */
  async getUsageRecordByPage(values: UsageRecordPayload): Promise<Result> {
    return await aierhubPost(`/api/transaction/usage_record`, {}, values);
  }

  /**
   * 获取积分获取记录
   */
  async getObtainedRecordByPage(values: GetObtainedRecordPayload): Promise<Result> {
    return await aierhubPost(`/api/transaction/obtained_record`,{},values);
  }

  /**
   * 获取充值记录
   */
  async getRechargeRecordByPage(values: GetRechargeRecordPayload): Promise<Result> {
    return await aierhubPost(`/api/transaction/recharge_record`,{},values);
  }
  /**
   * 上传图片
   */
  async fileUpload(values: { file: File }): Promise<Result> {
    return await aierhubPost(`/api/oss/file/upload`, {}, values);
  }
  /**
   * 更新用户信息
   */
  async userUpdate(values: {
    avatar?: string;
    name?: string;
  }): Promise<Result> {
    return await aierhubPost(`/api/user/update`, {}, values);
  }
}
export default new UserApi();
