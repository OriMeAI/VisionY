import { AUTH } from "./global-config";
import { CustomerLoginBody } from "./interfaces";

class UserHelper {
  constructor() {}

  /** 获取本地用户信息 */
  getLocalUserInfo(): CustomerLoginBody | null {
    try {
      const storage = localStorage.getItem(AUTH);
      if (!storage) return null;
      return JSON.parse(storage);
    } catch (err) {
      return null;
    }
  }
  /** 设置本地用户信息 */
  setLocalUserInfo(data: CustomerLoginBody) {
    localStorage.setItem(AUTH, JSON.stringify(data));
  }

  /** 移除本地用户信息 */
  clearLocalUserInfo() {
    localStorage.setItem(
      AUTH,
      JSON.stringify({
        state: { isAuthenticated: false, token: "" },
        version: 0,
      })
    );
  }
}
export default new UserHelper();
