/**
 * 状态栏
 */
import React from "react";
import { RepaintStatus } from "../../../../../libs/enums";
import style from "./style.module.css";
import { useTranslation } from "react-i18next";

interface IProps {
  repaintStatus: RepaintStatus;
}

const StatusBar: React.FC<IProps> = ({ repaintStatus }: IProps) => {
  const { t } = useTranslation();
  const statusTextMaps = {
    [RepaintStatus.UnStart]: t("status_unstart"),
    [RepaintStatus.Rendering]: t("status_rendering"),
    [RepaintStatus.Success]: t("status_success"),
  };
  const statusTextColorMaps = {
    [RepaintStatus.UnStart]: "#aaa",
    [RepaintStatus.Rendering]: "#44cef6",
    [RepaintStatus.Success]: "#0eb83a",
  };
  return (
    <div className={style.bottomStatus}>
      {/* <div className={style.title}>{t("status_bar")}:</div>
      <div className={style.inner}>
        <ul>
          <li>
            [{t("layer_background")}-
            <span style={{ color: statusTextColorMaps[repaintStatus] }}>
              {statusTextMaps[repaintStatus]}
            </span>
            ]
          </li>
        </ul>
      </div> */}
    </div>
  );
};

export default StatusBar;
