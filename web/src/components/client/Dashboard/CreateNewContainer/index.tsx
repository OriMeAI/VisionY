import { App } from "antd";
import { UploadFile } from "antd";
import React, { useContext, useEffect, useState } from "react";
import { createPortal } from "react-dom";
import { useTranslation } from "react-i18next";

import CreateNewContent from "../CreateNewContent";
import CreateNewBtn from "../CreateNewBtn";
import ModalBase from "../../Common/ModalBase";

import projectApi from "./../../../../api/projectApi";
import {
  CreateNewContexts,
  ICreateNewContexts,
} from "./../../../../contexts/create-new-contexts";
import {
  DashboardContexts,
  IDashboardContexts,
} from "./../../../../contexts/dashboard-contexts";

import { WriteStoryInputType,StoryScriptType } from "./../../../../libs/enums";

// 在顶部引入区域新增
import FileReader from "../../../../libs/file-reader";

interface IProps {
  createNewText?: React.ReactNode;
  usedCount: number;
  totalCount: number;
}

// 默认画面尺寸
const DEFAULT_ASPECT_RATIO = "1:1";
// 默认画面风格
const DEFAULT_STORY_BOARD_TYPE = 0;


const CreateNewContainer: React.FC<IProps> = ({
  createNewText,
  usedCount,
  totalCount,
}: IProps) => {
  const { t } = useTranslation();
  const dashboardContexts: IDashboardContexts =
    useContext<IDashboardContexts>(DashboardContexts);
  const { message: messageApi } = App.useApp();
  // 项目信息是否展开
  const [projectInfoFold, setProjectInfoFold] = useState<boolean>(false);
  // 项目名称 
  const [projectName, setProjectName] = React.useState<string>("");
  // 画面尺寸
  const [aspectRatio, setAspectRatio] = React.useState<string>(DEFAULT_ASPECT_RATIO);
  // 画面风格
  const [storyBoardType, setStoryBoardType] = React.useState<number>(DEFAULT_STORY_BOARD_TYPE);
  // 原始故事文本
  const [originStoryText, setOriginStoryText] = React.useState<string>("");
  // 生成的扩写故事文本
  const [expandedStoryText, setExpandedStoryText] = React.useState<string>("");
  // 输入你的故事文本
  const [yourStoryText, setYourStoryText] = React.useState<string>("");
  // 上传剧本文件
  const [uploadScriptFile, setUploadScriptFile] =
    React.useState<UploadFile<any> | null>(null);
  // 扩写故事是否在创作中
  const [isExpandingStory, setIsExpandingStory] = useState<boolean>(false);
  // 创建新作品输入类型
  const [writeStoryInputType, setWriteStoryInputType] =
    React.useState<WriteStoryInputType>(WriteStoryInputType.AiExtension);

  const [isCreateNewModalOpen, setIsCreateNewModalOpen] = useState<boolean>(false);

  const [isCreateNewBtnDisabled, setIsCreateNewBtnDisabled] = useState<boolean>(true);
  useEffect(() => {
    const inputTypeConditionMaps = {
      [WriteStoryInputType.AiExtension]: expandedStoryText && !isExpandingStory,
      [WriteStoryInputType.InputYourStory]: yourStoryText,
      [WriteStoryInputType.UploadScript]: uploadScriptFile,
    };
    if (projectName && inputTypeConditionMaps[writeStoryInputType]) {
      setIsCreateNewBtnDisabled(false);
    } else {
      setIsCreateNewBtnDisabled(true);
    }
  }, [
    projectName,
    expandedStoryText,
    isExpandingStory,
    yourStoryText,
    uploadScriptFile,
    writeStoryInputType,
  ]);

  const showCreateNewModal = async () => {

    if (usedCount < totalCount) {
      const now = new Date();
      const formattedDate = `${t('createNew_default_Project_Name')}${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}_${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}`;
      setProjectName(formattedDate);
      setIsCreateNewModalOpen(true);
    } else {
      dashboardContexts.setIsShowUpgradeModal(true);
    }
  };

  const handleCreateNewModalOk = async () => {
    // 新增文件内容读取逻辑
    let fileContent = '';
    if (writeStoryInputType === WriteStoryInputType.UploadScript && uploadScriptFile) {
      const result = await FileReader.readFile(uploadScriptFile.originFileObj as File);
      if (!result.success) {
        messageApi.error(result.error);
        return;
      }
      fileContent = result.content;
      // console.log('fileContent:', fileContent);
    }

    //AiExtension 1 InputYourStory 2 UploadScript 3 scriptType
    const inputTypeParamsMaps = {
      [WriteStoryInputType.AiExtension]: {
        name: projectName,
        storyBoardType,
        content: expandedStoryText,
        scriptType: StoryScriptType.AI_GENERATED,
        aspectRatio
      },
      [WriteStoryInputType.InputYourStory]: {
        name: projectName,
        storyBoardType,
        content: yourStoryText,
        scriptType: StoryScriptType.MANUAL_INPUT,
        aspectRatio
      },
      [WriteStoryInputType.UploadScript]: {
        name: projectName,
        storyBoardType,
        content: fileContent,  // 改用读取后的文本内容
        scriptType: StoryScriptType.FILE_UPLOAD,
        aspectRatio
      },
    };
    const res = await projectApi.createProject(
      inputTypeParamsMaps[writeStoryInputType]
    );
    if (res.success && res.result?.code === 0) {
      if (res.result?.data) {
        // handleCreateNewModalCancel();
        window.location.href = `/project/${res.result.data.id}/roleview`;
        // 在新标签页打开
        // window.open(`/project/${res.result.data.id}/roleview`, '_blank');
        // setTimeout(() => {
        //   window.open(`/project/${res.result.data.id}/roleview`, '_blank');
        // }, 300);
      }
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };

  const handleCreateNewModalCancel = () => {
    // 关闭弹窗时重置数据
    setProjectName("");
    setWriteStoryInputType(WriteStoryInputType.AiExtension);
    setAspectRatio(DEFAULT_ASPECT_RATIO);
    setStoryBoardType(DEFAULT_STORY_BOARD_TYPE);
    setOriginStoryText("");
    setExpandedStoryText("");
    setYourStoryText("");
    setUploadScriptFile(null);
    setIsExpandingStory(false);
    setIsCreateNewModalOpen(false);
    setProjectInfoFold(false);
  };
  const value = React.useMemo(
    () => ({
      projectInfoFold,
      setProjectInfoFold,
      projectName,
      setProjectName,
      writeStoryInputType,
      setWriteStoryInputType,
      aspectRatio,
      setAspectRatio,
      storyBoardType,
      setStoryBoardType,
      expandedStoryText,
      setExpandedStoryText,
      yourStoryText,
      setYourStoryText,
      uploadScriptFile,
      setUploadScriptFile,
      isExpandingStory,
      setIsExpandingStory,
      originStoryText,
      setOriginStoryText,
    }),
    [
      projectInfoFold,
      projectName,
      writeStoryInputType,
      aspectRatio,
      storyBoardType,
      expandedStoryText,
      yourStoryText,
      uploadScriptFile,
      isExpandingStory,
      originStoryText,
    ]
  );
  return (
    <CreateNewContexts.Provider value={value as ICreateNewContexts}>
      <div>
        <CreateNewBtn
            onBtnClick={showCreateNewModal}
            buttonText={createNewText}
          />
        {createPortal(
          <ModalBase
            open={isCreateNewModalOpen}
            onOk={handleCreateNewModalOk}
            onCancel={handleCreateNewModalCancel}
            okText={t('createNew_createBtn')}
            cancelText={t('createNew_cancelBtn')}
            okButtonDisabled={isCreateNewBtnDisabled}
            width={848}
            height={734}
          >
            <CreateNewContent />
           </ModalBase>,
          document.body
        )}
      </div>
    </CreateNewContexts.Provider>
  );
};

export default CreateNewContainer;
