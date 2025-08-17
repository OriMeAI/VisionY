import {
  AddRolePayload,
  CopyRolePayload,
  ApplyHistoryImagePayload,
  CreateProjectPayload,
  deleteRoleExamplePayload,
  deleteRolePayload,
  FetchImgPayload,
  GetRecentRoleListPayload,
  GetRoleListPayload,
  ImageGenerateHistoryItemPayload,
  // regenerateShotImagePayload,
  regenerateImageStatusPayload,
  // RegenerateRolePayload,
  ReplaceImagePayload,
  scriptToShotPayload,
  updateDefaultHistoryPayload,
  RenameRolePayload,
  uploadExampleFigurePayload,
  generateHighDefinitionImagePayload,
} from "../libs/interfaces";
import { aierhubGet, aierhubPost, Result } from "./aierhubFetch";

class ProjectApi {
  constructor() {}

  async getProjectStyles(): Promise<Result> {
    return await aierhubGet(`/api/storyboard/project/style`);
  }

  async getProjectStories(): Promise<Result> {
    return await aierhubGet(`/api/storyboard/project/stories`);
  }



  async createProject(values: CreateProjectPayload): Promise<Result> {
    return await aierhubPost(`/api/storyboard/create/project`, {}, values);
  }

  async getProjectById(projectId: string): Promise<Result> {
    return await aierhubGet(`/api/storyboard/project/info?id=${projectId}`);
  }

  async getRoleListById(values: GetRoleListPayload): Promise<Result> {
    return await aierhubPost(`/api/storyboard/role/list`, {}, values);
  }

  async getStoryboardListById(projectId: string): Promise<Result> {
    return await aierhubGet(`/api/storyboard/shot/list?projectId=${projectId}`);
  }

  async getRecentRoleList(values: GetRecentRoleListPayload): Promise<Result> {
    return await aierhubPost(`/api/storyboard/role/recent`, {}, values);
  }

  async addRoleItem(values: AddRolePayload): Promise<Result> {
    return await aierhubPost(`/api/storyboard/role/add`, {}, values);
  }

  async copyRoleItem(values: CopyRolePayload): Promise<Result> {
    return await aierhubPost(`/api/storyboard/role/copy`, {}, values);
  }

  // async regenerateRole(values: RegenerateRolePayload): Promise<Result> {
  //   return await aierhubPost(`/api/storyboard/role/regenerate`, {}, values);
  // }

  async getRoleImageHistory(values: {
    projectId: string;
    roleId: string;
  }): Promise<Result> {
    return await aierhubPost(`/api/storyboard/role/history`, {}, values);
  }

  async updateDefaultHistory(
    values: updateDefaultHistoryPayload
  ): Promise<Result> {
    return await aierhubPost(`/api/storyboard/role/update_default`, {}, values);
  }

  async deleteRole(values: deleteRolePayload): Promise<Result> {
    return await aierhubPost(`/api/storyboard/role/delete`, {}, values);
  }

  async swapFaceCheck(values: { preCheck: boolean }): Promise<Result> {
    return await aierhubPost(`/api/storyboard/swap/face/check`, {}, values);
  }

  async uploadExampleFigure( values: uploadExampleFigurePayload ): Promise<Result> {
    return await aierhubPost(`/api/storyboard/role/upload_example_figure`,{}, values);
  }

  async scriptToShot(values: scriptToShotPayload): Promise<Result> {
    return await aierhubPost(`/api/storyboard/script_to_shot`, {}, values);
  }

  async fetchImg(values: FetchImgPayload): Promise<Result> {
    return await aierhubPost(`/api/storyboard/fetch_img`, {}, values);
  }

  async deleteRoleExample(values: deleteRoleExamplePayload): Promise<Result> {
    return await aierhubPost(`/api/storyboard/role_example/delete`, {}, values);
  }

  // async generateHighDefinitionImage( values: generateHighDefinitionImagePayload): Promise<Result> {
  //   return await aierhubPost(`/api/storyboard/shot/hd_resolution`,{},values);
  // }

  // async regenerateShotImage(values: regenerateShotImagePayload): Promise<Result> {
  //   return await aierhubPost(`/api/storyboard/shot/regenerate`, {}, values);
  // }

  async regenerateImageStatus( values: regenerateImageStatusPayload ): Promise<Result> {
    return await aierhubPost(`/api/storyboard/status`, {}, values);
  }

  async getImageGenerateHistory(
    values: ImageGenerateHistoryItemPayload
  ): Promise<Result> {
    return await aierhubPost(`/api/storyboard/shot/history`, {}, values);
  }

  async applyHistoryImage(values: ApplyHistoryImagePayload): Promise<Result> {
    return await aierhubPost(`/api/storyboard/shot/pic_apply`, {}, values);
  }

  async replaceImage(values: ReplaceImagePayload): Promise<Result> {
    return await aierhubPost(`/api/storyboard/shot/pic_upload`, {}, values);
  }

  async renameRole(values: RenameRolePayload): Promise<Result> {
    return await aierhubPost(`/api/storyboard/role/rename`, {}, values);
  }
}
export default new ProjectApi();
