import {
  CreatePaypalPaymentPayload,
  CapturePaypalPaymentPayload,
  CancelPaypalPaymentPayload,
  CreatePaypalSubscriptionPayload,
  VerifyPaypalSubscriptionPayload,
  CancelPaypalSubscriptionPayload
} from "../libs/interfaces";

import { aierhubGet, aierhubPost, Result } from "./aierhubFetch";

class PricingApi {
  constructor() {}

  /**
   * 获取订阅方案列表
   */
  async getPlanList(): Promise<Result> {
    return await aierhubGet(`/api/plan/list`);
  }
  /**
   * 获取购买积分列表
   */
  async getCreditsItem(): Promise<Result> {
    return await aierhubGet(`/api/plan/credit/list`);
  }

 /**
 * 创建Paypal购买积分订单
 */
  async createPayment(values: CreatePaypalPaymentPayload): Promise<Result> {
    return await aierhubPost(`/api/paypal/create_payment`, {}, values);
  }

  /**
   * 确认Paypal购买积分订单
   */
  async capturePayment(values: CapturePaypalPaymentPayload): Promise<Result> {
    return await aierhubPost(`/api/paypal/capture_payment`, {}, values);
  }

  /**
   * 用户放弃Paypal购买积分订单
   */
  async cancelPayment(values: CancelPaypalPaymentPayload): Promise<Result> {
    return await aierhubPost(`/api/paypal/cancel_payment`, {}, values);
  }

  /**
   * 创建Paypal会员订阅订单
   */
  async createSubscription(values: CreatePaypalSubscriptionPayload): Promise<Result> {
    return await aierhubPost(`/api/paypal/create_subscription`, {}, values);
  }

  /**
   * 确认Paypal会员订阅订单
   */
  async verifySubscription(values: VerifyPaypalSubscriptionPayload): Promise<Result> {
    return await aierhubPost(`/api/paypal/verify_subscription`, {}, values);
  }

  /**
   * 用户放弃Paypal会员订阅订单
   */
  async cancelSubscription(values: CancelPaypalSubscriptionPayload): Promise<Result> {
    return await aierhubPost(`/api/paypal/cancel_subscription`, {}, values);
  }

}
export default new PricingApi();
