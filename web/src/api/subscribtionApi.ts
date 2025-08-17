import { UsageRecordPayload } from "../libs/interfaces";
import { aierhubGet, aierhubPost, parseResult, Result } from "./aierhubFetch";

class SubscribtionApi {
  constructor() {}

  /**
   * 获取支付信息
   */
  async getPlanDetailById(planId: string): Promise<Result> {
    return await aierhubGet(`/api/plan/detail/plan?planId=${planId}`);
  }
  /**
   * 获取购买生图次数支付信息
   */
  async getPlanDetailCreditById(planId: string): Promise<Result> {
    return await aierhubGet(
      `/api/plan/detail/credit?planId=${planId}`
    );
  }

  /**
   * 购买生图次数自定义价格
   */
  async prePurchase(values: {
    amount: string;
    count: string;
  }): Promise<Result> {
    return await aierhubPost(`/api/plan/credit/purchase`, {}, values);
  }

  /**
   * 新建支付订单
   */
  async orderCreate(values: {
    planId: string;
    sourceType: string;
  }): Promise<Result> {
    return await aierhubPost(`/api/order/create`, {}, values);
  }
  /**
   * 微信二维码支付轮询
   */
  async orderCreatePrePayWx(orderNo: string): Promise<Result> {
    return await aierhubGet(
      `/api/order/create_pre_pay/wx?orderNo=${orderNo}`
    );
  }
  /**
   * 支付宝二维码支付轮询
   */
  async orderCreatePrePayAli(orderNo: string): Promise<Result> {
    return await aierhubGet(
      `/api/order/trade/ali?orderNo=${orderNo}`
    );
  }
}
export default new SubscribtionApi();
