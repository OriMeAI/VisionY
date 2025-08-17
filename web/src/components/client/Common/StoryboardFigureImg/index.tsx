/**
 * 画面
 */

import { Spin, Tag } from "antd";

import { ShotResource, StoryboardShot } from "./../../../../types/storyboard";

import React, { useEffect, useState } from "react";
import { useTranslation } from "react-i18next"; // 添加 useTranslation 导入
import StoryboardEditBtns from "../StoryboardEditBtns";

interface IProps {
  boardItem: StoryboardShot;
  isEdit?: boolean;
}

const StoryboardFigureImg: React.FC<IProps> = React.memo(
  ({ boardItem, isEdit = true }: IProps) => {
    const { t } = useTranslation(); // 添加 useTranslation hook
    const [isRegenerating, setIsRegenerating] = useState<boolean>(false);
    const [loadingText, setLoadingText] = useState<string>( t("generating_high_definition_image"));

    const [resourceObj, setResourceObj] = useState<ShotResource>(boardItem.shot_resource);

    const setBoardLoadingText = (boardId:string,loadingText: string) => {
      setLoadingText(loadingText);
    }

    const setBoardIsRegenerating = (boardId:string,isRegenerating: boolean) => {
      setIsRegenerating(isRegenerating);
    }
    const setBoardShotResource = (boardId:string,resourceObj: ShotResource) => {
      setResourceObj(resourceObj);
    }

    useEffect(() => {
      setResourceObj(boardItem.shot_resource);
    }, [boardItem]);

    return (
      <div className="relative flex justify-center w-full h-[183px] cursor-default bg-black rounded">
        <div className="w-full h-[183px] overflow-hidden">
          <div>
            <Spin tip={loadingText} spinning={isRegenerating}>
              <img
                src={resourceObj.shot_resource_url}
                loading="lazy"
                alt={t("storyboard_image")}
                className="w-full h-[183px] object-contain aspect-[3/2]"
                draggable={false}
              />
              {resourceObj.is_HD ? (
                <Tag
                  className="absolute bottom-2 right-0 border-none"
                  style={{
                    background: "rgba(0, 0, 0, 0.4)",
                    backdropFilter: "blur(2px)",
                    color: "rgb(255, 255, 255)",
                  }}
                >
                  HD
                </Tag>
              ) : null}
            </Spin>
            <StoryboardEditBtns
              boardItem={boardItem}
              isEdit={isEdit}
              isRegenerating={isRegenerating}
              setBoardLoadingText={setBoardLoadingText}
              setBoardIsRegenerating={setBoardIsRegenerating}
              setBoardShotResource={setBoardShotResource}
            />
          </div>
        </div>
      </div>
    );
  }
);

export default StoryboardFigureImg;
