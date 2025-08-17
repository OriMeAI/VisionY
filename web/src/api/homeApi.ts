import { aierhubGet, parseResult, Result } from "./aierhubFetch";

class HomeApi {
  constructor() {}

  /**
   * 获取生图数量和作品数量
   */
  async getStatistics(): Promise<Result> {
    return await aierhubGet(`/api/index/statistics`);
  }

}
export default new HomeApi();
