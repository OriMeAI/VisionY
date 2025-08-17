/**
 * 分享项目弹窗
 */
import { Button, Input, App } from "antd";
import React from "react";
import { createPortal } from "react-dom";
import ModalBase from "../../client/Common/ModalBase";
import copyIconWhite from "./../../../../assets/images/icons/copy_icon_white.svg";
import correctIconWhiteSm from "./../../../../assets/images/icons/correct_icon_white_sm.svg";
import shareIconGreenLg from "./../../../../assets/images/icons/share_icon_green_lg.svg";

import { useTranslation } from "react-i18next";

interface IProps {
  projectId: string;
  isModalOpen: boolean;
  setIsModalOpen: (isModalOpen: boolean) => void;
}

const ShareProjectModal: React.FC<IProps> = ({
  projectId,
  isModalOpen,
  setIsModalOpen,
}: IProps) => {
  const {t} = useTranslation();
  const [isCopied, setIsCopied] = React.useState(false);
  const projectLink = `${window.location.origin}/share/${projectId}`;
  const { message: messageApi } = App.useApp();
  const handleModalCancel = async () => {
    setIsModalOpen(false);
  };

  const copyLink = () => {
    messageApi.success(t('copy_link_success'));
    navigator.clipboard.writeText(projectLink);
    setIsCopied(true);
    handleModalCancel();
  };
  return (
    <>
      {createPortal(
        <ModalBase
          open={isModalOpen}
          onCancel={handleModalCancel}
          width={512}
          height={undefined}
          // showFooter={false}
          footer={<div style={{ height: '0px' }} />}
        >
          <div style={{ padding: "20px 24px 0 24px" }}>
            <div className="mb-6 mt-1">
              <img
                src="data:image/svg+xml,%3csvg%20width='216'%20height='216'%20viewBox='0%200%20216%20216'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cg%20clip-path='url(%23clip0_3069_3564)'%3e%3cmask%20id='mask0_3069_3564'%20style='mask-type:alpha'%20maskUnits='userSpaceOnUse'%20x='-120'%20y='-120'%20width='336'%20height='336'%3e%3crect%20width='336'%20height='336'%20transform='translate(-120%20-120)'%20fill='url(%23paint0_radial_3069_3564)'/%3e%3c/mask%3e%3cg%20mask='url(%23mask0_3069_3564)'%3e%3ccircle%20cx='48'%20cy='48'%20r='47.5'%20stroke='%23EAECF0'/%3e%3ccircle%20cx='48'%20cy='48'%20r='47.5'%20stroke='%23EAECF0'/%3e%3ccircle%20cx='48'%20cy='48'%20r='71.5'%20stroke='%23EAECF0'/%3e%3ccircle%20cx='48'%20cy='48'%20r='95.5'%20stroke='%23EAECF0'/%3e%3ccircle%20cx='48'%20cy='48'%20r='119.5'%20stroke='%23EAECF0'/%3e%3ccircle%20cx='48'%20cy='48'%20r='143.5'%20stroke='%23EAECF0'/%3e%3ccircle%20cx='48'%20cy='48'%20r='167.5'%20stroke='%23EAECF0'/%3e%3c/g%3e%3c/g%3e%3cdefs%3e%3cradialGradient%20id='paint0_radial_3069_3564'%20cx='0'%20cy='0'%20r='1'%20gradientUnits='userSpaceOnUse'%20gradientTransform='translate(168%20168)%20rotate(90)%20scale(168%20168)'%3e%3cstop/%3e%3cstop%20offset='1'%20stop-opacity='0'/%3e%3c/radialGradient%3e%3cclipPath%20id='clip0_3069_3564'%3e%3crect%20width='336'%20height='336'%20fill='white'%20transform='translate(-120%20-120)'/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e"
                className="absolute left-0 top-0"
                alt="icon"
              />
              <div className="w-12 h-12 rounded-full bg-green-100 flex items-center justify-center">
                <img src={shareIconGreenLg} alt="icon" />
              </div>
            </div>
            <div className="relative z-10">
              <div className="mb-5">
                <h2 className="text-lg text-gray-900 font-semibold mb-1">
                  {t('share_your_project')}
                </h2>
                <p className="text-sm text-slate-600">
                  {t('share_warning')}
                </p>
              </div>
              <h2 className="text-sm mb-1 text-slate-700">{t('project_link')}</h2>
              <div className="flex w-full justify-between space-x-2">
                <Input
                  disabled
                  size="large"
                  className="truncate"
                  value={projectLink}
                />
                <Button
                  type="primary"
                  size="large"
                  onClick={copyLink}
                  icon={
                    <img
                      src={isCopied ? correctIconWhiteSm : copyIconWhite}
                      alt="copy"
                    />
                  }
                />
              </div>
            </div>
          </div>
        </ModalBase>,
        document.body
      )}
    </>
  );
};

export default ShareProjectModal;
