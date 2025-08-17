import loginApi from "../api/loginApi";
import userHelper from "./user-helper";
import { googleLogout } from '@react-oauth/google';

// 单例模式
class AuthService {
  private static instance: AuthService;
  private logoutCallbacks: Array<() => void> = [];

  private constructor() {}

  public static getInstance(): AuthService {
    if (!AuthService.instance) {
      AuthService.instance = new AuthService();
    }
    return AuthService.instance;
  }

  public registerLogoutCallback(callback: () => void): void {
    this.logoutCallbacks.push(callback);
  }

  public async logout(): Promise<void> {
    const data = await loginApi.logout();
    googleLogout();
    userHelper.clearLocalUserInfo();
    console.log("logout", data);
    
    // 调用所有注册的回调
    this.logoutCallbacks.forEach(callback => callback());
  }
}

export default AuthService.getInstance();