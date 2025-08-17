import { RoleItemObj } from "../libs/interfaces";
import { createContext } from "react";

export interface IRoleViewContexts {
  checkedRoleItemIndex: number;
  setCheckedRoleItemIndex: React.Dispatch<React.SetStateAction<number>>;
  roleList: RoleItemObj[];
  setRoleList: React.Dispatch<React.SetStateAction<RoleItemObj[]>>;
  projectId: string;
  setProjectId: React.Dispatch<React.SetStateAction<string>>;
  uploadExampleFigureImg: string;
  setUploadExampleFigureImg: React.Dispatch<React.SetStateAction<string>>;
  setIsTourOpen: React.Dispatch<React.SetStateAction<boolean>>;
  tourRef1: React.MutableRefObject<null>;
  tourRef2: React.MutableRefObject<null>;
  tourRef3: React.MutableRefObject<null>;
}

export const RoleViewContexts = createContext<IRoleViewContexts>(
  {} as IRoleViewContexts
);
