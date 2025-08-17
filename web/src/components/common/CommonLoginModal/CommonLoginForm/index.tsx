/**
 * 登录表单
 */
import { Button, Form, Input, App, Divider } from "antd"; // Added Divider
import * as React from "react";
import loginApi from "./../../../../api/loginApi";
import { IUserContexts, UserContexts } from "./../../../../contexts/user-contexts";
import userHelper from "./../../../../libs/user-helper";
import { useTranslation } from "react-i18next";
import VisionYLogo from "../../../../../home/static/assets/visiony_logo_transparent_180.svg";
// import GoogleLoginButton from "../GoogleLoginButton"; // Import GoogleLoginButton
import GoogleLoginPage from "../GoogleLoginPage";
import { trackEvent, setUserId } from './../../../../libs/amplitude';

interface IProps {
  onLoginSuccess?: () => void;
}

const CommonLoginForm: React.FC<IProps> = ({ 
  onLoginSuccess 
}) => {
  const { t } = useTranslation();
  const { message: messageApi } = App.useApp();
  const userContexts: IUserContexts =
    React.useContext<IUserContexts>(UserContexts);
  const [form] = Form.useForm();

  const [emailValid, setEmailValid] = React.useState<boolean>(false);
  const [email, setEmail] = React.useState<string>("");
  const [emailCode, setEmailCode] = React.useState<string>("");
  const [emailTimeCount, setEmailTimeCount] = React.useState<number>(60);

  // 在组件顶部添加一个 ref
  const currentTimeCount = React.useRef(60);

  const sendEmailInterval = React.useRef<NodeJS.Timeout | null>(null);

  const onEmailChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const emailRegex =
      /^(?:(?:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*)|(?:"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*"))@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)$/;
    if (e.target.value && emailRegex.test(e.target.value)) {
      setEmailValid(true);
    } else {
      setEmailValid(false);
    }
    setEmail(e.target.value);
  };

  const sendEmailCode = async () => {
    // 同时更新 ref 和状态
    currentTimeCount.current = 59;
    setEmailTimeCount(59);

    sendEmailInterval.current = setInterval(() => {
      currentTimeCount.current -= 1;
      setEmailTimeCount(currentTimeCount.current);
      
      if (currentTimeCount.current === 0) {
        clearInterval(sendEmailInterval.current!);
        currentTimeCount.current = 60;
        setEmailTimeCount(60);
      }
    }, 1000);

    const res = await loginApi.sendEmailCode({
      email: email
    });
    if (res.success && res.result?.code === 0) {
      messageApi.success(t("verification_code_sent"));
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };

  const emailLogin = async () => {
    const res = await loginApi.emailLogin({
      code: emailCode,
      email: email,
    });
    if (res.success && res.result?.code === 0) {

        const userID = res.result?.data?.userID
        const token = res.result?.data?.accessToken
        setUserId(userID);
        
        trackEvent('user_login', {
          login_method: 'email'
        });

      userHelper.setLocalUserInfo({
        state: {
          isAuthenticated: true,
          token: token,
        },
        version: 0,
      });
      onLoginSuccess && onLoginSuccess();
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };

  const onLoginBtnClick = async () => { 
    if (
      !/^(?:(?:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*)|(?:"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*"))@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)$/.test(
        email
      )
    ) {
      messageApi.error(t("please_enter_correct_email_address"));
      return;
    }
    if (!/^\d{6}$/.test(emailCode)) {
      messageApi.error(t("please_enter_correct_verification_code"));
      return;
    }
    await emailLogin();
  };

  const validateEmail = (_: any, value: string) => {
    const emailRegex =
      /^(?:(?:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*)|(?:"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*"))@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)$/;
    if (!value || !emailRegex.test(value)) {
      return Promise.reject(new Error(t("please_enter_correct_email_address")));
    }
    return Promise.resolve();
  };

  const validateCode = (_: any, value: string) => {
    const codeRegex = /^\d{6}$/;
    if (!value || !codeRegex.test(value)) {
      return Promise.reject(
        new Error(t("please_enter_correct_verification_code"))
      );
    }
    return Promise.resolve();
  };

  return (
    <div className="mx-auto flex flex-col justify-center space-y-6 sm:w-[310px]">
      <div
        onClick={() => {
          window.open("/", '_blank');
        }}
        className="flex items-center justify-center gap-2.5 cursor-pointer w-full"
      >
        <img className="w-10 h-10" src={VisionYLogo} alt="logo" />
      </div>
      <div className="flex flex-col">
        <div className="text-2xl font-semibold tracking-tight flex text-center justify-center relative">        
          {t("welcome_to_visiony")}
          {/* <div className="w-[43px] h-[22px] px-2 py-0.5 bg-purple-50 rounded-full border border-purple-200 justify-start items-center flex ml-2 -mt-1">
            <div className="text-center text-violet-500 text-xs font-medium leading-[18px]">
              Alpha
            </div>
          </div> */}
        </div>
        <div className="text-gray-500 text-xs flex text-center justify-center mt-2 whitespace-normal">
          { t("unregistered_user_login")}
        </div>
        {/* <div className="text-gray-500 text-xs truncate  flex text-center justify-center mt-2">
          { t("unregistered_user_login")}
        </div> */}
      </div>

      <div className="grid gap-6">
        <GoogleLoginPage />
        <Divider>
          <span className="text-xs text-gray-500">OR</span>
        </Divider>
        <Form
          form={form} 
          onFinish={(values) => {
            onLoginBtnClick(); 
          }}
        >
          <Form.Item
            label={<span className="font-semibold">{t("email_address")}</span>}
            name="email"
            layout="vertical"
            style={{ height: 68 }}
            rules={[{ validator: validateEmail }]}
          >
            <Input
              onChange={onEmailChange}
              size="large"
              variant="outlined"
              className="mt-1.5"
              placeholder={t("enter_your_email")}
            />
          </Form.Item>
          <Form.Item
            label={
              <span className="font-semibold">{t("verification_code")}</span>
            }
            name="emailCode"
            layout="vertical"
            style={{ height: 68 }}
            rules={[{ validator: validateCode }]}
          >
            <Input
              size="large"
              className="mt-1.5"
              onChange={(e) => setEmailCode(e.target.value)}
              autoComplete="off"
              suffix={
                <Button
                  type="text"
                  size="small"
                  variant="link"
                  onClick={sendEmailCode}
                  disabled={!emailValid || currentTimeCount.current < 60}
                >
                  <span>
                    {emailTimeCount  < 60
                      ? t("resend_email_verification_code", {
                          count: emailTimeCount ,
                        })
                      : t("get_email_verification_code")}
                  </span>
                </Button>
              }
            />
          </Form.Item>
          <Form.Item layout="vertical" style={{ height: 32 }}>
            <div>
              {t("agree_to_terms")}
              <a href="/termsofuse" target="_blank" className="text-primary">
                《{t("terms_of_use")}》
              </a>
              {t("and")}
              <a href="/privacypolicy" target="_blank" className="text-primary">
                《{t("privacy_policy")}》
              </a>
            </div>
          </Form.Item>
          <Form.Item layout="vertical">
            <div className="mt-4">
              <Button
                type="primary"
                size="large"
                variant="solid"
                className="w-full"
                htmlType="submit"
              >
                <span>{t("login")}</span>
              </Button>
            </div>
          </Form.Item>
        </Form>
      </div>
    </div>
  );
};

export default CommonLoginForm;