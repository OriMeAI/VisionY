/**
 * 通用头部组件
 */
import { Button } from "antd";
import * as React from "react";
import { useTranslation } from "react-i18next";
import enterIcon from "./../../../../../assets/images/layout/enter_icon.svg";
import enterIconLight from "./../../../../../assets/images/layout/enter_icon_light.svg";
import {
  LOGO_BASE64_SRC_DARK,
  LOGO_BASE64_SRC_LIGHT,
} from "../../../../libs/global-config";
import LanguageDropdown from "../../LanguageDropdown";
import style from "./style.module.css";
interface IProps {
  theme?: "dark" | "light";
}

const Header: React.FC<IProps> = ({ theme = "dark" }) => {
  const { t } = useTranslation();
  return (
    <div className="w-full">
      <div className={`${style.container} mx-auto`}>
        <header className="relative">
          <div className="h-[86px]">
            <div className="flex items-center h-full">
              <div
                onClick={() => {
                  if (window.location.pathname !== "/") {
                    window.open("/", "_blank");
                  }
                }}
                className={`flex items-center justify-center gap-2.5 ml-4 lg:ml-0 ${
                  window.location.pathname !== "/" ? "cursor-pointer" : ""
                }`}
              >
                <img
                  src={
                    theme === "dark"
                      ? LOGO_BASE64_SRC_DARK
                      : LOGO_BASE64_SRC_LIGHT
                  }
                  width="40"
                  height="40"
                  alt="bg"
                />
              <span
                className="text-xl font-bold text-center hidden md:block"
                style={{
                  color: theme === "dark"? "#fff" : "#000",
                }}
              >
                VisionY
              </span>
              </div>

              <div className="ml-auto flex items-center space-x-6">
                <LanguageDropdown />
                <div className="flex items-center lg:flex-1 lg:items-center lg:justify-end lg:space-x-6 ml-2">
                  <Button
                    style={{
                      color: theme === "dark" ? "#fff" : "#7E2FFF",
                      borderColor: theme === "dark" ? "#fff" : "#7E2FFF",
                    }}
                    size="large"
                    ghost
                    className="rounded-lg"
                    onClick={() => {
                      if (window.location.pathname !== "/workspace") {
                        window.open("/workspace", "_blank");
                      }
                    }}
                  >
                    <div className="w-4 h-4 mr-2">
                      <img
                        src={theme === "dark" ? enterIcon : enterIconLight}
                      />
                    </div>
                    <span>{t("enter_workspace")}</span>
                  </Button>
                </div>
              </div>
            </div>
          </div>
        </header>
      </div>
    </div>
  );
};

export default Header;
