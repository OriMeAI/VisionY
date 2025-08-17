/**
 * 用户中心页面
 */
import React,{useEffect} from "react";
import { Button } from "antd";
// import Footer from "../common/Layout/Footer";
// import Header from "../common/Layout/Header";
import { IUserContexts, UserContexts } from "./../../contexts/user-contexts";
import { useTranslation } from "react-i18next";
import authService from "../../libs/auth-service";

import NewFooter from "../common/Layout/NewFooter";
import NewHeader from "../common/Layout/NewHeader";

import Content from "./Content";

const UserCenter: React.FC = () => {
  const { t } = useTranslation();
  const userContexts: IUserContexts =React.useContext<IUserContexts>(UserContexts);

  useEffect(() => {
    authService.registerLogoutCallback(() => {
      userContexts.setIsAuthenticated(false);
      userContexts.setUserInfo(undefined);
      window.location.href = "/workspace";
    });
  }, [userContexts]);  
  
  return (
    <div className="min-h-screen flex flex-col">
      {/* 固定在顶部的 Header */}
      <NewHeader/>

      {/* 内容区域，带有顶部和底部的 padding 以避免被 header 和 footer 遮挡 */}
      <div className="flex-1 flex flex-col">
        {userContexts.isAuthenticated ? <Content /> : (
          <div className="flex-1 flex flex-col flex-nowrap space-y-4 items-center justify-center">
            <img
              className="w-12 h-12"
              src="data:image/svg+xml,%3csvg%20width='48'%20height='48'%20viewBox='0%200%2048%2048'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M17.6875%2037.5617C4.78127%2037.5617%205.07528%2037.5617%2010.453%2025.1445V33.0578'%20stroke='%23141414'%20stroke-width='1.4'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3cpath%20d='M38.9487%2027.3549C36.5334%2027.2644%2023.4524%2027.1531%2022.5058%2028.0999C21.1403%2029.4658%2017.7623%2038.8949%2019.1148%2040.6985C28.3054%2040.8735%2035.2554%2041.0607%2036.6148%2040.5168C37.3164%2040.2361%2037.8767%2039.4291%2038.1892%2038.6998C38.4366%2038.1221%2041.0352%2029.3172%2041.0352%2029.0691'%20stroke='%23101828'%20stroke-width='1.4'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3cpath%20d='M18.668%2040.6178C16.7249%2039.8835%2014.6876%2039.238%2012.8169%2038.2773'%20stroke='%23141414'%20stroke-width='1.4'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3cpath%20d='M13.1136%2014.9848C10.0788%2024.9549%2023.6564%2029.1776%2027.2521%2019.1531C29.2013%2013.7187%2022.6433%205.7197%2015.9211%2011.7235'%20stroke='%23141414'%20stroke-width='1.4'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3cpath%20d='M22.5261%2018.9332C22.6504%2018.5972%2022.7391%2018.4002%2022.8086%2018.0742'%20stroke='%23141414'%20stroke-width='1.4'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3cpath%20d='M19.7188%2018.8772C19.8492%2018.6094%2019.8708%2018.3692%2019.9219%2018.0664'%20stroke='%23141414'%20stroke-width='1.4'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3c/svg%3e"
              alt="laptop_work"
            />
            <div className="text-center">
              <h2 className="text-lg font-semibold">{t("not_logged_in")}</h2>
              <p className="text-sm text-gray-500">
                {t("register_login_to_experience")}
              </p>
            </div>

            <Button
              type="primary"
              variant="solid"
              size="large"
              onClick={() => userContexts.setIsShowLoginModal(true)}
            >
              <span>{t("login_now")}</span>
            </Button>
          </div>
        )}
      </div>

      {/* 固定在底部的 Footer */}
      <NewFooter/>
    </div>
  );
};

export default UserCenter;