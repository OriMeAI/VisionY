import projectApi from "./../../../api/projectApi";
import { IRoleViewContexts } from "../../../contexts/role-view-contexts";

class RoleViewStore {
  constructor() {}
  async getRoleList(roleViewContexts: IRoleViewContexts, callback: () => void) {
    const data = await projectApi.getRoleListById({
      projectId: roleViewContexts.projectId
    });
    callback();
    roleViewContexts.setRoleList(data.result.data);
    if (Array.isArray(data.result.data) && data.result.data.length > 0) {
      roleViewContexts.setCheckedRoleItemIndex(0);
    }
  }
}
export default new RoleViewStore();
