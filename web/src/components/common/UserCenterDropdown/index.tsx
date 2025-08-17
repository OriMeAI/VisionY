/**
 * 个人中心下拉框
 */
import {
  Avatar,
  Button,
  Dropdown,
  MenuProps,
  App,
  Tag,
} from "antd";
import * as React from "react";
import { useTranslation } from "react-i18next";
import avatarIcon from "./../../../../assets/images/layout/avatar.png";
import { IUserContexts, UserContexts } from "./../../../contexts/user-contexts";
import logoutIcon from "./../../../../assets/images/pages/usercenter/logout_icon.svg";
import authService from "./../../../libs/auth-service";
import userApi from "../../../api/userApi";

interface IProps {}

const UserCenterDropdown: React.FC<IProps> = ({}) => {
  const { t } = useTranslation();
  const userContexts: IUserContexts = React.useContext<IUserContexts>(UserContexts);
  const [dropdownOpen, setDropdownOpen] = React.useState<boolean>(false);
  const { message: messageApi } = App.useApp();

  const handleNavigation = (path: string) => {
    // 获取当前页面路径
    const currentPath = window.location.pathname;
    // 如果目标路径与当前路径相同，不进行跳转
    if (currentPath !== path) {
      window.open(path, '_blank');
    }
  };

  // console.log("userContexts",userContexts);

  const items: MenuProps["items"] = [
    {
      label: (
        <div className="flex flex-col rounded-lg space-y-4">
          <div className="flex flex-col items-center space-y-2">
            <Avatar
              shape="circle"
              style={{ width: 60, height: 60 }}
              src={ userContexts.userInfo?.avatar || avatarIcon }
            />
            <p className="flex items-center text-black truncate max-w-24">
              {userContexts.userInfo?.name}
            </p>
          </div>
          {/* <Divider className="my-2" /> */}
          <div className="flex flex-row justify-between h-6">
            <p className="flex items-center text-xs text-gray-500 mr-2">
              {t("membership_level")}
            </p>
            <Tag color={"purple"} className="flex items-center text-primary m-0">
              {userContexts.userInfo?.planName}
            </Tag>
          </div>
          {/* <Divider className="my-2" /> */}
          <div className="flex flex-row justify-between h-6">
            <p className="flex items-center text-xs text-gray-500  mr-2">
              {t("current_credits")}
            </p>
            <p className="flex items-center text-base font-bold text-indigo-900">
              {userContexts.userInfo?.credits.toLocaleString()}
            </p>
          </div>
        </div>
      ),
      key: "0",
      onClick: () => {
        handleNavigation("/usercenter");
      },
    },
    {
      type: "divider",
    },
    {
      // icon: <img src={logoutIcon} alt={t("logout")} />,
      label: <span>{t("terms_of_use")}</span>,
      key: "1",
      onClick: () => {
        handleNavigation("/termsofuse");
      },
    },
    {
      type: "divider",
    },
    {
      // icon: <img src={logoutIcon} alt={t("logout")} />,
      label: <span>{t("privacy_policy")}</span>,
      key: "2",
      onClick: () => {
        handleNavigation("/privacypolicy");
      },
    },
    {
      type: "divider",
    },
    {
      icon: <img src={logoutIcon} alt={t("logout")} />,
      label: <span>{t("logout")}</span>,
      key: "3",
      onClick: async () => {
        await authService.logout();
        messageApi.success(t("logout_success"));
      },
    },
  ];

  const handleDropdownVisibleChange = async(visible: boolean) => {
    setDropdownOpen(visible);
    if (visible && userContexts.isAuthenticated) {
      const data = await userApi.getUserInfo();
      if (data.result?.data) {
        userContexts.setUserInfo(data.result.data);
        console.log("handleDropdownVisibleChange");
      }
    }
  };

  const handleMenuClick: MenuProps["onClick"] = (e) => {
    if (e.key !== "0") {
      setDropdownOpen(false);
    }
  };

  return (
    <Dropdown
      menu={{
        items,
        style: { minWidth: 180 }, // 设置菜单最小宽度
        onClick: handleMenuClick,
      }}
      // trigger={["click"]}
      open={dropdownOpen}
      onOpenChange={handleDropdownVisibleChange}
    >
      {/* <Button
        type="text"
        size="large"
        icon={
          <Avatar
            shape="circle"
            style={{ width: 40, height: 40 }}
            src={ userContexts.userInfo?.avatar || avatarIcon }
          />
        }
        onClick={(e) => e.preventDefault()}
        className="!bg-transparent"
      /> */}
      <Button
        type="text"
        size="large"
        icon={
          <div className="flex items-center space-x-2">
            <div className="flex flex-col items-start">
              <span className="text-xs text-gray-500">{t("current_credits")}</span>
              <span className="text-sm font-bold text-indigo-900">
                {userContexts.userInfo?.credits?.toLocaleString() || '0'}
              </span>
            </div>
            <Avatar
              shape="circle"
              style={{ width: 40, height: 40 }}
              src={ userContexts.userInfo?.avatar || avatarIcon }
            />
          </div>
        }
        onClick={(e) => e.preventDefault()}
        className="!bg-transparent !w-auto"
        style={{ width: 'auto' }}
      />
    </Dropdown>
  );
};

export default UserCenterDropdown;
