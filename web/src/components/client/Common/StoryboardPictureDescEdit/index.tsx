import { Flex, Input, App } from "antd";
import React, { ChangeEvent, useContext,useEffect } from "react";
import { createPortal } from "react-dom";

import { useTranslation } from "react-i18next";
import {
  DetailContexts,
  IDetailContexts,
} from "../../Common/DetailContainer/contexts/detail-contexts";
import ModalBase from "../ModalBase";
import dashboardApi from "./../../../../api/dashboardApi";
import {
  Character,
  SceneDescription,
} from "./../../../../types/storyboard";

const { TextArea } = Input;
interface IProps {
  boardId: string;
  isModalOpen?: boolean;
  setIsModalOpen?: React.Dispatch<React.SetStateAction<boolean>>;
  backgroundDesc?: SceneDescription;
  setBackgroundDesc?: React.Dispatch<React.SetStateAction<SceneDescription>>;
}

const StoryboardPictureDescEdit: React.FC<IProps> = ({
  boardId,
  isModalOpen = false,
  setIsModalOpen,
  backgroundDesc,
  setBackgroundDesc,
}: IProps) => {
  const { t } = useTranslation();
  const detailContexts: IDetailContexts = useContext<IDetailContexts>(DetailContexts);
  const { message: messageApi } = App.useApp();

  const [tempBackgroundDesc, setTempBackgroundDesc] = React.useState<SceneDescription>(null);

  useEffect(() => {
    if (backgroundDesc) {
      setTempBackgroundDesc(backgroundDesc);
    }
  }, [backgroundDesc]);

  const handleModalCancel = async () => {
    setIsModalOpen(false);
  };

  const handleModalOk = async () => {
    setIsModalOpen(false);
    // 检查是否有变化
    const hasChanges = !isDescriptionEqual(backgroundDesc, tempBackgroundDesc);

    if (hasChanges) {
      await updateCellValue();
    }
  };

  // 辅助函数：比较两个场景描述对象是否相等
  const isDescriptionEqual = (
    desc1: SceneDescription,
    desc2: SceneDescription
  ): boolean => {
    // 比较背景描述
    if (desc1.background !== desc2.background) return false;

    // 比较角色数量
    if (desc1.characters.length !== desc2.characters.length) return false;

    // 比较每个角色的描述
    for (let i = 0; i < desc1.characters.length; i++) {
      const char1 = desc1.characters[i];
      const char2 = desc2.characters.find((c) => c.role_id === char1.role_id);

      if (!char2 || char1.action_and_emotion !== char2.action_and_emotion) {
        return false;
      }
    }

    return true;
  };

  const updateCellValue = async () => {
    const res = await dashboardApi.storyboardUpdate({
      projectId: detailContexts.projectItemObj?.id,
      storyboardId: boardId,
      data: tempBackgroundDesc,
      updateType: "scene_description",
    });
    if (res.success && res.result?.code === 0) {
      setBackgroundDesc(tempBackgroundDesc);
    } else {
      messageApi.error(res.result?.msg);
    }
  };

  const onBgDescChange = (e: ChangeEvent<HTMLTextAreaElement>) => {
    const newBackgroundDescObj = {
      ...tempBackgroundDesc,
      background: e.target.value,
    };
    setTempBackgroundDesc(newBackgroundDescObj);
  };

  const onRoleDescChange = (
    e: ChangeEvent<HTMLTextAreaElement>,
    roleId: string
  ) => {
    const newBackgroundDescObj = {
      ...tempBackgroundDesc,
      characters: tempBackgroundDesc.characters.map((item) => {
        if (item.role_id === roleId) {
          return {
            ...item,
            action_and_emotion: e.target.value,
          };
        }
        return item;
      }),
    };
    setTempBackgroundDesc(newBackgroundDescObj);
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
                {t("scene_description")}
              </div>
            </div>
            <div>
            <Flex vertical>
              <div>{t("background")}：</div>
              <TextArea
                showCount
                value={tempBackgroundDesc?.background}
                maxLength={300}
                onChange={onBgDescChange}
                style={{
                  height: 80,
                  resize: "none",
                  marginBottom: 24,
                }}
                placeholder={t("please_input")}
              />
            </Flex>

              {/* 根据editType判断是否显示角色编辑区域 */}
              {tempBackgroundDesc?.characters?.map((item: Character, index) => {
                return <Flex key={`roleDesc--${item.role_id}-${index}`} vertical>
                        <div>{item.role_name}：</div>
                          <TextArea
                            showCount
                            value={item.action_and_emotion}
                            maxLength={300}
                            onChange={(e) => {
                              onRoleDescChange(e, item.role_id);
                            }}
                            style={{
                              height: 80,
                              resize: "none",
                              marginBottom: 24,
                            }}
                            placeholder={t("please_input")}
                          />
                      </Flex>;
              })}
            </div>
          </div>
        </ModalBase>,
        document.body
      )}
    </>
  );
};

export default StoryboardPictureDescEdit;
