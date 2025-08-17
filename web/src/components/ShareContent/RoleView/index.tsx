/**
 * 角色页面(预览不可编辑)
 */

import { RoleItemObj } from "./../../../libs/interfaces";

import React from "react";
import { useTranslation } from "react-i18next";
import {
  IShareRoleViewContexts,
  ShareRoleViewContexts,
} from "./contexts/share-role-view-contexts";
import RoleItemEdit from "./RoleItemEdit";
import RoleList from "./RoleList";
interface IProps {
  id: string;
  roleList: RoleItemObj[];
  setRoleList: React.Dispatch<React.SetStateAction<RoleItemObj[]>>;
  isNew?: boolean;
}

const RoleView: React.FC<IProps> = ({
  id,
  roleList,
  setRoleList,
  isNew,
}: IProps) => {
  const { t } = useTranslation();
  // 当前选中的角色
  const [checkedRoleItemIndex, setCheckedRoleItemIndex] =
    React.useState<number>(0);
  const [projectId, setProjectId] = React.useState<string>(id);
  // 人脸参考图
  const [uploadExampleFigureImg, setUploadExampleFigureImg] =
    React.useState<string>("");
  const value = React.useMemo(
    () => ({
      checkedRoleItemIndex,
      setCheckedRoleItemIndex,
      roleList,
      setRoleList,
      projectId,
      setProjectId,
      uploadExampleFigureImg,
      setUploadExampleFigureImg,
    }),
    [checkedRoleItemIndex, roleList, projectId, uploadExampleFigureImg]
  );
  return (
    <ShareRoleViewContexts.Provider value={value as IShareRoleViewContexts}>
      <div className="flex py-6 px-6 space-x-6 w-[1200px] h-[948px] mx-auto overflow-auto">
        <div className="w-[400px] p-6 rounded-lg flex-shrink-0 bg-white">
          <div className="w-full flex justify-between items-center mb-6">
            <h2 className="text-lg font-semibold">
              {t("roleView_title")}
            </h2>
          </div>
          <RoleList roleList={roleList} />
        </div>
        <RoleItemEdit />
      </div>
    </ShareRoleViewContexts.Provider>
  );
};

export default RoleView;
