/**
 * 使用案例按钮
 */
import { Button, ConfigProvider } from "antd";
import React, { useContext } from "react";
import { createPortal } from "react-dom";
import { useTranslation } from "react-i18next";
import ModalBase from "../../client/Common/ModalBase";
import {
  DashboardContexts,
  IDashboardContexts,
} from "./../../../contexts/dashboard-contexts";
import {
  IModalContexts,
  ModalContexts,
} from "./.././../../contexts/modal-contexts";

import planLimit from "./../../../../assets/images/pages/workspace/plan_limit.jpg";

interface IProps {}

const UpgradeModal: React.FC<IProps> = ({}) => {
  const { t } = useTranslation();
  const dashboardContexts: IDashboardContexts = useContext(DashboardContexts);
  const modalContexts: IModalContexts = useContext<IModalContexts>(ModalContexts);
  const handleModalCancel = async () => { dashboardContexts.setIsShowUpgradeModal(false);};

  const showMembershipModal = () => {
    handleModalCancel();
    modalContexts.setIsShowMembershipModal(true);
  };

  return (
    <>
      {createPortal(
        <ModalBase
          open={dashboardContexts.isShowUpgradeModal}
          onCancel={handleModalCancel}
          okText={t("upgrade_modal_got_it")}
          cancelText={t("upgrade_modal_got_it")}
          width={400}
          height={undefined}
          footer={
            <div style={{ display: "flex", marginTop: 24 }}>
              <ConfigProvider
                theme={{
                  components: {
                    Button: {
                      colorPrimaryHover: "#7E2FFF",
                    },
                  },
                }}
              >
                <Button
                  type="default"
                  variant="outlined"
                  size="large"
                  className="w-full"
                  onClick={handleModalCancel}
                >
                  <span>{t("upgrade_modal_got_it")}</span>
                </Button>
              </ConfigProvider>
              <ConfigProvider
                theme={{
                  components: {
                    Button: {
                      colorPrimary: "#7E2FFF",
                      colorPrimaryHover: "#7E2FFF",
                    },
                  },
                }}
              >
              <Button
                type="primary"
                variant="solid"
                size="large"
                className="w-full"
                style={{ marginInlineStart: 8 }}
                onClick={showMembershipModal}
              >
                <span>{t("upgrade_modal_extend_limit")}</span>
              </Button>
              </ConfigProvider>
            </div>
          }
        >
          <div
            className="w-auto grid gap-4"
            style={{ padding: "24px 24px 0 24px" }}
          >
            <div>
              <div className="space-y-6">
                <img
                  className="min-w-[352px] rounded-lg"
                  src={planLimit}
                />
                <div>
                  <h2 className="text-lg font-semibold text-center">
                    {t("upgrade_modal_limit_reminder")}
                  </h2>
                  <p className="text-sm text-muted-foreground text-left">
                    {t("upgrade_modal_project_limit_message")}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </ModalBase>,
        document.body
      )}
    </>
  );
};

export default UpgradeModal;
