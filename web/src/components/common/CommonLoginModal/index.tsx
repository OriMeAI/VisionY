/**
 * 登录按钮及弹窗
 */
import React, {useEffect,useState,useContext} from "react";
import { App } from "antd"; // Added Divider
import { createPortal } from "react-dom";
import { useTranslation } from "react-i18next";
import ModalBase from "../../client/Common/ModalBase";
import CommonLoginForm from "./CommonLoginForm";
import userHelper from "./../../../libs/user-helper";
import { IUserContexts, UserContexts } from "./../../../contexts/user-contexts";
import { trackEvent, setUserId } from './../../../libs/amplitude';


interface IProps {}

const CommonLoginModal: React.FC<IProps> = ({}) => {
  const userContexts: IUserContexts = useContext<IUserContexts>(UserContexts);
  const { t } = useTranslation();
  const { message: messageApi } = App.useApp();

  const [isShowLoginModal, setIsShowLoginModal] = useState(false);

  useEffect(() => {
    setIsShowLoginModal(userContexts.isShowLoginModal);
  }, [userContexts.isShowLoginModal]);

  //处理前进或者后退导致的loading显示问题
  useEffect(() => {
    const handlePopState = (event: PopStateEvent) => {
      userContexts.setIsShowLoginModelLoading(false);
    };

    window.addEventListener('popstate', handlePopState);
    
    return () => {
      window.removeEventListener('popstate', handlePopState);
    };
  }, []);

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const access_token = params.get("access_token");
    const user_id = params.get("user_id");
  
    if (access_token) {     
        setUserId(user_id);
        
        trackEvent('user_login', {
          login_method: 'google'
        });
      
        // 删除 token 参数
        params.delete("access_token");
        params.delete("user_id");
    
        // 构造新的 URL（如果没有参数就不要加 ?）
        const newQuery = params.toString();
        const newUrl = newQuery ? `${window.location.pathname}?${newQuery}`: window.location.pathname;

        window.history.replaceState({}, "", newUrl);
        
        if (access_token === "googl_login_fail") {
            messageApi.error(t("googl_login_failed"));
        } else {
          userHelper.setLocalUserInfo({
            state: {
                isAuthenticated: true,
                token: access_token,
            },
            version: 0,
          });
          userContexts.setIsShowLoginModal(false);

          // 登录成功后，根据当前路径判断是否需要重定向
          if(window.location.pathname === "/login"){
            window.location.href = "/workspace";
          }else{
            window.location.reload();
          }
        }
    }
  }, []);

  const handleModalCancel = async () => {
    userContexts.setIsShowLoginModal(false);
  };

  const handleModalOk = async () => {
    handleModalCancel();
  };
  return (
    <>
      {createPortal(
        <ModalBase
          open={isShowLoginModal}
          onOk={handleModalOk}
          onCancel={handleModalCancel}
          okText={t("loginProvider_confirm")}
          cancelText={t("loginProvider_cancel")}
          width={400}
          height={undefined}//{630}
          showFooter={false}
          footer={<div style={{ height: '0px' }}></div>}
        //   wrapperClassName={style.commonLoginModal}
          destroyOnClose={false}
        >
        <div className="bg-white/60 backdrop-blur-sm rounded-lg p-6 w-full h-full">
            <CommonLoginForm
              onLoginSuccess={() => {
                  handleModalCancel();
                  window.location.reload();
              }}
            />
        </div>
        </ModalBase>,
        document.body
      )}
    </>
  );
};

export default CommonLoginModal;
