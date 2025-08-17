import {
  StoryboardCopyPayload,
  StoryboardDeletePayload,
  StoryboardSortPayload,
  StoryboardUpdatePayload,
  RenameProjectPayload,
} from "../libs/interfaces";
import { aierhubGet, aierhubPost, Result } from "./aierhubFetch";

class DashboardApi {
  constructor() {}

  /**
   * 获取案例列表
   */
  async getTemplateList(): Promise<Result> {
    return await aierhubGet(`/api/template/list`);
  }

  /**
   * 获取项目列表
   */
  async getProjectListByPage(
    pageNum: number,
    pageSize: number
  ): Promise<Result> {
    return await aierhubGet(
      `/api/storyboard/project/list?pageSize=${pageSize}&pageNum=${pageNum}`
    );
  }
  /**
   * 获取项目数量
   */
  async getProjectBenefit(): Promise<Result> {
    return await aierhubGet(`/api/storyboard/project/benefit`);
  }
  // 复制项目
  async copyProject(projectId: string): Promise<Result> {
    return await aierhubPost(
      `/api/storyboard/project/copy?projectId=${projectId}`,
      {},
      {}
    );
  }
  // 删除项目
  async deleteProject(projectId: string): Promise<Result> {
    return await aierhubPost(
      `/api/storyboard/project/delete?id=${projectId}`,
      {},
      {}
    );
  }
  // 更新项目
  async renameProject(values: RenameProjectPayload): Promise<Result> {
    return await aierhubPost(`/api/storyboard/project/rename`, {}, values);
  }
  // 更新分镜表
  async storyboardUpdate(values: StoryboardUpdatePayload): Promise<Result> {
    return await aierhubPost(`/api/storyboard/shot/update`, {}, values);
  }
  // 分镜表排序
  async storyboardSort(values: StoryboardSortPayload): Promise<Result> {
    return await aierhubPost(`/api/storyboard/shot/sort`, {}, values);
  }
  // 分镜表添加数据项
  async storyboardCopy(values: StoryboardCopyPayload): Promise<Result> {
    return await aierhubPost(`/api/storyboard/shot/copy`, {}, values);
  }
  // 分镜表删除数据项
  async storyboardDelete(values: StoryboardDeletePayload): Promise<Result> {
    return await aierhubPost(`/api/storyboard/shot/delete`, {}, values);
  }
  // 使用案例
  async useTemplate(id: string): Promise<Result> {
    return await aierhubPost(`/api/template/copy/${id}`, {}, {});
  }
}
export default new DashboardApi();
