import { Flex, Input, App } from "antd";
import React, { ChangeEvent, useContext,useEffect } from "react";
import { createPortal } from "react-dom";
import {
  DetailContexts,
  IDetailContexts,
} from "../../Common/DetailContainer/contexts/detail-contexts";
import ModalBase from "../ModalBase";
import dashboardApi from "./../../../../api/dashboardApi";
import { Dialogue, StoryboardShot } from "./../../../../types/storyboard";
import { useTranslation } from "react-i18next";

const { TextArea } = Input;
interface IProps {
  boardItem: StoryboardShot;
  isModalOpen: boolean;
  setIsModalOpen: React.Dispatch<React.SetStateAction<boolean>>;
  dialogues: Dialogue[];
  setDialogues: React.Dispatch<React.SetStateAction<Dialogue[]>>;
}

const StoryboardDialoguesEdit: React.FC<IProps> = ({
  boardItem,
  isModalOpen,
  setIsModalOpen,
  dialogues,
  setDialogues,
}: IProps) => {
  const { t } = useTranslation();
  const detailContexts: IDetailContexts = useContext<IDetailContexts>(DetailContexts);
  const [tempDialogues, setTempDialogues] = React.useState<Dialogue[]>(null);
  const { message: messageApi } = App.useApp();

  useEffect(() => {
    if(dialogues){
      setTempDialogues(dialogues);
    }
  }, [dialogues])

  const handleModalCancel = async () => { setIsModalOpen(false);};

  const handleModalOk = async () => {
    setIsModalOpen(false);
    // 检查是否有变化
    const hasChanges = !isDialoguesEqual(dialogues, tempDialogues);

    if (hasChanges) {
      await updateCellValue();
    }
  };

  // 辅助函数：比较两个对话数组是否相等
  const isDialoguesEqual = (
    dialogues1: Dialogue[],
    dialogues2: Dialogue[]
  ): boolean => {
    // 比较对话数量
    if (dialogues1.length !== dialogues2.length) return false;

    // 比较每个对话的内容
    for (let i = 0; i < dialogues1.length; i++) {
      const dialogue1 = dialogues1[i];
      const dialogue2 = dialogues2.find((d) => d.role_id === dialogue1.role_id);

      if (!dialogue2 || dialogue1.content !== dialogue2.content) {
        return false;
      }
    }

    return true;
  };

  const updateCellValue = async () => {
    const res = await dashboardApi.storyboardUpdate({
      projectId: detailContexts.projectItemObj?.id,
      storyboardId: boardItem.shot_id,
      data: tempDialogues,
      updateType: "dialogues",
    });
    if (res.success && res.result?.code === 0) {
      setDialogues(tempDialogues);
    } else {
      messageApi.error(res.result?.msg);
    }
  };

  const onDialogueChange = (
    e: ChangeEvent<HTMLTextAreaElement>,
    roleId: string
  ) => {
    const newDialogues = tempDialogues.map((item) => {
      if (item.role_id === roleId) {
        return {
          ...item,
          content: e.target.value,
        };
      }
      return item;
    });
    setTempDialogues(newDialogues);
  };

  return (
    <>
      {createPortal(
        <ModalBase
          open={isModalOpen}
          onOk={handleModalOk}
          onCancel={handleModalCancel}
          okText={t("confirm")}
          cancelText={t("cancel")}
          width={520}
          height={undefined}
        >
          <div
            className="w-auto grid gap-4"
            style={{ padding: "24px 24px 0 24px" }}
          >
            <div className="space-y-1.5">
              <div className="text-lg font-semibold">
                {t("storyboard_dialogues")}
              </div>
            </div>
            <div>
              {tempDialogues?.map((item: Dialogue, index) => {
                return (
                  <Flex key={`dialogue-edit-${item.role_id}-${index}`} vertical>
                    <div>{item.role_name}：</div>
                    <TextArea
                      showCount
                      value={item.content}
                      maxLength={300}
                      onChange={(e) => {
                        onDialogueChange(e, item.role_id);
                      }}
                      style={{
                        height: 80,
                        resize: "none",
                        marginBottom: 24,
                      }}
                      placeholder={t("please_input")}
                    />
                  </Flex>
                );
              })}
            </div>
          </div>
        </ModalBase>,
        document.body
      )}
    </>
  );
};

export default StoryboardDialoguesEdit;
