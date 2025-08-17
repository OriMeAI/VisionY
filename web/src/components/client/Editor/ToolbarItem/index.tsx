/**
 * 绘画工具项
 */

import {
  EditorContexts,
  IEditorContexts,
} from "./../../../../contexts/editor-contexts";
import { Radio, Tooltip } from "antd";

import React, { useContext, useState } from "react";
import style from "./style.module.css";

interface IToolbarItemProps {
  id: number;
  tip?: string;
  icon: string;
  name: string;
  hoverIcon?: string;
  activeIcon?: string;
}

const ToolbarItem: React.FC<IToolbarItemProps> = ({
  id,
  tip,
  icon,
  name,
  hoverIcon = "",
  activeIcon = "",
}: IToolbarItemProps) => {
  const editorContexts: IEditorContexts = useContext(EditorContexts);

  return (
    <Radio.Button
      value={id}
      className={style.toolbarItemWrapper}
    >
      <Tooltip placement="top" title={tip}>
        <div className="relative w-6 h-6">
          <img
            src={editorContexts.toolActiveId === id ? activeIcon : icon}
            alt={name}
            className="absolute top-1/2 -translate-y-1/2 left-1/2 -translate-x-1/2 inset-0 transition-opacity duration-200 group-hover:opacity-0"
          />
          <img
            src={hoverIcon}
            alt={`${name} hover`}
            className="absolute top-1/2 -translate-y-1/2 left-1/2 -translate-x-1/2 inset-0 opacity-0 transition-opacity duration-200 group-hover:opacity-100"
          />
        </div>
      </Tooltip>
    </Radio.Button>
  );
};

export default ToolbarItem;
