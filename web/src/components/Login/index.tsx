/**
 * 登录页面
 */
import React,{useEffect} from "react";
import { Button } from "antd";
import userHelper from "../../libs/user-helper";

import { IUserContexts, UserContexts } from "./../../contexts/user-contexts";
import { useTranslation } from "react-i18next";

const Login: React.FC = () => {
  const { t } = useTranslation();
  const userContexts: IUserContexts =React.useContext<IUserContexts>(UserContexts);

  useEffect(() => {
    const authInfo = userHelper.getLocalUserInfo();
    //1 判断是否登录
    const isLogin = authInfo?.state.isAuthenticated ?? false;
    if(isLogin){
      window.location.href = "/workspace";
    }else{
      userContexts.setIsShowLoginModal(true);
    }
  }, []);
  
  return (
    <div className="min-h-screen flex flex-col">
    </div>
  );
};

export default Login;
