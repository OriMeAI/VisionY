/**
 * 作品详情页的Tab组件
 */

import { Segmented, Select } from "antd";
import React, { useEffect, useState } from "react";
import { useTranslation } from "react-i18next";
import bookIcon from "./../../../../assets/images/pages/detail/book_icon.svg";
import smileIcon from "./../../../../assets/images/pages/detail/smile_icon.svg";
import { DetailTabType } from "./../../../libs/enums";
import { LINK_BG_COLOR_MAPS, TAB_LINK_MAPS_NEW } from "./../../../libs/global-config";
import drawHelper from "./../../../libs/draw-helper";
import { ProjectItemObj } from "@/src/libs/interfaces";

// 路由与tab映射
export const LINK_TAB_MAPS_NEW = {
  scriptview: DetailTabType.Script,
  roleview: DetailTabType.Role,
  tableview: DetailTabType.FilmTable,
  boardview: DetailTabType.Storyboard,
  visualview: DetailTabType.VisualView,
};
interface IProps {
  currSegment: DetailTabType;
  setCurrSegment: React.Dispatch<React.SetStateAction<DetailTabType>>;
  templateProjectItem: ProjectItemObj | undefined;
}

const DetailTabRight: React.FC<IProps> = ({
  currSegment,
  setCurrSegment,
  templateProjectItem,
}: IProps) => {
  const { t } = useTranslation();

  const onSegmentedChange = (value: DetailTabType | string) => {
    if (typeof value === "string") {
      return;
    }
    setCurrSegment(value);
    // Store in sessionStorage with project id as key
    if (templateProjectItem?.id) {
      sessionStorage.setItem(`selectedTab_${templateProjectItem.id}`, value.toString());
    }
  };
  React.useEffect(() => {
    document.body.style.backgroundColor =
      LINK_BG_COLOR_MAPS[
        TAB_LINK_MAPS_NEW[currSegment] as keyof typeof LINK_BG_COLOR_MAPS
      ];
  }, [currSegment]);
  // 根据leftWidth决定使用Segmented还是Select组件

  const [isNarrowScreen, setIsNarrowScreen] = useState<boolean>(drawHelper.getWinW() > 0 && drawHelper.getWinW() < 980);

  // 添加窗口大小变化监听
  useEffect(() => {
    const handleResize = () => {
      setIsNarrowScreen(drawHelper.getWinW() > 0 && drawHelper.getWinW() < 980);
    };

    window.addEventListener("resize", handleResize);

    // 组件卸载时移除事件监听
    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []); // 依赖项更新
  // 选项数据，两种控件共用
  const options = [
    {
      label: (
        <div className="h-9 flex items-center space-x-2 w-36 justify-center">
          <img src={bookIcon} alt="" />
          <span className="text-sm">{t("script")}</span>
        </div>
      ),
      value: DetailTabType.Script,
    },
    {
      label: (
        <div className="h-9 flex items-center space-x-2 w-36 justify-center">
          <img src={smileIcon} alt="" />
          <span className="text-sm">{t("role")}</span>
        </div>
      ),
      value: DetailTabType.Role,
    },
  ];

  // Select组件的选项数据
  const selectOptions = [
    {
      value: "--",
      label: "--",
    },
    ...options.map((option) => ({
      value: option.value,
      label: t(option.value === DetailTabType.Script ? "script" : "role"),
    })),
  ];

  return isNarrowScreen ? (
    // 窄屏幕使用Select组件
    <Select
      style={{ width: "100%" }}
      value={
        TAB_LINK_MAPS_NEW[currSegment] === "scriptview" ||
        TAB_LINK_MAPS_NEW[currSegment] === "roleview"
          ? LINK_TAB_MAPS_NEW[
              TAB_LINK_MAPS_NEW[currSegment] as keyof typeof LINK_TAB_MAPS_NEW
            ]
          : "--"
      }
      onChange={onSegmentedChange}
      options={selectOptions}
    />
  ) : (
    // 宽屏幕使用Segmented组件
    <Segmented
      size="large"
      className="hidden md:block"
      value={currSegment}
      options={options}
      onChange={onSegmentedChange}
    />
  );
};

export default DetailTabRight;
