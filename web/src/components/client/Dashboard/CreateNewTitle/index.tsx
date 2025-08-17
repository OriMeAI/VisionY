/**
 * 创建新作品弹窗内容
 */

import React from "react";
import createNewIcon from "./../../../../../assets/images/pages/workspace/create_new_icon.svg";
import { useTranslation } from "react-i18next";

const CreateNewTitle: React.FC = () => {
  const { t } = useTranslation();
  return (
    <div className="px-6 pt-6 pb-5">
      <div className="flex space-x-4">
        <div className="border h-12 w-12 rounded-lg flex items-center justify-center">
          <img src={createNewIcon} alt={"create new icon"} />
        </div>
        <div>
          <h2 className="text-gray-900 text-lg font-semibold">
            {t("create_new_work2")}
          </h2>
          <p className="text-slate-600 text-sm ">{t("draw_story_steps")}</p>
        </div>
      </div>
    </div>
  );
};

export default CreateNewTitle;
