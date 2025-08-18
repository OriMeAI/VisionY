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

  const [currSegment, setCurrSegment] = React.useState<DetailTabType | null>(DetailTabType.VisualView);
  const [templateProjectItem, setTemplateProjectItem] = React.useState<ProjectItemObj | undefined>();

  useEffect(() => {
    authService.registerLogoutCallback(() => {
      userContexts.setIsAuthenticated(false);
      userContexts.setUserInfo(undefined);
    });
  }, [userContexts]);

  // 获取案例展示预览
  useEffect(() => {
    setCurrSegment(DetailTabType.VisualView);
    (async () => {
      // 从URL路径中获取ID参数，例如从/share/10011中提取10011
      const pathId = window.location.pathname.split("/").filter(Boolean)[1];
      // console.log('pathId', pathId)
      if (pathId) {
        const data = await shareApi.getTemplateById(pathId);
        // console.log('data', data)
        setTemplateProjectItem(data.result?.data);
      }
    })();
  }, []);
  return (
    <ShareDetailContainer
      currSegment={currSegment}
      setCurrSegment={setCurrSegment}
      projectName={templateProjectItem?.name || ''}
    >
      <ShareProjectContent
        currSegment={currSegment}
        templateProjectItem={templateProjectItem}
      />
    </ShareDetailContainer>
  );
};

export default Share;
