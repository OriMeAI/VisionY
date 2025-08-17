/**
 * 人脸参考按钮及弹窗
 */

import { Button, App } from "antd";
import smileFacePlusIcon from "./../../../../../assets/images/pages/roleView/smile_face_plus_icon.svg";
import projectApi from "./../../../../api/projectApi";

import React, { useContext, useState } from "react";
import { createPortal } from "react-dom";
import { useTranslation } from "react-i18next";
import ModalBase from "../../Common/ModalBase";
import {
  IRoleViewContexts,
  RoleViewContexts,
} from "../../../../contexts/role-view-contexts";
import FaceReferContent from "../FaceReferContent";

interface IProps {}

const FaceRefer: React.FC<IProps> = ({}: IProps) => {
  const { t } = useTranslation();
  const roleViewContexts = useContext<IRoleViewContexts>(RoleViewContexts);
  const [isModalOpen, setIsModalOpen] = useState<boolean>(false);
  const { message: messageApi } = App.useApp();

  const showModal = async () => {
    setIsModalOpen(true);
    // await swapFaceCheck();
  };

  // 人脸参考校验
  const swapFaceCheck = async () => {
    const res = await projectApi.swapFaceCheck({
      preCheck: true,
    });
    if (res.success && res.result?.code === 0) {
      if (res.result?.data) {
      }
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };

  const handleModalCancel = async () => {
    setIsModalOpen(false);
  };

  const handleModalOk = async () => {
    await handleModalCancel();
  };
  return (
    <>
      <Button
        type="primary"
        size="large"
        className="rounded-lg thrid-step px-8"
        onClick={showModal}
        disabled={roleViewContexts.roleList.length === 0}
        ref={roleViewContexts.tourRef1}
      >
        <img src={smileFacePlusIcon} alt={t("faceRefer_button_alt")} />
        <span>{t("faceRefer_button_text")}</span>
      </Button>

      {createPortal(
        <ModalBase
          open={isModalOpen}
          onCancel={handleModalCancel}
          width={688}
          height={undefined}
          footer={
            <>
              <Button
                type="primary"
                size="large"
                onClick={handleModalOk}
                disabled={roleViewContexts.uploadExampleFigureImg.length === 0}
              >
                <span>{t("faceRefer_modal_confirm")}</span>
              </Button>
            </>
          }
        >
          <div
            className="w-auto grid gap-4"
            style={{
              padding: "24px 24px 0 24px",
              display: "flex",
              flexDirection: "column",
            }}
          >
            <div className="space-y-1.5">
              <div className="text-lg font-semibold text-left">
                {t("faceRefer_modal_title")}
              </div>
            </div>
            <FaceReferContent />
          </div>
        </ModalBase>,
        document.body
      )}
    </>
  );
};

export default FaceRefer;
