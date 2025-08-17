/**
 * 绘画工具栏
 */

import {
  EditorContexts,
  IEditorContexts,
} from "./../../../../contexts/editor-contexts";
import { TOOL_LIST } from "../editor-config";
import { Radio, RadioChangeEvent } from "antd";
import React, { useContext } from "react";
import ToolbarItem from "../ToolbarItem";
import style from "./style.module.css";
import { EditorToolItem } from "./../../../../libs/interfaces";
import { useTranslation } from "react-i18next";

const Toolbar: React.FC = () => {
  const {t} = useTranslation();

  //需要重新修改tool_list的tip
  const TOOL_TIP = [
  // {
  //   id: 1,
  //   tip: t("pointer_tool"),
  // },
  {
    id: 1,
    tip: t("gripper_tool"),
  },
  {
    id: 2,
    tip: t("brush_tool"),
  },
  {
    id: 3,
    tip: t("eraser_tool"),
  },
  {
    id: 4,
    tip: t("enlarge_tool"),
  },
  {
    id: 5,
    tip: t("lessen_tool"),
  },
];


  const editorContexts: IEditorContexts = useContext(EditorContexts);

  const onChange = (e: RadioChangeEvent) => {
    editorContexts.setToolActiveId(e.target.value);
  };
  return (
    <div className={style.topTools}>
      <Radio.Group
        value={editorContexts.toolActiveId}
        buttonStyle="solid"
        onChange={onChange}
      >
        {Array.isArray(TOOL_LIST) && TOOL_LIST.length > 0
          ? TOOL_LIST.map((toolItem: EditorToolItem, toolIndex: number) => {
            // 查找对应的工具提示
            const toolTip = TOOL_TIP.find((tip: any) => tip.id === toolItem.id);
            
            return (
              <ToolbarItem
                {...toolItem}
                // 如果找到对应的提示，则替换原来的tip
                tip={toolTip ? toolTip.tip : toolItem.tip}
                key={`tool_item_${toolItem.id}_${toolIndex}`}
              />
            );
          })
          : null}
      </Radio.Group>
    </div>
  );
};

export default Toolbar;
