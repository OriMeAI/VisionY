/**
 * 图片组件
 */


import React from "react";

interface IProps {
  width?: number;
  height?: number;
  icon: string;
}

const NextImg: React.FC<IProps> = ({
  width,
  height,
  icon,
}: IProps) => {
  return <img width={width || 24} height={height || 24} src={icon} alt="" />;
};

export default NextImg;
