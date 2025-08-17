/**
 * 返回按钮及标题
 */

import { LeftOutlined } from "@ant-design/icons";
import React from "react";

interface IProps {
  title?: string;
  link?: string;
}

const DetailTitle: React.FC<IProps> = ({ title, link }: IProps) => {
  return (
    <div className="flex items-center">
      <a 
        href={link}  
        className="inline-block py-2 pr-5 pl-3 rounded-[40px] hover:text-[rgba(0,0,0,.88)] hover:bg-[rgba(0,0,0,0.04)]
         active:bg-[rgba(0,0,0,0.08)] transition-all duration-200 ease-in-out whitespace-nowrap"
      >
        <LeftOutlined className="align-middle" />
        <span  className="align-middle max-[980px]:hidden truncate min-w-40 max-w-56 ml-2 hover:text-[rgba(0,0,0,.88)]">
          {title}
        </span>
      </a>
    </div>
  );
};

export default DetailTitle;
