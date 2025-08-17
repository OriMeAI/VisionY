/**
 * 单元格下拉框
 */

import { Select, App } from "antd";
import React, { useContext } from "react";
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
import style from "./style.module.css";

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
  options: string[];
  selectWidth: number;
}

const CellSelect: React.FC<IProps> = ({
  cellValue,
  dataObj,
  valueKey,
  storyboardId,
  options,
  selectWidth,
}: IProps) => {
  const [currCellValue, setCurrCellValue] = React.useState<string>(cellValue);
  const detailContexts: IDetailContexts = useContext<IDetailContexts>(DetailContexts);
  const { message: messageApi } = App.useApp();
  const updateCellValue = async (value: string) => {

    // 获取选中值在options数组中的索引
    const selectedIndex = options.findIndex(option => option === value);
    
    // 构建要发送到服务器的对象，包含值和索引
    const updatedDataObj = { 
      "value": value,
      "value_index": selectedIndex !== -1 ? selectedIndex : 0 // 如果找不到索引，默认为0
    };

    const res = await dashboardApi.storyboardUpdate({
      projectId: detailContexts.projectItemObj?.id,
      storyboardId: storyboardId,
      data: updatedDataObj,
      updateType: valueKey
    });
    if (res.success && res.result?.code === 0) {
      setCurrCellValue(value);
    }else{
      messageApi.error(res.result?.msg);
    }
  };
  const handleChange = async (value: string) => {
    await updateCellValue(value);
  };
  return (
    <Select
      value={currCellValue}
      style={{ width: selectWidth }}
      onChange={handleChange}
      options={options.map((option) => ({ value: option, label: option }))}
      popupClassName={style.centeredSelectDropdown} // 下拉菜单使用居中样式
      className={style.centeredSelect} // 选择框使用居中样式
    />
  );
};

export default CellSelect;
