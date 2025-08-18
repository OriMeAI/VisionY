/**
 * 作品详情页的Tab组件
 */

import { ProjectItemObj } from "@/src/libs/interfaces";
import { Segmented, Select } from "antd";
import React, { useEffect, useState } from "react";
import { useTranslation } from "react-i18next";
import filmIcon from "./../../../../assets/images/pages/detail/film_icon.svg";
import storyboardIcon from "./../../../../assets/images/pages/detail/storyboard_icon.svg";
import viewIcon from "./../../../../assets/images/pages/detail/view_icon.svg";
import { DetailTabType } from "./../../../libs/enums";
import { LINK_BG_COLOR_MAPS, TAB_LINK_MAPS_NEW } from "./../../../libs/global-config";
import drawHelper from "./../../../libs/draw-helper";


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
}

const DetailTabLeft: React.FC<IProps> = ({
  currSegment,
  setCurrSegment,
}: IProps) => {
  const { t } = useTranslation();

  console.log("currSegment", currSegment);

  const onSegmentedChange = (value: DetailTabType | string) => {
    if (typeof value === "string") {
      return;
    }
    setCurrSegment(value);
    // Store in sessionStorage with project id as key
    // if (templateProjectItem?.id) {
    //   sessionStorage.setItem(`selectedTab_${templateProjectItem.id}`, value.toString());
    // }
  };
  // 根据 TAB_LINK_MAPS[currSegment] 的值设置 body 的背景颜色
  // React.useEffect(() => {
  //   document.body.style.backgroundColor =
  //     LINK_BG_COLOR_MAPS[
  //       TAB_LINK_MAPS_NEW[currSegment] as keyof typeof LINK_BG_COLOR_MAPS
  //     ];
  // }, [currSegment]);
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
          <img src={filmIcon} alt="" />
          <span className="text-sm">{t("film_table")}</span>
        </div>
      ),
      value: DetailTabType.FilmTable,
    },
    {
      label: (
        <div className="h-9 flex items-center space-x-2 w-36 justify-center">
          <img src={storyboardIcon} alt="" />{" "}
          <span className="text-sm">{t("storyboard")}</span>
        </div>
      ),
      value: DetailTabType.Storyboard,
    },
    {
      label: (
        <div className="h-9 flex items-center space-x-2 w-36 justify-center">
          <img src={viewIcon} alt="" />{" "}
          <span className="text-sm">{t("visual_mode")}</span>
        </div>
      ),
      value: DetailTabType.VisualView,
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
      label: t(
        option.value === DetailTabType.FilmTable
          ? "film_table"
          : option.value === DetailTabType.Storyboard
          ? "storyboard"
          : "visual_mode"
      ),
    })),
  ];

  return isNarrowScreen ? (
    // 窄屏幕使用Select组件
    <Select
      style={{ width: "100%" }}
      value={
        TAB_LINK_MAPS_NEW[currSegment] === "tableview" ||
        TAB_LINK_MAPS_NEW[currSegment] === "boardview" ||
        TAB_LINK_MAPS_NEW[currSegment] === "visualview"
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
      options={[
        {
          label: (
            <div className="h-9 flex items-center space-x-2 w-36 justify-center">
              <img
                src={filmIcon}
                alt=""
              />
              <span className="text-sm">{t("film_table")}</span>
            </div>
          ),
          value: DetailTabType.FilmTable,
        },
        {
          label: (
            <div className="h-9 flex items-center space-x-2 w-36 justify-center">
              <img src={storyboardIcon} alt="" />{" "}
              <span className="text-sm">{t("storyboard")}</span>
            </div>
          ),
          value: DetailTabType.Storyboard,
        },
        {
          label: (
            <div className="h-9 flex items-center space-x-2 w-36 justify-center">
              <img src={viewIcon} alt="" />{" "}
              <span className="text-sm">{t("visual_mode")}</span>
            </div>
          ),
          value: DetailTabType.VisualView,
        },
      ]}
      onChange={onSegmentedChange}
    />
  );
};

export default DetailTabLeft;
