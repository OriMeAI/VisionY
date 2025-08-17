/**
 * 使用案例按钮
 */
import { Button, App } from "antd";
import React from "react";
import dashboardApi from "./../../../api/dashboardApi";
import {
  DashboardContexts,
  IDashboardContexts,
} from "./../../../contexts/dashboard-contexts";
import { useTranslation } from "react-i18next";

interface IProps {
  templateId: string;
  usedCount: number;
  totalCount: number;
}

const UseTemplateBtn: React.FC<IProps> = ({
  templateId,
  usedCount,
  totalCount,
}) => {
  const {t} = useTranslation();
  const dashboardContexts: IDashboardContexts =
    React.useContext(DashboardContexts);
  const { message: messageApi } = App.useApp();
  const useTemplate = async () => {
    const res = await dashboardApi.useTemplate(templateId);
    if (res.success && res.result?.code === 0 && res.result?.data) {
      window.location.href = `/project/${res.result.data}/tableview`;
      // 在新标签页打开
      // window.open(`/project/${res.result.data}/tableview`, '_blank');
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };
  return (
    <Button
      onClick={() => {
        if (usedCount >= totalCount) {
          dashboardContexts.setIsShowUpgradeModal(true);
        } else {
          useTemplate();
        }
      }}
      type="default"
      variant="outlined"
      className="text-primary"
    >
      <span>{t('use_case')}</span>
    </Button>
  );
};

export default UseTemplateBtn;
