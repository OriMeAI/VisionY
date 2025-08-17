import { aierhubGet, parseResult, Result } from "./aierhubFetch";

class ShareApi {
  constructor() {}

  /**
   * 获取案例项目数据
   */
  async getTemplateById(id: string): Promise<Result> {
    return await aierhubGet(`/api/template/${id}`);
  }

  /**
   * 获取案例分镜表（表格数据）
   */
  async getTemplateShootById(id: string): Promise<Result> {
    return await aierhubGet(`/api/template/shot/${id}`);
  }

  /**
   * 获取案例角色数据
   */
  async getTemplateRoleById(id: string): Promise<Result> {
    return await aierhubGet(`/api/template/role/${id}`);
  }
}
export default new ShareApi();
