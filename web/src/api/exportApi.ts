import { aierhubPost, aierhubFetchFile, Result } from "./aierhubFetch";

class ExportApi {
  constructor() {}

  /**
   * 导出视频/分轨
   */
  async exportVideo(values: {
    projectId: string;
    exportAllTracks?: boolean;
  }): Promise<Result> {
    return await aierhubPost(`/api/storyboard/export/video`, {}, values);
  }
  /**
   * 导出所有图片
   */
  async exportImg(values: { projectId: string }): Promise<Result> {
    return await aierhubPost(`/api/storyboard/export/img`, {}, values);
  }
  /**
   * 导出excel
   */
  async exportExcel(values: { projectId: string }): Promise<Result> {
    return await aierhubFetchFile(`/api/storyboard/export/excel`, {}, values);
  }
  /**
   * 导出pdf
   */
  async exportPdf(values: { projectId: string }): Promise<Result> {
    return await aierhubPost(`/api/storyboard/export/pdf`, {}, values);
  }
}
export default new ExportApi();
