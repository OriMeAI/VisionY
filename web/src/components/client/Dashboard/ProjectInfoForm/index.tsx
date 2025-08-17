/**
 * 创建新作品表单
 */

import { App } from "antd";
import { ArrowLeftOutlined } from "@ant-design/icons";
import { Button, Checkbox, Form, Input, Tooltip } from "antd";
import projectApi from "./../../../../api/projectApi";
import {
  CreateNewContexts,
  ICreateNewContexts,
} from "./../../../../contexts/create-new-contexts";
import { useTranslation } from "react-i18next";

import React, { useContext, useEffect } from "react";
import style from "./style.module.css";

//与服务器数据一致 
const IMAGE_SIZE_LIST = [
    {
      "id": 1,
      "label": "1:1",
      "value": "1:1",
      "className": "w-6 h-6",
      "tip": "1024x1024",
      "imgWidth": 1024,
      "imgHeight": 1024,
    },
    {
      "id": 2,
      "label": "16:9",
      "value": "16:9",
      "className": "w-6 h-3.5",
      "tip": "1344x768",
      "imgWidth": 1344,
      "imgHeight": 768,
    },
    {
      "id": 3,
      "label": "4:3",
      "value": "4:3",
      "className": "w-6 h-[18px]",
      "tip": "1152x896",
      "imgWidth": 1152,
      "imgHeight": 896,
    },
    {
      "id": 4,
      "label": "3:2",
      "value": "3:2",
      "className": "w-6 h-4",
      "tip": "1216x832",
      "imgWidth": 1216,
      "imgHeight": 832,
    },
    {
      "id": 5,
      "label": "2:3",
      "value": "2:3",
      "className": "w-4 h-6",       
      "tip": "832x1216",
      "imgWidth": 832,
      "imgHeight": 1216,
    },
    {
      "id": 6,
      "label": "3:4",
      "value": "3:4",
      "className": "w-[18px] h-6",
      "tip": "896x1152",
      "imgWidth": 896,
      "imgHeight": 1152,
    },
    {
      "id": 7,
      "label": "9:16",
      "value": "9:16",
      "className": "w-3.5 h-6",
      "tip": "768x1344",
      "imgWidth": 768,
      "imgHeight": 1344,
    },
]

interface IProps {
}

