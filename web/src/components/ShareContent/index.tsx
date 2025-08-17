/**
 * 预览页面（不可编辑）
 */
import React, { useEffect } from "react";
import { useTranslation } from "react-i18next";
import { useParams } from "react-router-dom";
import authService from "../../libs/auth-service";
import ShareProjectContent from "../Share/ShareProjectContent";
import ShareDetailContainer from "../Share/ShareDetailContainer";
import shareApi from "./../../api/shareApi";
import { IUserContexts, UserContexts } from "./../../contexts/user-contexts";
import { DetailTabType } from "./../../libs/enums";
import { ProjectItemObj } from "./../../libs/interfaces";

const Share: React.FC = () => {
  const { t } = useTranslation();
  const userContexts: IUserContexts =
    React.useContext<IUserContexts>(UserContexts);

  // 从URL路径中获取ID参数，例如从/share/10011中提取10011
  const { id } = useParams<{ id: string }>();
  const pathId = window.location.pathname.split("/").filter(Boolean)[1] || id;
  const [currSegment, setCurrSegment] = React.useState<DetailTabType | null>(DetailTabType.VisualView);
  const [templateProjectItem, setTemplateProjectItem] = React.useState<ProjectItemObj | undefined>();
  // Initialize from sessionStorage on mount
  // useEffect(() => {
  //   if (templateProjectItem?.id) {
  //     const storedSegment = sessionStorage.getItem(
  //       `selectedTab_${templateProjectItem.id}`
  //     );
  //     if (storedSegment) {
  //       const tabValue = parseInt(storedSegment, 10);
  //       if (!isNaN(tabValue) && tabValue in DetailTabType) {
  //         setCurrSegment(tabValue as DetailTabType);
  //       }
  //     } else {
  //       setCurrSegment(DetailTabType.FilmTable);
  //     }
  //   }
  // }, [templateProjectItem?.id]);

  useEffect(() => {
    authService.registerLogoutCallback(() => {
      userContexts.setIsAuthenticated(false);
      userContexts.setUserInfo(undefined);
    });
  }, [userContexts]);

  // 获取案例展示预览
  useEffect(() => {
    (async () => {
      const data = await shareApi.getTemplateById(pathId);
      setTemplateProjectItem(data.result?.data);
    })();
  }, [pathId]);
  return (
    <ShareDetailContainer
      currSegment={currSegment}
      setCurrSegment={setCurrSegment}
      projectId={id}
      templateProjectItem={templateProjectItem}
    >
      <ShareProjectContent
        currSegment={currSegment}
        templateProjectItem={templateProjectItem}
      />
    </ShareDetailContainer>
  );
};

export default Share;
