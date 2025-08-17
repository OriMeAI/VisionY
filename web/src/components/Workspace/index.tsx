/**
 * 工作台页面
 */
// import { useMediaQuery } from "@react-hook/media-query";
import { Button, Layout, Menu, Tooltip } from "antd";
import { useEffect } from "react";
import { useTranslation } from "react-i18next";
import authService from "../../libs/auth-service";

// import { FaDiscord } from 'react-icons/fa';
import LanguageDropdown from "../common/LanguageDropdown";
import UserCenterDropdown from "../common/UserCenterDropdown";
import cubeIcon from "./../../../assets/images/pages/workspace/cube_icon.svg";
import visualStroyLogo from "./../../../home/static/assets/visiony_logo_transparent_180.svg";
import { IUserContexts, UserContexts } from "./../../contexts/user-contexts";
import dashboardApi from "./.././../api/dashboardApi";
import {
  IModalContexts,
  ModalContexts,
} from "./.././../contexts/modal-contexts";
import { ProjectBenefitType } from "./.././../libs/interfaces";
import style from "./style.module.css";
import React from "react";

import ProjectList from "./ProjectList";
import TemplateList from "./TemplateList";


const { Sider, Content } = Layout;

const Workspace: React.FC = () => {
  const { t } = useTranslation();

  // const startYear = 2023;
  const currentYear = new Date().getFullYear();
  // const yearDisplay = startYear === currentYear ? currentYear : `${startYear}-${currentYear}`;

  const userContexts: IUserContexts =React.useContext<IUserContexts>(UserContexts);
  useEffect(() => {
    authService.registerLogoutCallback(() => {
      userContexts.setIsAuthenticated(false);
      userContexts.setUserInfo(undefined);
    });
  }, [userContexts]);  

  const modalContexts: IModalContexts = React.useContext<IModalContexts>(ModalContexts);
  const [projectBenefit, setProjectBenefit] = React.useState<ProjectBenefitType>();
  const refreshProjectBenefit = async () => {
    const data = await dashboardApi.getProjectBenefit();
    if(!data.success) return;
    setProjectBenefit(data.result?.data);
  };
  // 获取项目数量
  useEffect(() => {
    (async () => {
      if (userContexts.isAuthenticated) {
        await refreshProjectBenefit();
      }
    })();
  }, [userContexts.isAuthenticated]);
  const showCreditsModal = () => {
    modalContexts.setIsShowCreditsModal(true);
  };

  const showMembershipModal = () => {
    modalContexts.setIsShowMembershipModal(true);
  };

  const showLoginModal = () => {
    userContexts.setIsShowLoginModal(true);
  };
  useEffect(() => {
    // 页面加载完毕后折叠侧边栏
    // setCollapsed(true);
  }, []);
  return (
    <Layout className={`h-screen overflow-hidden ${style.workspaceWrapper}`}>
      <Sider
        theme="light"
        trigger={null}
        collapsible
        collapsed={true}
        className= "bg-background"
        width={280}
        style={{
          width: 80,
          maxWidth: 80,
          minWidth: 80,
          borderRight: "none",
          height: "100%",
        }}
      >
        <div className="flex flex-col h-full justify-between px-6 py-6 space-y-6">
          <Tooltip title={t("back_to_home")} placement="right">
            <div
              onClick={() => {
                window.open("/", '_blank');
              }}
              className="flex items-center justify-center gap-2.5 cursor-pointer w-full"
            >
              <img className="w-8 h-8" src={visualStroyLogo} alt="logo" />
              {/* <span
                className={`text-2xl font-bold text-center ${collapsed ? 'hidden' : 'block'}`}
              >
                VisionY
              </span> */}
            </div>
          </Tooltip>

          <Menu
            className="flex-1 flex flex-col gap-2"
            style={{
              width: "100%",
              background: "transparent",
              borderInlineEnd: "none",
            }}
            mode="inline"
            defaultSelectedKeys={["1"]}
            items={[
              {
                key: "1",
                icon: (
                  <div className="w-6 h-6">
                    <img src={cubeIcon} />
                  </div>
                ),
                label: (
                  <span className="font-semibold text-base">
                    {t("workspace")}
                  </span>
                )
              },
            ]}
          />
          <div aria-hidden="true" style={{ display: "none" }}></div>
          <div
            className="space-y-6 mt-4 flex flex-col items-center"
          >
            <div
              className="flex gap-5 flex-col"
            >
              <Button
                type="text"
                className="group text-brand-text transition-colors duration-300"
                icon={
                  <svg className="w-5 h-5 group-hover:text-primary" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <title>Discord</title>
                    <path d="M20.317 4.3698a19.7913 19.7913 0 00-4.8851-1.5152.0741.0741 0 00-.0785.0371c-.211.3753-.4404.8648-.6083 1.2495-1.8447-.2762-3.68-.2762-5.4868 0-.1679-.3847-.3973-.8742-.6083-1.2495a.0741.0741 0 00-.0785-.0371 19.7363 19.7363 0 00-4.8851 1.5152.0699.0699 0 00-.0321.0277C.5334 9.0458-.319 13.5779.0992 18.0578a.0824.0824 0 00.0312.0561c2.0528 1.5076 4.0413 2.4228 5.9929 3.0294a.0777.0777 0 00.0842-.0276c.4616-.6304.8731-1.2952 1.227-1.9942a.076.076 0 00-.0416-.1057c-.6528-.2476-1.278-.5495-1.8722-.8923a.077.077 0 01-.0076-.1277c.1258-.0941.2517-.1923.3718-.2914a.0743.0743 0 01.0776-.0106c3.9278 1.7933 8.18 1.7933 12.0614 0a.0743.0743 0 01.0776.0106c.1201.0991.246.1973.3718.2914a.077.077 0 01-.0076.1277c-.5942.3428-1.2194.6447-1.8722.8923a.076.076 0 00-.0416.1057c.3539.699.7654 1.3638 1.227 1.9942a.0777.0777 0 00.0842.0276c1.9516-.6067 3.9401-1.5219 5.9929-3.0294a.0824.0824 0 00.0312-.0561c.5004-4.3802-.3265-8.9762-2.6054-13.6602a.0699.0699 0 00-.0321-.0277zM8.0201 15.3312c-.7804 0-1.4162-.8163-1.4162-1.8229 0-1.0066.6358-1.823 1.4162-1.823.7804 0 1.4161.8163 1.4161 1.823 0 1.0066-.6357 1.8229-1.4161 1.8229zm7.9748 0c-.7804 0-1.4162-.8163-1.4162-1.8229 0-1.0066.6358-1.823 1.4162-1.823.7804 0 1.4162.8163 1.4162 1.823 0 1.0066-.6358 1.8229-1.4162 1.8229Z"/>
                  </svg>
                }
                onClick={() => window.open('https://discord.gg/CBaZPDjWEn', '_blank')}
              />
              <Button
                type="text"
                className="group text-brand-text transition-colors duration-300"
                icon={
                  <svg className="w-5 h-5 group-hover:text-primary" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <title>X/Twitter</title>
                    <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
                  </svg>
                }
                onClick={() => window.open('https://www.x.com/VisionY_AI', '_blank')}
              />
              <Button
                type="text"
                className="group text-brand-text transition-colors duration-300"
                icon={
                  <svg className="w-5 h-5 group-hover:text-primary" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <title>Youtube</title>
                    <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
                  </svg>
                }
                onClick={() => window.open('https://www.youtube.com/@VisionY_AI', '_blank')}
              />
              {/* <Button
                type="text"
                className="group text-brand-text transition-colors duration-300"
                icon={
                  <svg className="w-5 h-5 group-hover:text-primary" fill="currentColor" viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg">
                    <title>Tiktok</title>
                    <path d="M448,209.91a210.06,210.06,0,0,1-122.77-39.25V349.38A162.55,162.55,0,1,1,185,188.31V278.2a74.62,74.62,0,1,0,52.23,71.18V0l88,0a121.18,121.18,0,0,0,1.86,22.17h0A122.18,122.18,0,0,0,381,102.39a121.43,121.43,0,0,0,67,20.14Z"/>
                  </svg>
                }
                onClick={() => window.open('https://www.tiktok.com/@visiony_ai', '_blank')}
              /> */}
              <Button
                type="text"
                className="group text-brand-text transition-colors duration-300"
                icon={
                  <svg className="w-5 h-5 group-hover:text-primary" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <title>Instagram</title>
                    <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/>
                  </svg>
                }
                onClick={() => window.open('https://www.instagram.com/visiony_ai', '_blank')}
              />
            </div>
          </div>
        </div>
      </Sider>
      <Layout className="min-h-screen bg-white">
        <Content>
          <div className="flex flex-col">
            <div className="relative h-12 w-full flex flex-row justify-between items-center space-x-6 px-6 my-3">
              <div className="text-xl font-bold text-gray-800 max-[936px]:invisible max-[936px]:w-0 max-[936px]:overflow-hidden">{t("workspace")}</div>
              <div className="flex flex-row items-center space-x-6">
                <Button
                  type="text"
                  size="large"
                  className="max-sm:hidden" // 在中等屏幕以下隐藏
                  onClick={showMembershipModal}
                >
                  <span>{t("subscribe_membership")}</span>
                </Button>
                <Button
                  type="text"
                  size="large"
                  className="max-sm:hidden" // 在中等屏幕以下隐藏
                  onClick={showCreditsModal}
                >
                  <span>{t("purchase_generate_credits")}</span>
                </Button>
                <LanguageDropdown />
                {userContexts.isAuthenticated ? (
                  <UserCenterDropdown />
                ) : (
                  <Button
                    onClick={showLoginModal}
                    type="primary"
                    size="large"
                    variant="solid"
                  >
                    <span>{t("login")}</span>
                  </Button>
                )}
              </div>
            </div>
            <div className="h-[calc(100vh-72px)] flex flex-col justify-between overflow-y-auto">
              <div className="px-6">
                <TemplateList
                  usedCount={projectBenefit?.usedCount}
                  totalCount={projectBenefit?.totalCount}
                />
                <ProjectList
                  usedCount={projectBenefit?.usedCount}
                  totalCount={projectBenefit?.totalCount}
                  refreshProjectBenefit={refreshProjectBenefit}
                />
              </div>
              <div className="mx-auto py-2 flex flex-wrap flex-row justify-center">
                <p className="text-neutral-400 text-xs text-center">
                  © {currentYear} Orime. {t('all_rights_reserved')}
                </p>
              </div>
            </div>
          </div>
        </Content>
      </Layout>
    </Layout>
  );
};

export default Workspace;
