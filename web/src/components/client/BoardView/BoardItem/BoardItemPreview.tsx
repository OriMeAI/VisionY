/**
 * 故事板列表项页面
 */

import { Button, Popconfirm } from "antd";
import deleteIcon from "./../../../../../assets/images/icons/delete_icon.svg";
import audioIcon from "./../../../../../assets/images/pages/boardView/audio_icon.svg";
import copyIcon from "./../../../../../assets/images/pages/boardView/copy_icon.svg";
import sortIcon2 from "./../../../../../assets/images/pages/boardView/sort_icon_2.svg";
import videoIcon from "./../../../../../assets/images/pages/boardView/video_icon.svg";
import stringUtils from "./../../../../libs/string-utils";
import { StoryboardShot } from "./../../../../types/storyboard";

import React from "react";
import StoryboardFigureImg from "../../Common/StoryboardFigureImg";
import StoryboardPictureDesc from "../../Common/StoryboardPictureDesc";
import { isNumber } from "lodash";
import { useTranslation } from "react-i18next";
import StoryboardDialogues from "../../Common/StoryboardDialogues";

type IProps = {
  bodyList: StoryboardShot[];
} & Partial<{
  boardItem: StoryboardShot;
  itemIndex: number;
  height: number;
  width: number;
}>;

const BoardItemPreview: React.FC<IProps> = (props: IProps) => {
  const { t } = useTranslation();
  const { boardItem, itemIndex, bodyList, height, width } = props;
  if (!boardItem || !isNumber(itemIndex)) {
    return null;
  }

  const style = {
    zIndex: 9999,
    backgroundColor: "#fff",
    padding: "24px",
    borderRadius: "8px",
    boxShadow: "0 1px 2px -2px rgba(0, 0, 0, 0.08), 0 1px 3px 0 rgba(0, 0, 0, 0.06), 0 2px 4px 2px rgba(0, 0, 0, 0.04)",
    cursor: "default",
    height,
    width,
  };

  return (
    <div className="cursor-default" style={style}>
      <div style={{ width: "100%"}}>
        <div className="w-full">
          <div className="flex items-center justify-between">
            <div className="flex items-center ">
              <div className="mr-6 flex items-center">
                <img src={sortIcon2} alt={t("sort")} className="mr-2 cursor-move" />
                <span>
                {stringUtils.prefixZero((itemIndex + 1).toString())}
                </span>
              </div>
            </div>
            <div className="flex items-center">
              <Button
                className="border-none"
                icon={<img src={copyIcon} alt={t("copy")} />}
              />
              <Popconfirm
                placement="rightTop"
                title={t("delete_storyboard")}
                description={t("delete_storyboard_confirm")}
                trigger="click"
                okText={t("confirm")}
                cancelText={t("cancel2")}
              >
                <Button
                  className="border-none"
                  icon={<img src={deleteIcon} alt={t("delete")} />}
                />
              </Popconfirm>
            </div>
          </div>

          <StoryboardFigureImg
            boardItem={boardItem}
          />
          <div className="flex flex-col px-1">
            <div className="flex">
              <p className="py-4">
                <img src={videoIcon} alt={t("video")} />
              </p>
              <div className="py-2 flex-1">
                <StoryboardPictureDesc boardItem={boardItem} />
              </div>
            </div>
            <div
              className="ant-divider css-aw5bp3 ant-divider-horizontal my-0"
              role="separator"
            ></div>
            <div className="flex">
              <p className="py-4">
                <img src={audioIcon} alt={t("audio")} />
              </p>
              <div className="py-2 flex-1">
                <StoryboardDialogues boardItem={boardItem} />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export { BoardItemPreview };
