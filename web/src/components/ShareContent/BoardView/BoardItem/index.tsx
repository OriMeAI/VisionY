/**
 * 故事板列表项页面
 */

import { Card } from "antd";
import audioIcon from "./../../../../../assets/images/pages/boardView/audio_icon.svg";
import videoIcon from "./../../../../../assets/images/pages/boardView/video_icon.svg";
import stringUtils from "./../../../../libs/string-utils";
import { StoryboardShot } from "./../../../../types/storyboard";

import React from "react";
import StoryboardFigureImg from "./../../../client/Common/StoryboardFigureImg";
import StoryboardPictureDesc from "./../../../client/Common/StoryboardPictureDesc";
import StoryboardDialogues from "./../../../client/Common/StoryboardDialogues";

interface IProps {
  boardItem: StoryboardShot;
  itemIndex: number;
}

const BoardItem: React.FC<IProps> = (props: IProps) => {
  const { boardItem, itemIndex } = props;
  return (
    <Card
      variant="borderless"
      className="flex relative h-full"
      style={{ 
        borderRadius: 8,
        boxShadow: "0 1px 2px -2px rgba(0, 0, 0, 0.08), 0 1px 3px 0 rgba(0, 0, 0, 0.06), 0 2px 4px 2px rgba(0, 0, 0, 0.04)" 
      }}
    >
      <div style={{ width: "100%" }}>
        <div className="w-full">
          <div className="flex items-center justify-between">
            <div className="flex items-center ">
              <div className="mr-6 flex items-center">
                <span>
                  {stringUtils.prefixZero((itemIndex + 1).toString())}
                </span>
              </div>
            </div>
          </div>
          <StoryboardFigureImg
            boardItem={boardItem}
            isEdit={false}
          />
          <div className="flex flex-col px-1">
            <div className="flex">
              <p className="py-4">
                <img src={videoIcon} alt="video" />
              </p>
              <div className="py-2 flex-1">
                <StoryboardPictureDesc boardItem={boardItem} isEdit={false} />
              </div>
            </div>
            <div
              className="ant-divider css-aw5bp3 ant-divider-horizontal my-0"
              role="separator"
            ></div>
            <div className="flex">
              <p className="py-4">
                <img src={audioIcon} alt="audio" />
              </p>
              <div className="py-2 flex-1">
                <StoryboardDialogues boardItem={boardItem} isEdit={false} />
              </div>
            </div>
          </div>
        </div>
      </div>
    </Card>
  );
};

export default BoardItem;
