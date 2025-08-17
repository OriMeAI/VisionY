/**
 * 重命名项目弹窗
 */
import { Button, Form, Input, App } from "antd";
import React from "react";
import { createPortal } from "react-dom";
import { useTranslation } from "react-i18next";
import ModalBase from "../../client/Common/ModalBase";
import dashboardApi from "./../../../api/dashboardApi";

interface IProps {
  projectId: string;
  isModalOpen: boolean;
  setIsModalOpen: (isModalOpen: boolean) => void;
  onRenameSuccess?: (newName: string) => void; // 添加回调函数
}

const RenameProjectModal: React.FC<IProps> = ({
  projectId,
  isModalOpen,
  setIsModalOpen,
  onRenameSuccess
}: IProps) => {
  const { t } = useTranslation();
  const [currProjectName, setCurrProjectName] = React.useState<string>("");
  const { message: messageApi } = App.useApp();

  const renameProject = async () => {
    const res = await dashboardApi.renameProject({
      id: projectId,
      name: currProjectName,
    });
    if (res.success && res.result?.code === 0) {
      setCurrProjectName("");
      onRenameSuccess(currProjectName);
      messageApi.success(t('common_update_success'));
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };

  const handleModalOk = async () => {
    if (!currProjectName) {
      messageApi.error(t('project_name_required'));
      return;
    }
    setIsModalOpen(false);
    await renameProject();
  };
  const onNameChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setCurrProjectName(e.target.value);
  };
  return (
    <>
      {createPortal(
        <ModalBase
          open={isModalOpen}
          onCancel={() => setIsModalOpen(false)}
          width={520}
          height={262}
          footer={
            <Button type="primary" size="large" onClick={handleModalOk}>
              <span>{t('common_confirm')}</span>
            </Button>
          }
        >
          <div
            className="w-auto grid gap-4"
            style={{ padding: "24px 24px 0 24px" }}
          >
            <div className="space-y-1.5">
              <div className="text-lg font-semibold">{t('project_rename_title')}</div>
            </div>
            <p className="text-slate-600">
              {t('project_rename_description')}
            </p>
            <div className="mt-1">
              <div>
                <Form.Item
                  name="name"
                  layout="vertical"
                >
                  <Input
                    placeholder={t('project_enter_new_name')}
                    size="large"
                    maxLength={64}
                    onChange={onNameChange}
                    value={currProjectName}
                    autoComplete="off"
                  />
                </Form.Item>
              </div>
            </div>
          </div>
        </ModalBase>,
        document.body
      )}
    </>
  );
};

export default RenameProjectModal;
