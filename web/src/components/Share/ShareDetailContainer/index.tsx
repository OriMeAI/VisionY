/**
 * Dashboard详情页Layout组件
 */

import { Button } from "antd";
import React from "react";
import { useTranslation } from "react-i18next";
import { DetailTabType } from "../../../libs/enums";
import { ProjectItemObj } from "../../../libs/interfaces";
import DetailTabLeft from "../DetailTabLeft";
import DetailTabRight from "../DetailTabRight";
import DetailTitle from "./../../../components/client/Common/DetailTitle";
import LanguageDropdown from "./../../../components/common/LanguageDropdown";
import { IUserContexts, UserContexts } from "./../../../contexts/user-contexts";

interface IProps {
  currSegment: DetailTabType;
  setCurrSegment: React.Dispatch<React.SetStateAction<DetailTabType>>;
  projectId: string; // 项目id
  children: React.ReactNode;
  templateProjectItem: ProjectItemObj | undefined;
}

const ShareDetailContainer: React.FC<IProps> = ({
  currSegment,
  setCurrSegment,
  projectId,
  children,
  templateProjectItem,
}: IProps) => {
  const { t } = useTranslation();
  const userContexts: IUserContexts =
    React.useContext<IUserContexts>(UserContexts);
  const pathname = location.pathname;
  // 获取路由片段信息
  const routeSegments = pathname.split("/");
  let lastSegment = routeSegments[routeSegments.length - 1];

  return (
    <div className="overflow-hidden">
      <div className="h-[72px] shadow-sm fixed w-full top-0 z-50 bg-white">
        <div className="mx-8 h-full flex items-center justify-between">
          {/* <DetailTitle title={t("back")} link="/workspace" /> */}
          <div className="flex items-center">
            <a 
              href="/workspace"
              className="bg-primary text-white py-2 px-5 rounded-lg font-medium hover:bg-primary-darker hover:text-white transition-all duration-300 ease-in-out transform hover:scale-105 hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-primary focus:ring-opacity-50"
            >
              {/* <span  className="align-middle max-[980px]:hidden truncate min-w-40 max-w-56 ml-2 hover:text-[rgba(0,0,0,.88)]">
                {t("workspace")}
              </span> */}
              {t("workspace")}
            </a>
          </div>

          <div className="truncate max-w-[200px] ml-2 text-lg font-semibold">
            {templateProjectItem?.name}
          </div>
          {/* <DetailTab projectId={projectId} /> */}
          <div className="flex items-center space-x-6">
            <LanguageDropdown />
          </div>
        </div>
      </div>
      <div className="flex w-full mt-[72px]">
        <div
          style={{
            width: "100%",
            // border: "1px solid #F3F5F9",
            position: "relative",
          }}
        >
          <div
            className="h-[72px] shadow-sm absolute left-0 top-0 z-50 bg-white"
            style={{
              width: "100%",
              maxWidth: "100%",
              overflow: "hidden",
            }}
          >
            <div className="mx-8 h-full flex items-center justify-between space-x-4">
              {/* 无论宽度如何，都使用相同的组件，但在组件内部根据宽度决定使用Select还是Segmented */}

              <DetailTabLeft
                currSegment={currSegment}
                setCurrSegment={setCurrSegment}
                templateProjectItem={templateProjectItem}
              />
              <DetailTabRight
                currSegment={currSegment}
                setCurrSegment={setCurrSegment}
                templateProjectItem={templateProjectItem}
              />
            </div>
          </div>
          <div
            className="h-full bg-background mt-[72px]"
            style={{
              height: "calc(100vh - 144px)",
              overflow: "auto",
              width: "100%",
            }}
          >
            {children}
          </div>
        </div>
      </div>
    </div>
  );
};

export default ShareDetailContainer;
