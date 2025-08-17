import { RoleItemObj } from "./../../../../libs/interfaces";
import { createContext } from "react";

export interface IShareRoleViewContexts {
  checkedRoleItemIndex: number;
  setCheckedRoleItemIndex: React.Dispatch<React.SetStateAction<number>>;
  roleList: RoleItemObj[];
  setRoleList: React.Dispatch<React.SetStateAction<RoleItemObj[]>>;
  projectId: string;
  setProjectId: React.Dispatch<React.SetStateAction<string>>;
  uploadExampleFigureImg: string;
  setUploadExampleFigureImg: React.Dispatch<React.SetStateAction<string>>;
}

export const ShareRoleViewContexts = createContext<IShareRoleViewContexts>(
  {} as IShareRoleViewContexts
);
