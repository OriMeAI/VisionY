
import { Flex } from "antd";
import React from "react";
import SyncSliderInput from "../../Common/SyncSliderInput";
import style from "./style.module.css";

interface IToolDropItemProps {
  label?: string;
  minSize?: number;
  maxSize?: number;
  onSliderChange?: (newValue: number) => void;
  defaultValue?: number;
  value?: number;
}

const ToolDropItem: React.FC<IToolDropItemProps> = ({
  label,
  minSize,
  maxSize,
  onSliderChange,
  defaultValue,
  value,
}: IToolDropItemProps) => {
  return (
    <Flex className={style.topToolsDrop}>
      <label>{label}</label>
      <SyncSliderInput
        min={minSize}
        max={maxSize}
        step={1}
        onSliderChange={onSliderChange}
        defaultValue={defaultValue}
        value={value}
      />
    </Flex>
  );
};

export default ToolDropItem;
