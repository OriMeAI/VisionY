import { ROLE_TOUR_SHOWN, TABLE_TOUR_SHOWN } from "./global-config";

class TourHelper {
  constructor() {}

  /** 获取是否显示角色引导 */
  getLocalRoleTourShown(): string | null {
    try {
      const storage = localStorage.getItem(ROLE_TOUR_SHOWN);
      if (!storage) return null;
      return storage;
    } catch (err) {
      return null;
    }
  }
  /** 设置是否显示角色引导 */
  setLocalRoleTourShown(data: string) {
    localStorage.setItem(ROLE_TOUR_SHOWN, data);
  }

  /** 获取是否显示分镜表引导 */
  getLocalTableTourShown(): string | null {
    try {
      const storage = localStorage.getItem(TABLE_TOUR_SHOWN);
      if (!storage) return null;
      return storage;
    } catch (err) {
      return null;
    }
  }
  /** 设置是否显示分镜表引导 */
  setLocalTableTourShown(data: string) {
    localStorage.setItem(TABLE_TOUR_SHOWN, data);
  }
}
export default new TourHelper();
