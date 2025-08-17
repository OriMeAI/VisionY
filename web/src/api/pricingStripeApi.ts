import {
  CreateStripePaymentPayload,
  CaptureStripePaymentPayload,
  CancelStripePaymentPayload,
  CreateStripeSubscriptionPayload,
  VerifyStripeSubscriptionPayload,
  CancelStripeSubscriptionPayload
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
 * 创建Stripe购买积分订单
 */
  async createPayment(values: CreateStripePaymentPayload): Promise<Result> {
    return await aierhubPost(`/api/stripe/create_payment`, {}, values);
  }

  /**
   * 确认Stripe购买积分订单
   */
  async capturePayment(values: CaptureStripePaymentPayload): Promise<Result> {  
    return await aierhubPost(`/api/stripe/capture_payment`, {}, values);
  }

  /**
   * 用户放弃Stripe购买积分订单
   */
  async cancelPayment(values: CancelStripePaymentPayload): Promise<Result> {
    return await aierhubPost(`/api/stripe/cancel_payment`, {}, values);
  }

  /**
   * 创建Stripe会员订阅订单
   */
  async createSubscription(values: CreateStripeSubscriptionPayload): Promise<Result> {
    return await aierhubPost(`/api/stripe/create_subscription`, {}, values);
  }

  /**
   * 确认Stripe会员订阅订单
   */
  async verifySubscription(values: VerifyStripeSubscriptionPayload): Promise<Result> {
    return await aierhubPost(`/api/stripe/verify_subscription`, {}, values);
  }

  /**
   * 用户放弃Stripe会员订阅订单
   */
  async cancelSubscription(values: CancelStripeSubscriptionPayload): Promise<Result> {
    return await aierhubPost(`/api/stripe/cancel_subscription`, {}, values);
  }

}
export default new PricingApi();
