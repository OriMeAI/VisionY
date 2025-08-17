import { RepaintPayload } from "../libs/interfaces";
import { aierhubGet, aierhubPost, parseResult, Result } from "./aierhubFetch";

class EditorApi {
  constructor() {}

  /**
   * 重绘
   */
  // async repaintShot(values: RepaintPayload): Promise<Result> {
  //   return await aierhubPost(`/api/storyboard/shot/repaint`, {}, values);
  // }
  /**
   * 获取当前故事板详情
   */
  async getStoryboardShotDetail(storyboardId: string): Promise<Result> {
    return await aierhubGet(
      `/api/storyboard/shot/detail?storyboardId=${storyboardId}`
    );
  }
}
export default new EditorApi();
