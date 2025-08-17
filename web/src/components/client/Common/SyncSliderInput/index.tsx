/**
 * 通用组件：滑块输入框联动组件
 */

import { useValueChange } from "./../../../../hooks/useValueChange";
import { Flex, InputNumber, Slider } from "antd";
import React, { useEffect } from "react";
import style from "./style.module.css";
interface ISyncSliderInputProps {
  defaultValue?: number;
  value?: number;
  min?: number;
  max?: number;
  step?: number;
  onSliderChange?: (value: number) => void;
}

const SyncSliderInput: React.FC<ISyncSliderInputProps> = ({
  defaultValue,
  value,
  min,
  max,
  step,
  onSliderChange,
}: ISyncSliderInputProps) => {
  const [inputValue, onInputValueChange, setInputValue] =
    useValueChange<number>(defaultValue || 0);

  const onChange = (newValue: number) => {
    onSliderChange && onSliderChange(newValue);
    onInputValueChange(newValue);
  };

  useEffect(() => {
    if (undefined !== value) {
      setInputValue(value);
    }
  }, [value]);
  return (
    <Flex className={style.syncSliderInputWrapper}>
      <Slider
        min={min || 1}
        max={max || 10}
        onChange={onChange}
        value={typeof inputValue === "number" ? inputValue : 0}
        step={step || 1}
      />
      <InputNumber
        min={min || 1}
        max={max || 10}
        style={{
          margin: "4px 16px",
          width: 60,
          height: 28,
          display: "flex",
          alignItems: "center",
          border: "1px solid #d9d9d9",
          borderRadius: 3,
        }}
        value={typeof inputValue === "number" ? inputValue : 0}
        onChange={onChange}
        step={step || 1}
      />
    </Flex>
  );
};

export default SyncSliderInput;
