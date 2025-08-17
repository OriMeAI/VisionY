import { ProjectItemObj } from "./../../../../../libs/interfaces";
import { createContext } from "react";

export interface IDetailContexts {
  projectItemObj: ProjectItemObj;
  setProjectItemObj: React.Dispatch<React.SetStateAction<ProjectItemObj>>;
  showRightPanel: boolean;
  setShowRightPanel: React.Dispatch<React.SetStateAction<boolean>>;
}

export const DetailContexts = createContext<IDetailContexts>(
  {} as IDetailContexts
);
