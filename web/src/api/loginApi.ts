import { aierhubGet, aierhubPost, parseResult, Result } from "./aierhubFetch";

class LoginApi {
  constructor() {}

  // google登录
  async googleLogin(values: {
    token: string;
  }): Promise<Result> {
    return await aierhubPost(
      `/api/auth/google/login`,
      {},
      values
    );
  }

  // 获取邮箱验证码
  async sendEmailCode(values: {
    email: string;
  }): Promise<Result> {
    return await aierhubPost(
      `/api/auth/email/send_code`,
      {},
      values
    );
  }
  // 验证码验证
  async captchaVerify(values: {
    captchaVerifyParam: string;
    scene: number;
  }): Promise<Result> {
    return await aierhubPost(`/api/captcha/verify`, {}, values);
  }
  // 获取手机验证码
  async sendSmsCode(values: {
    mobile: string;
    scene: number;
    ticket: string;
  }): Promise<Result> {
    return await aierhubPost(`/api/user/auth/send-sms-code`, {}, values);
  }
  // 手机登录
  async smsLogin(values: {
    code: string;
    mobile: string;
    ticket: string;
  }): Promise<Result> {
    return await aierhubPost(`/api/user/auth/sms-login`, {}, values);
  }
  // 邮箱登录
  async emailLogin(values: {
    code: string;
    email: string;
  }): Promise<Result> {
    return await aierhubPost(`/api/auth/email/login`, {}, values);
  }
  /**
   * 退出登录
   */
  async logout(): Promise<Result> {
    return await aierhubGet(`/api/auth/logout`);
  }
}
export default new LoginApi();
