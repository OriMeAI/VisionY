/**
 * 作品详情页的Tab组件
 */

import { Segmented, Select } from "antd";
import React from "react";
import { useTranslation } from "react-i18next";
import { useNavigate } from "react-router-dom";
import {
  DetailContexts,
  IDetailContexts,
} from "../../client/Common/DetailContainer/contexts/detail-contexts";
import bookIcon from "./../../../../assets/images/pages/detail/book_icon.svg";
import bookIconDisabled from "./../../../../assets/images/pages/detail/book_icon_disabled.svg";
import smileIcon from "./../../../../assets/images/pages/detail/smile_icon.svg";
import { DetailTabType } from "./../../../libs/enums";
import { LINK_BG_COLOR_MAPS, TAB_LINK_MAPS_NEW } from "./../../../libs/global-config";


// 路由与tab映射
export const LINK_TAB_MAPS_NEW = {
  scriptview: DetailTabType.Script,
  roleview: DetailTabType.Role,
  tableview: DetailTabType.FilmTable,
  boardview: DetailTabType.Storyboard,
  visualview: DetailTabType.VisualView,
};
interface IProps {
  projectId: string; // 项目id
  leftWidth?: number; // 左侧容器宽度
}

const DetailTabRight: React.FC<IProps> = ({
  projectId,
  leftWidth = 0,
}: IProps) => {
  const { t } = useTranslation();
  const detailContexts: IDetailContexts =
    React.useContext<IDetailContexts>(DetailContexts);
  const pathname = location.pathname;
  const navigate = useNavigate();
  // 获取路由片段信息
  const routeSegments = pathname.split("/");
  const onSegmentedChange = (value: DetailTabType | string) => {
    if (typeof value === "string") {
      return;
    }
    navigate(`/project/${projectId}/${TAB_LINK_MAPS_NEW[value]}`);
  };
  let lastSegment = routeSegments[routeSegments.length - 1];

  // 根据 lastSegment 的值设置 body 的背景颜色
  React.useEffect(() => {
    document.body.style.backgroundColor =
      LINK_BG_COLOR_MAPS[lastSegment as keyof typeof LINK_BG_COLOR_MAPS];
  }, [lastSegment]);
  // 根据leftWidth决定使用Segmented还是Select组件
  const isNarrowScreen = leftWidth > 0 && leftWidth < 980;

  // 选项数据，两种控件共用
  const options = [
    {
      label: (
        <div className="h-9 flex items-center space-x-2 w-36 justify-center">
          <img src={
              detailContexts.projectItemObj?.hasShot &&
              detailContexts.projectItemObj?.hasStoryboard
                ? bookIcon
                : bookIconDisabled} alt="" />
          <span className="text-sm">{t("script")}</span>
        </div>
      ),
      value: DetailTabType.Script,
      disabled:
        !detailContexts.projectItemObj?.hasShot ||
        !detailContexts.projectItemObj?.hasStoryboard,
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
      disabled: option.disabled,
    })),
  ];

  return isNarrowScreen ? (
    // 窄屏幕使用Select组件
    <Select
      style={{ width: "100%" }}
      value={
        lastSegment === "scriptview" || lastSegment === "roleview"
          ? LINK_TAB_MAPS_NEW[lastSegment as keyof typeof LINK_TAB_MAPS_NEW]
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
      value={LINK_TAB_MAPS_NEW[lastSegment as keyof typeof LINK_TAB_MAPS_NEW]}
      options={options}
      onChange={onSegmentedChange}
    />
  );
};

export default DetailTabRight;
