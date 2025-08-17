/**
 * 单元格数字输入框
 */

import { Input, App } from "antd";
import React, { ChangeEvent, FocusEvent, useContext } from "react";
import {
  DetailContexts,
  IDetailContexts,
} from "../../Common/DetailContainer/contexts/detail-contexts";
import dashboardApi from "./../../../../api/dashboardApi";
import {
  CameraAngle,
  MainCharacter,
  SceneDescription,
  ShotResource,
  ShotTime,
  ShotType,
  ShotSize,
} from "./../../../../types/storyboard";

interface IProps {
  cellValue: string;
  dataObj:
    | ShotResource
    | SceneDescription
    | MainCharacter[]
    | ShotSize
    | CameraAngle
    | ShotType
    | ShotTime;
  valueKey: string;
  storyboardId: string;
  inputWidth: number;
}

const CellInputNumber: React.FC<IProps> = ({
  cellValue,
  dataObj,
  valueKey,
  storyboardId,
  inputWidth,
}: IProps) => {
  const [currCellValue, setCurrCellValue] = React.useState<string>(cellValue);
  const [defaultCellValue, setDefaultCellValue] = React.useState<string>(cellValue);

  const detailContexts: IDetailContexts = useContext<IDetailContexts>(DetailContexts);
  const { message: messageApi } = App.useApp();
  const updateCellValue = async (value: string) => {
    const updatedDataObj = { "value": value };
    const res = await dashboardApi.storyboardUpdate({
      projectId: detailContexts.projectItemObj?.id,
      storyboardId: storyboardId,
      data: updatedDataObj,
      updateType: valueKey
    });
    if (res.success && res.result?.code === 0) {
      // 更新成功后，将新值设为默认值
      setDefaultCellValue(value);
    } else {
      messageApi.error(res.result?.msg);
    }
  };
  const handleChange = async (e: ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    // 只允许输入大于1的正整数
    if (value === "" || (/^\d+$/.test(value) && parseInt(value) >= 1)) {
      setCurrCellValue(value);
    }
  };
  const handleBlur = async (e: FocusEvent<HTMLInputElement>) => {
    const value = e.target.value;
    // 如果为空或不是有效的正整数，设置为1
    if (value === "" || !/^\d+$/.test(value) || parseInt(value) < 1) {
      setCurrCellValue(defaultCellValue);
    } else if (String(value) !== String(defaultCellValue)) {
      // 只有当值发生变化时，才更新到服务器
      await updateCellValue(value);
    }
  };
  return (
    <Input
      value={currCellValue}
      style={{ width: inputWidth,textAlign: 'center' }}
      onChange={handleChange}
      onBlur={handleBlur}
    />
  );
};

export default CellInputNumber;
