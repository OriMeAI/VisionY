/**
 * 角色页面
 */

import { Tour, TourProps } from "antd";
import React, { useRef, useState } from "react";
import { useTranslation } from "react-i18next";
import { useParams } from "react-router-dom";
import { RoleItemObj } from "./../../../../libs/interfaces";
import {
  IRoleViewContexts,
  RoleViewContexts,
} from "../../../../contexts/role-view-contexts";
import RoleViewContainer from "./../RoleViewContainer";

interface IProps {}

const RoleViewContent: React.FC<IProps> = ({}: IProps) => {
  const { t } = useTranslation();
  const { projectId } = useParams<{ projectId: string }>();
  // 当前选中的角色
  const [checkedRoleItemIndex, setCheckedRoleItemIndex] =
    React.useState<number>(0);
  const [roleList, setRoleList] = React.useState<RoleItemObj[]>([]);
  const [currProjectId, setCurrProjectId] = React.useState<string>(projectId);
  // 人脸参考图
  const [uploadExampleFigureImg, setUploadExampleFigureImg] =
    React.useState<string>("");

  const tourRef1 = useRef(null);
  const tourRef2 = useRef(null);
  const tourRef3 = useRef(null);

  const [isTourOpen, setIsTourOpen] = useState<boolean>(false);

  const steps: TourProps["steps"] = [
    // 隐藏面部参考图功能
    // {
    //   title: t("face_reference"),
    //   description: t("face_reference_description"),
    //   target: () => tourRef1.current,
    // },
    {
      title: t("regenerate_image"),
      description: t("regenerate_image_description"),
      target: () => tourRef2.current,
    },
    {
      title: t("generate_storyboard"),
      description: t("generate_storyboard_description"),
      target: () => tourRef3.current,
    },
  ];
  const value = React.useMemo(
    () => ({
      checkedRoleItemIndex,
      setCheckedRoleItemIndex,
      roleList,
      setRoleList,
      projectId: currProjectId,
      setProjectId: setCurrProjectId,
      uploadExampleFigureImg,
      setUploadExampleFigureImg,
      setIsTourOpen,
      tourRef1,
      tourRef2,
      tourRef3,
    }),
    [
      checkedRoleItemIndex,
      roleList,
      currProjectId,
      uploadExampleFigureImg,
      tourRef1,
      tourRef2,
      tourRef3
    ]
  );
  return (
    <RoleViewContexts.Provider value={value as IRoleViewContexts}>
      <RoleViewContainer />
      <Tour
        open={isTourOpen}
        onClose={() => setIsTourOpen(false)}
        steps={steps}
      />
    </RoleViewContexts.Provider>
  );
};

export default RoleViewContent;
