/**
 * Dashboard详情页Layout组件
 */

import { Button } from "antd";
import React, { useEffect, useRef, useState } from "react";
import { useTranslation } from "react-i18next";

import { CloseOutlined } from "@ant-design/icons"; // 添加关闭图标
import {
  DetailContexts,
  IDetailContexts,
} from "../../client/Common/DetailContainer/contexts/detail-contexts";
import ChatBox from "../ChatBox";
import DetailTabLeft from "../DetailTabLeft";
import DetailTabRight from "../DetailTabRight";
import DetailTitle from "./../../../components/client/Common/DetailTitle";
import ExportDropdown from "./../../../components/common/ExportDropdown";
import LanguageDropdown from "./../../../components/common/LanguageDropdown";
import UserCenterDropdown from "./../../../components/common/UserCenterDropdown";
import {
  IModalContexts,
  ModalContexts,
} from "./../../../contexts/modal-contexts";
import { IUserContexts, UserContexts } from "./../../../contexts/user-contexts";

interface IProps {
  projectId: string; // 项目id
  children: React.ReactNode;
}

const DetailContainer: React.FC<IProps> = ({ projectId, children }: IProps) => {
  const { t } = useTranslation();
  const userContexts: IUserContexts =
    React.useContext<IUserContexts>(UserContexts);
  const detailContexts: IDetailContexts =
    React.useContext<IDetailContexts>(DetailContexts);
  const modalContexts: IModalContexts =
    React.useContext<IModalContexts>(ModalContexts);
  const INIT_RIGHT_PANEL_WIDTH = detailContexts.showRightPanel ? 400 : 0;
  const pathname = location.pathname;
  // 获取路由片段信息
  const routeSegments = pathname.split("/");
  let lastSegment = routeSegments[routeSegments.length - 1];

  // 添加状态来跟踪左侧容器的宽度
  const [leftWidth, setLeftWidth] = useState(
    window.innerWidth - INIT_RIGHT_PANEL_WIDTH
  );
  const [isDragging, setIsDragging] = useState(false);
  // 使用DetailContexts中的showRightPanel状态
  // 添加状态来跟踪右侧容器的宽度
  const [rightWidth, setRightWidth] = useState(INIT_RIGHT_PANEL_WIDTH);
  const dividerRef = useRef<HTMLDivElement>(null);

  // 添加窗口大小变化监听
  useEffect(() => {
    const handleResize = () => {
      if (!detailContexts.showRightPanel) {
        // 如果右侧面板隐藏，则左侧容器占据整个窗口
        setLeftWidth(window.innerWidth);
        return;
      }

      const availableWidth = window.innerWidth;

      // 判断屏幕是否小于700px
      if (availableWidth < 700) {
        // 在小屏幕下，确保右侧宽度不小于400px
        const newRightWidth = Math.max(INIT_RIGHT_PANEL_WIDTH, rightWidth);
        setRightWidth(newRightWidth);
        // 左侧宽度可以小于300px
        setLeftWidth(Math.max(100, availableWidth - newRightWidth));
      } else {
        // 当屏幕变小时，优先保持右侧宽度不变，缩小左侧宽度
        if (availableWidth < leftWidth + rightWidth) {
          // 如果左侧宽度大于300，优先保持右侧宽度不变，缩小左侧宽度
          if (leftWidth > 300) {
            // 计算新的左侧宽度，但确保不小于300
            const newLeftWidth = Math.max(300, availableWidth - rightWidth);
            setLeftWidth(newLeftWidth);
          }
          // 如果左侧已经达到最小宽度300，则开始缩小右侧宽度
          else if (rightWidth > INIT_RIGHT_PANEL_WIDTH) {
            // 右侧宽度缩小，但不小于400
            const newRightWidth = Math.max(
              INIT_RIGHT_PANEL_WIDTH,
              availableWidth - 300
            );
            setRightWidth(newRightWidth);
            setLeftWidth(availableWidth - newRightWidth);
          }
          // 如果右侧已经达到最小宽度400，则继续缩小左侧宽度
          else {
            setLeftWidth(availableWidth - INIT_RIGHT_PANEL_WIDTH);
            setRightWidth(INIT_RIGHT_PANEL_WIDTH);
          }
        }
        // 当屏幕变大时，保持右侧宽度不变，增加左侧宽度
        else if (!isDragging) {
          // 直接计算新的左侧宽度为可用宽度减去右侧宽度
          setLeftWidth(availableWidth - rightWidth);
        }
      }
    };

    window.addEventListener("resize", handleResize);

    // 组件卸载时移除事件监听
    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, [detailContexts.showRightPanel, leftWidth, rightWidth, isDragging]); // 依赖项更新

  // 添加关闭按钮并实现隐藏功能

  // 处理关闭按钮点击事件
  const handleClosePanel = () => {
    detailContexts.setShowRightPanel(false);
    // 当隐藏右侧面板时，将左侧容器宽度设置为全屏
    setLeftWidth(window.innerWidth);
  };

  // 处理拖动事件
  const handleMouseDown = (e: React.MouseEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      if (!isDragging) return;

      const availableWidth = window.innerWidth;

      // 判断屏幕是否小于700px
      if (availableWidth < 700) {
        // 在小屏幕下，确保右侧宽度不小于400px，左侧宽度可以小于300px
        const minLeftWidth = Math.max(
          100,
          availableWidth - INIT_RIGHT_PANEL_WIDTH
        ); // 左侧最小宽度为100px
        const newLeftWidth = Math.min(
          e.clientX,
          availableWidth - INIT_RIGHT_PANEL_WIDTH
        );

        // 确保左侧宽度不小于最小值
        setLeftWidth(Math.max(minLeftWidth, newLeftWidth));
        setRightWidth(availableWidth - Math.max(minLeftWidth, newLeftWidth));
      } else {
        // 在大屏幕下，保持原有逻辑
        const newLeftWidth = Math.max(
          300,
          Math.min(e.clientX, window.innerWidth - INIT_RIGHT_PANEL_WIDTH)
        );
        setLeftWidth(newLeftWidth);
        setRightWidth(window.innerWidth - newLeftWidth);
      }
    };

    const handleMouseUp = () => {
      setIsDragging(false);
    };

    if (isDragging) {
      document.addEventListener("mousemove", handleMouseMove);
      document.addEventListener("mouseup", handleMouseUp);
    }

    return () => {
      document.removeEventListener("mousemove", handleMouseMove);
      document.removeEventListener("mouseup", handleMouseUp);
    };
  }, [isDragging]);
  const showCreditsModal = () => {
    modalContexts.setIsShowCreditsModal(true);
  };

  const showMembershipModal = () => {
    modalContexts.setIsShowMembershipModal(true);
  };

  // 不再需要计算右侧容器宽度，因为我们现在直接使用状态变量
  // const rightWidth = showRightPanel ? window.innerWidth - leftWidth : 0;

  return (
    <div className="overflow-hidden">
      <div className="h-[72px] shadow-sm fixed w-full top-0 z-50 bg-white">
        <div className="mx-8 h-full flex items-center justify-between">
          <DetailTitle title={t("back")} link="/workspace" />

          <div className="truncate max-w-[200px] ml-2 text-lg font-semibold">
            {detailContexts.projectItemObj?.name}
          </div>
          {/* <DetailTab projectId={projectId} /> */}
          <div className="flex items-center space-x-6">
            <Button
              type="text"
              size="large"
              className="max-[980px]:hidden" // 在中等屏幕以下隐藏
              onClick={showMembershipModal}
            >
              <span>{t("subscribe_membership")}</span>
            </Button>
            <Button
              type="text"
              size="large"
              className="max-[980px]:hidden" // 在中等屏幕以下隐藏
              onClick={showCreditsModal}
            >
              <span>{t("purchase_generate_credits")}</span>
            </Button>
            <ExportDropdown
              projectId={projectId}
              btnDisabled={!detailContexts.projectItemObj?.hasShot}
            />
            <LanguageDropdown />
            {userContexts.isAuthenticated ? (
              <UserCenterDropdown />
            ) : (
              <Button
                onClick={() => {
                  userContexts.setIsShowLoginModal(true);
                }}
                type="primary"
                size="large"
                variant="solid"
              >
                <span>{t("login")}</span>
              </Button>
            )}
          </div>
        </div>
      </div>
      <div className="flex w-full mt-[72px]">
        <div
          style={{
            width: detailContexts.showRightPanel ? `${leftWidth}px` : "100%",
            // border: "1px solid #F3F5F9",
            position: "relative",
          }}
        >
          <div
            className="h-[72px] shadow-sm absolute left-0 top-0 z-50 bg-white"
            style={{
              width: detailContexts.showRightPanel ? `${leftWidth}px` : "100%",
              maxWidth: detailContexts.showRightPanel
                ? `${leftWidth}px`
                : "100%",
              overflow: "hidden",
            }}
          >
            <div className="mx-8 h-full flex items-center justify-between space-x-4">
              {/* 无论宽度如何，都使用相同的组件，但在组件内部根据宽度决定使用Select还是Segmented */}

              <DetailTabLeft projectId={projectId} leftWidth={leftWidth} />
              <DetailTabRight projectId={projectId} leftWidth={leftWidth} />
            </div>
          </div>
          <div
            className="h-full bg-background mt-[72px]"
            style={{
              height: "calc(100vh - 144px)",
              overflow: "auto",
              width: detailContexts.showRightPanel ? `${leftWidth}px` : "100%",
            }}
          >
            {children}
          </div>
        </div>

        {/* 添加可拖动的分隔条 */}
        {detailContexts.showRightPanel && (
          <div
            ref={dividerRef}
            className="cursor-col-resize w-[6px] bg-gray-200 hover:bg-[#7E2FFF] active:bg-[#7E2FFF] h-[calc(100vh-72px)]"
            onMouseDown={handleMouseDown}
            style={{
              transition: isDragging ? "none" : "background-color 0.2s",
              position: "fixed",
              left: `${leftWidth}px`,
              top: "72px",
              zIndex: 60,
            }}
          />
        )}

        {detailContexts.showRightPanel && (
          <div
            className="fixed right-0 top-[72px] h-[calc(100vh-72px)]"
            style={{ width: `${rightWidth}px` }}
          >
            {/* 添加关闭按钮 */}
            <Button
              type="text"
              icon={<CloseOutlined />}
              onClick={handleClosePanel}
              className="absolute top-2 right-2 z-10 hover:bg-gray-100"
              size="small"
            />
            <ChatBox />
          </div>
        )}
      </div>
    </div>
  );
};

export default DetailContainer;
