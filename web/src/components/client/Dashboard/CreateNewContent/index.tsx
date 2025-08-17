/**
 * 创建新作品弹窗内容
 */

import { Divider } from "antd";
import React, { useContext } from "react";
import CreateNewTitle from "../CreateNewTitle";

import ProjectInfoForm from "../ProjectInfoForm";
import WriteStoryForm from "../WriteStoryForm";

import {
  CreateNewContexts,
  ICreateNewContexts,
} from "../../../../contexts/create-new-contexts";
interface IProps {
}

const CreateNewContent: React.FC<IProps> = ({
}: IProps) => {
  const createNewContexts: ICreateNewContexts = useContext<ICreateNewContexts>(CreateNewContexts);
  return (
    <div className="max-h-[calc(100vh-100px)] min-w-[848px]">
      <CreateNewTitle />
      <div className="relative border-y h-[554px]">
        <div className="flex h-full">
          <div
            className={`px-6 py-6 relative transition-all duration-500 ${
              createNewContexts.projectInfoFold ? "w-1/4" : "w-1/2"
            }`}
          >
            <ProjectInfoForm />
          </div>
          <Divider type="vertical" className="h-full mx-0" />
          <div
            className={`px-6 py-6 ${
              createNewContexts.projectInfoFold ? "w-3/4" : "w-1/2"
            }`}
          >
            <WriteStoryForm />
          </div>
        </div>
      </div>
    </div>
  );
};

export default CreateNewContent;
