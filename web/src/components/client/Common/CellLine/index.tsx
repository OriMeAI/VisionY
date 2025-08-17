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


interface IProps {
  cellValue: string;
  storyboardId: string;
  textareaWidth: number;
  textareaHeight: number;
}

const CellLine: React.FC<IProps> = ({
  cellValue,
  storyboardId,
  textareaWidth,
  textareaHeight,
}: IProps) => {
  const [currCellValue, setCurrCellValue] = React.useState<string>(cellValue);
  const detailContexts: IDetailContexts =
    useContext<IDetailContexts>(DetailContexts);
  const updateCellValue = async (value: string) => {
    const res = await dashboardApi.storyboardUpdate({
      projectId: detailContexts.projectItemObj?.id,
      storyboardId: storyboardId,
      data: value,
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
        resize: "none",
        height: textareaHeight,
        minHeight: 74,
        maxHeight: 184,
      }}
    />
  );
};

export default CellLine;
