import { Button } from "antd";
import React, { useEffect } from "react";
import { useTranslation } from "react-i18next";
import image404 from "./../../../assets/images/pages/404/404-DkMt8Rdf.png";
import { ERROR_MSG_404, LANGUAGE } from "./../../libs/global-config";

const NotFound: React.FC = () => {
  const { t, i18n } = useTranslation();
  const msg = localStorage.getItem(ERROR_MSG_404);
  localStorage.setItem(ERROR_MSG_404, "");

  useEffect(() => {
    const language = localStorage.getItem(LANGUAGE);
    if (language) {
      i18n.changeLanguage(language);
    }
  }, [i18n]);

  console.log(i18n);

  return (
    <div className="min-h-screen flex items-center justify-center flex-col">
      <img src={image404} alt="404" className="w-40" />
      <h2 className="text-sm text-center mt-5">
        {msg && msg !== "undefined" ? msg : t("default_message")}
      </h2>
      <Button
        type="primary"
        variant="solid"
        size="large"
        className="mt-5"
        onClick={() => (window.location.href = "/")}
      >
        <span>{t("back_to_home")}</span>
      </Button>
    </div>
  );
};

export default NotFound;
