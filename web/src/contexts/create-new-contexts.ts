import { UploadFile } from "antd";
import { createContext } from "react";
import { WriteStoryInputType } from "../libs/enums";

export interface ICreateNewContexts {
  projectInfoFold: boolean;
  setProjectInfoFold: React.Dispatch<React.SetStateAction<boolean>>;
  projectName: string;
  setProjectName: React.Dispatch<React.SetStateAction<string>>;
  writeStoryInputType: WriteStoryInputType;
  setWriteStoryInputType: React.Dispatch<React.SetStateAction<WriteStoryInputType>>;
  isExpandingStory: boolean;
  setIsExpandingStory: React.Dispatch<React.SetStateAction<boolean>>;
  originStoryText: string;
  setOriginStoryText: React.Dispatch<React.SetStateAction<string>>;
  expandedStoryText: string;
  setExpandedStoryText: React.Dispatch<React.SetStateAction<string>>;
  yourStoryText: string;
  setYourStoryText: React.Dispatch<React.SetStateAction<string>>;
  uploadScriptFile: UploadFile<any> | null,
  setUploadScriptFile: React.Dispatch<React.SetStateAction<UploadFile<any> | null>>;
  aspectRatio: string;
  setAspectRatio: React.Dispatch<React.SetStateAction<string>>;
  storyBoardType: number;
  setStoryBoardType: React.Dispatch<React.SetStateAction<number>>;
}

export const CreateNewContexts = createContext<ICreateNewContexts>(
  {} as ICreateNewContexts
);