const ProjectInfoForm: React.FC<IProps> = ({
}: IProps) => {
  const { t } = useTranslation();
  const { message: messageApi } = App.useApp();
  const createNewContexts: ICreateNewContexts = useContext<ICreateNewContexts>(CreateNewContexts);

  const [styleDataList, setStyleDataList] = React.useState<any[]>([]);
  const [pictureSizeList, setPictureSizeList] = React.useState<any[]>(IMAGE_SIZE_LIST);

  const [showStylesList, setShowStylesList] = React.useState<any[]>([]);
  const [showSizesList, setShowSizesList] = React.useState<any[]>([]);

  const [isFoldBtnDisabled, setIsFoldBtnDisabled] = React.useState<boolean>(false);

  const [form] = Form.useForm();

  // 监听context中projectName的变化，更新表单值
  useEffect(() => {
    form.setFieldsValue({
      projectName: createNewContexts.projectName,
    });
  }, [createNewContexts.projectName]);

  // 项目名称变更
  const onNameChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    createNewContexts.setProjectName(e.target.value);
  };

  // 画面风格变更
  const onStoryBoardTypeChange = (type: number) => {
    createNewContexts.setStoryBoardType(type);
  };

  // 折叠项目信息
  const onFoldProjectInfo = () => {
    createNewContexts.setProjectInfoFold(false);
  };

  // 项目信息折叠时显示选中的画面尺寸和画面风格，否则显示全部
  useEffect(() => {
    if (createNewContexts.projectInfoFold) {
      setShowSizesList(
        pictureSizeList.filter(
          (item) => createNewContexts.aspectRatio === item.value
        )
      );
      setShowStylesList(
        styleDataList.filter(
          (item) => item.type === createNewContexts.storyBoardType
        )
      );
    } else {
      setShowSizesList(pictureSizeList);
      setShowStylesList(styleDataList);
    }
  }, [createNewContexts.projectInfoFold, styleDataList, pictureSizeList]);

  // 故事创作中时禁用折叠按钮
  useEffect(() => {
    setIsFoldBtnDisabled(createNewContexts.isExpandingStory);
  }, [createNewContexts.isExpandingStory]);

  // 获取项目风格列表
  useEffect(() => {
    (async () => {
      const data = await projectApi.getProjectStyles();
      if (data.success) {
        setStyleDataList(data.result?.data.styleDataList);
        // setPictureSizeList(data.result?.data.pictureSizeList);
      } else {
        messageApi.error(data.result.msg);
      }
    })();
  }, []);

  return (
    <div className={style.createNewFormWrapper}>
      <Form form={form} layout="vertical">
        <Form.Item
          label={<span className="font-semibold">{t("project_info_form_project_name")}</span>}
          name="projectName"
          rules={[{ required: true, message: t("project_info_form_please_enter_project_name") }]}
        >
          <Input
            size="large"
            autoComplete="off"
            onChange={onNameChange}
            placeholder={t("project_info_form_project_name_placeholder")}
          />
        </Form.Item>

        <Form.Item
          label={<span className="font-semibold">{t("project_info_form_picture_size")}</span>}
          name="pictureSize"
          rules={[{ required: true, message: "" }]}
          layout="vertical"
        >
          <div className={`grid ${createNewContexts.projectInfoFold ? "grid-cols-1 justify-items-start" : "grid-cols-[repeat(auto-fit,minmax(40px,1fr))]"} gap-2`}>
            {Array.isArray(showSizesList) && showSizesList.length > 0
              ? showSizesList.map(
                  (pictureSizeItem: any, pictureSizeIndex: number) => {
                    return (
                      <div
                        className={`position: relative; opacity: 1; transform: none; transform-origin: 0% 50% 0px; ${style.pictureSizeItem}`}
                        key={`picture_size_item_${pictureSizeItem.id}_${pictureSizeIndex}`}
                      >
                        <Tooltip placement="top" title={pictureSizeItem.tip}>
                          <Button
                            className={`h-full w-full border-none`}
                            onClick={() =>
                              createNewContexts.setAspectRatio(
                                pictureSizeItem.value
                              )
                            }
                          >
                            <div className="flex flex-col items-center">
                              <div className="h-6 flex items-center">
                                <p
                                  className={`border-2 border-[#d5dae1] rounded transition duration-300 ease-in-out ${
                                    pictureSizeItem.className
                                  } ${
                                    createNewContexts.aspectRatio ===
                                    pictureSizeItem.value
                                      ? "border-primary"
                                      : ""
                                  }`}
                                ></p>
                              </div>
                              <span
                                className={`text-[10px] font-semibold transition duration-300 ease-in-out leading-4 ${
                                  createNewContexts.aspectRatio ===
                                  pictureSizeItem.value
                                    ? "text-primary"
                                    : ""
                                }`}
                              >
                                {pictureSizeItem.label}
                              </span>
                            </div>
                          </Button>
                        </Tooltip>
                      </div>
                    );
                  }
                )
              : null}
          </div>
        </Form.Item>

        <Form.Item
          label={<span className="font-semibold">{t("project_info_form_picture_style")}</span>}
          name="storyBoardType"
          rules={[{ required: true, message: "" }]}
          layout="vertical"
        >
          <div style={{ height: '290px', overflowY: 'auto'}}>
            <ul className={`grid ${
              createNewContexts.projectInfoFold 
                ? "grid-cols-1" 
                : "grid-cols-2 sm:grid-cols-3 md:grid-cols-4"
            } auto-rows-max gap-3 pr-2.5`}>
              {Array.isArray(showStylesList) && showStylesList.length > 0
                ? showStylesList.map(
                    (projectStyleItem: any, projectStyleIndex: number) => {
                      return (
                        <li
                          className={`relative opacity-100 transform-none ${
                            createNewContexts.projectInfoFold ? "w-[63px]" : "w-full"
                          }`}
                          key={`picture_size_item_${projectStyleItem.id}_${projectStyleIndex}`}
                          onClick={() =>
                            onStoryBoardTypeChange(projectStyleItem.type)
                          }
                        >
                          <div className="relative w-full">
                            <div className="rounded-lg overflow-hidden">
                              <img
                                src={projectStyleItem?.image_url}
                                className="w-full h-[84px] object-cover rounded-lg transition duration-300 ease-in-out scale-100"
                                alt=""
                                // loading="lazy"
                              />
                              <div
                                className={`absolute inset-0 w-full h-[84px] border-${
                                  createNewContexts.storyBoardType ===
                                  projectStyleItem.type
                                    ? "2"
                                    : "none"
                                } border-primary rounded-lg z-10 transition duration-300 ease-in-out opacity-${
                                  createNewContexts.storyBoardType ===
                                  projectStyleItem.type
                                    ? "100"
                                    : "0"
                                }`}
                              >
                                {createNewContexts.storyBoardType ===
                                projectStyleItem.type ? (
                                  <Checkbox
                                    checked={true}
                                    className={`absolute top-1 right-1 z-1`}
                                  />
                                ) : null}
                              </div>
                            </div>
                            <div className="mt-1">
                              <h2 className="text-xs font-semibold">
                                {projectStyleItem?.name}
                              </h2>
                            </div>
                          </div>
                        </li>
                      );
                    }
                  )
                : null}
            </ul>
          </div>
        </Form.Item>
        {createNewContexts.projectInfoFold ? (
          <Button
            className={`absolute bottom-10 p-0 border-none hover:bg-transparent ${
              isFoldBtnDisabled ? "bg-transparent" : ""
            }`}
            onClick={onFoldProjectInfo}
            icon={<ArrowLeftOutlined />}
            disabled={isFoldBtnDisabled}
          >
            <span>{t("project_info_form_back_to_select")}</span>
          </Button>
        ) : null}
      </Form>
    </div>
  );
};

export default ProjectInfoForm;
