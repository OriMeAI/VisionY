/**
 * 图标按钮组件
 */

import { Button } from "antd";

import React from "react";
import style from "./style.module.css";

interface IProps {
  handleClick: () => void;
  width?: number;
  height?: number;
  icon: string;
  disabled?: boolean;
}

const IconOnlyBtn: React.FC<IProps> = ({
  handleClick,
  width,
  height,
  icon,
  disabled,
}: IProps) => {
  return (
    <Button
      className={`bg-transparent border-none hover:bg-transparent ${style.iconOnlyBtnWrapper}`}
      size="large"
      onClick={handleClick}
      disabled={disabled}
      icon={
        <img width={width || 24} height={height || 24} src={icon} alt="" />
      }
    />
  );
};

export default IconOnlyBtn;
