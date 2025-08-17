/**
 * 主要人物
 */

import { Avatar, Button, Checkbox, Tooltip, App } from "antd";
import plusIcon from "./../../../../../assets/images/icons/plus.svg";
import { RoleItemObj } from "./../../../../libs/interfaces";
import { MainCharacter, StoryboardShot } from "./../../../../types/storyboard";

import React, { useContext } from "react";
import { createPortal } from "react-dom";
import { useTranslation } from "react-i18next";
import {
  DetailContexts,
  IDetailContexts,
} from "../DetailContainer/contexts/detail-contexts";
import ModalBase from "../ModalBase";
import mainFigureIcon from "./../../../../../assets/images/pages/boardView/main_figure_icon.svg";
import dashboardApi from "./../../../../api/dashboardApi";
import projectApi from "./../../../../api/projectApi";

interface IProps {
  boardItem: StoryboardShot;
  isEdit?: boolean;
  handleBoardItemChange?: (updatedBoardItem: StoryboardShot) => void;
}

const CellMainFigure: React.FC<IProps> = ({
  boardItem,
  isEdit = true,
  handleBoardItemChange = null
}: IProps) => {
  const { t } = useTranslation();
  const detailContexts: IDetailContexts = useContext<IDetailContexts>(DetailContexts);
  const [isModalOpen, setIsModalOpen] = React.useState<boolean>(false);

  const [roleList, setRoleList] = React.useState<RoleItemObj[]>([]);
  const getRoleList = async () => {
    const data = await projectApi.getRoleListById({
      projectId: detailContexts.projectItemObj?.id
    });
    if (data.success) {
      setRoleList(data.result?.data || []);
    }
  };
  const [mainFigureList, setMainFigureList] = React.useState<MainCharacter[]>( boardItem.main_characters );
  const [tempMainFigureList, setTempMainFigureList] = React.useState<MainCharacter[]>( boardItem.main_characters );

  const { message: messageApi } = App.useApp();

  React.useEffect(() => {
    setMainFigureList(boardItem.main_characters);
  }, [boardItem]);

  const updateCellValue = async () => {
    const res = await dashboardApi.storyboardUpdate({
      projectId: detailContexts.projectItemObj?.id,
      storyboardId: boardItem.shot_id,
      data: tempMainFigureList,
      updateType: "main_characters"
    });
    if (res.success && res.result?.code === 0) {
      // 调用回调函数，将更新后的数据传递给父组件
      if (handleBoardItemChange) {
        const updatedBoardItem = res.result.data;
        console.log('调用 handleBoardItemChange', updatedBoardItem);
        handleBoardItemChange(updatedBoardItem);
      }
    }else{
      messageApi.error(res.result?.msg);
    }
  };
  const showModal = async () => {
    setTempMainFigureList([...mainFigureList]); // 使用数组展开运算符正确复制数组
    setIsModalOpen(true);
    await getRoleList();
  };
  const handleModalCancel = async () => {
    setIsModalOpen(false);
  };

  const handleModalOk = async () => {
    handleModalCancel();
    // 检查是否有变化
    const hasChanges = !areArraysEqual(mainFigureList, tempMainFigureList);
    
    if (hasChanges) {
      await updateCellValue();
    }
  };


  // 辅助函数：比较两个数组是否相等
  const areArraysEqual = (arr1: MainCharacter[], arr2: MainCharacter[]): boolean => {
    if (arr1.length !== arr2.length) return false;
    
    // 创建一个映射来检查每个角色是否存在
    const roleMap = new Map<string, boolean>();
    
    arr1.forEach(character => {
      roleMap.set(character.role_id, true);
    });
    
    // 检查第二个数组中的每个角色是否都在第一个数组中
    for (const character of arr2) {
      if (!roleMap.has(character.role_id)) {
        return false;
      }
    }
    
    return true;
  };

  const handleSelectCharacter = (roleItem: RoleItemObj) => {
    setTempMainFigureList((prev) => {
      // 确保 prev 是数组
      const prevList = Array.isArray(prev) ? prev : [];
      
      if (
        prevList.some(
          (figure: MainCharacter) =>
            figure.role_id === roleItem.roleId
        )
      ) {
        return prevList.filter(
          (figure: MainCharacter) =>
            figure.role_id !== roleItem.roleId
        );
      } else {
        if (prevList.length >= 3) {
          messageApi.info(t("main_figure_max_character"));
          return prevList;
        }
        return [
          ...prevList,
          {
            role_name: roleItem.figureName,
            role_resource_url: roleItem.url,
            role_id: roleItem.roleId,
          },
        ];
      }
    });
  }

  return (
    <>
      <div 
        onClick={isEdit ? showModal : undefined}
        className="min-w-[168px]" // 添加最小宽度类
      >
        <Avatar.Group>
          {Array.isArray(mainFigureList) && mainFigureList.length > 0
            ? mainFigureList.map((figureItem: MainCharacter, index: number) => (
                <Tooltip
                  title={figureItem.role_name}
                  key={`main_figure_${figureItem.role_id}_${index}`}
                >
                  <Avatar
                    className="avatar-top-image"
                    src={figureItem.role_resource_url}
                    style={{ width: 40, height: 40 }}
                  />
                </Tooltip>
              ))
            : null}

          {isEdit ? (
            <Button
              shape="circle"
              type="dashed"
              size="large"
              icon={<img src={plusIcon} alt="" />}
              style={{ width: 40, height: 40 }}
            />
          ) : null}
        </Avatar.Group>
      </div>
      {createPortal(
        <ModalBase
          open={isModalOpen}
          onOk={handleModalOk}
          onCancel={handleModalCancel}
          okText={t("common_confirm")}
          cancelText={t("common_cancel")}
          width={612}
          height={undefined}
        >
          <div className="px-6 pt-6 pb-5">
            <div className="flex space-x-4">
              <div className="border h-12 w-12 rounded-lg flex items-center justify-center">
                <img src={mainFigureIcon} alt="" />
              </div>
              <div>
                <h2 className="text-gray-900 text-lg font-semibold">
                  {t("cell_main_figure_title")}
                </h2>
                <p className="text-slate-600 text-sm">
                  {t("cell_main_figure_subtitle")}
                </p>
              </div>
            </div>
          </div>
          <div className="flex px-6 border-b border-t">
            <div className="w-full">
              <div className="min-h-16 rounded-lg bg-background px-4 py-5 mt-6">
                <ul className="flex space-x-5">
                  {Array.isArray(tempMainFigureList) && tempMainFigureList.length > 0 ? (
                    tempMainFigureList.map(
                      (figureItem: MainCharacter, index: number) => (
                        <li
                          key={`figure_item_${figureItem.role_id}_${index}`}
                          className="flex flex-col items-center"
                        >
                          <div className="h-16 w-16 rounded-full overflow-hidden relative">
                            <img
                              className="w-full h-full object-contain bg-white"
                              src={figureItem.role_resource_url}
                              alt=""
                            />
                          </div>
                          <p className="mt-1 text-sm">{figureItem.role_name}</p>
                        </li>
                      )
                    )
                  ) : (
                    <span className="text-gray-500">
                      {t("cell_main_figure_no_main_character")}
                    </span>
                  )}
                </ul>
              </div>
              <div className="border flex-1 rounded-lg my-6">
                <h2 className="px-5 py-4 text-slate-700 text-sm font-medium">
                  {t("cell_main_figure_role_library")}
                </h2>
                <div className="sm:max-w-[564px] mx-4">
                  <div style={{maxHeight: 280 , overflowY: 'auto'}}>
                    <ul className="py-2 gap-2 flex">
                      {Array.isArray(roleList) && roleList.length > 0
                        ? roleList.map(
                            (roleItem: RoleItemObj, index: number) => (
                              <li
                                key={`role_item_${roleItem.roleId}_${index}`}
                                className="cursor-pointer transition-all duration-200 ease-in-out"
                                onClick={() => {
                                  handleSelectCharacter(roleItem);
                                }}
                              >
                                <div className="w-[122px] h-[220px] rounded-lg overflow-hidden relative bg-background">
                                  <div className="w-full h-full overflow-hidden">
                                    <img
                                      src={roleItem.url}
                                      className="w-full h-full object-contain transition duration-300 ease-in-out scale-110"
                                      alt=""
                                    />
                                  </div>
                                  { tempMainFigureList.some( (figure: MainCharacter) => figure.role_id === roleItem.roleId) ? (
                                    <div className="absolute inset-0 w-full h-full border-2 border-primary rounded-lg z-10 transition duration-300 ease-in-out opacity-100">
                                      <Checkbox
                                        checked={true}
                                        className={`absolute top-0.5 right-1 z-10`}
                                      />
                                    </div>
                                  ) : null}
                                </div>
                                <p className="font-semibold mt-2">
                                  {roleItem.figureName}
                                </p>
                              </li>
                            )
                          )
                        : null}
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </ModalBase>,
        document.body
      )}
    </>
  );
};

export default CellMainFigure;
