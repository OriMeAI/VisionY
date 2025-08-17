/**
 * 单元格textarea输入框
 */

import { Input } from "antd";
import React, { ChangeEvent, FocusEvent, useContext } from "react";
import {
  DetailContexts,
  IDetailContexts,
} from "../../Common/DetailContainer/contexts/detail-contexts";
import dashboardApi from "./../../../../api/dashboardApi";
import { StoryHeadIdType } from "./../../../../libs/enums";

// 更新分镜表参数
import { CameraAngle, Dialogue, MainCharacter, SceneDescription, ShotResource, ShotTime, ShotType, ShotSize } from './../../../../types/storyboard';

interface IProps {
  cellValue: string;
  dataObj: ShotResource | SceneDescription | MainCharacter[] | ShotSize | CameraAngle | ShotType | ShotTime;
  valueKey: string;
  storyboardId: string;
  textareaWidth: number;
  textareaHeight: number;
}

const CellTextarea: React.FC<IProps> = ({
  cellValue,
  dataObj,
  valueKey,
  storyboardId,
  textareaWidth,
  textareaHeight,
}: IProps) => {
  const [currCellValue, setCurrCellValue] = React.useState<string>(cellValue);
  const detailContexts: IDetailContexts =
    useContext<IDetailContexts>(DetailContexts);
  const updateCellValue = async (value: string) => {
    const updatedDataObj = { ...dataObj, [valueKey]: value };
    const res = await dashboardApi.storyboardUpdate({
      projectId: detailContexts.projectItemObj?.id,
      storyboardId: storyboardId,
      data: updatedDataObj,
      updateType: "ShotTime"
    });
    if (res.success && res.result?.code === 0) {
    }
  };
  const handleChange = async (e: ChangeEvent<HTMLTextAreaElement>) => {
    setCurrCellValue(e.target.value);
  };
  const handleBlur = async (e: FocusEvent<HTMLTextAreaElement>) => {
    await updateCellValue(e.target.value);
  };
  return (
    <Input.TextArea
      value={currCellValue}
      onChange={handleChange}
      onBlur={handleBlur}
      className="overflow-y-auto border-none"
      style={{
        width: textareaWidth,
        overflowY: "hidden",
        resize: "none",
        height: textareaHeight,
        minHeight: 74,
        maxHeight: 184,
      }}
    />
  );
};

export default CellTextarea;
