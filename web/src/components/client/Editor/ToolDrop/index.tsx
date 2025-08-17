
import {
  EditorContexts,
  IEditorContexts,
} from "./../../../../contexts/editor-contexts";
import arrayUtils from "./../../../../libs/array-utils";
import {
  DEFAULT_BRUSH_SIZE,
  DEFAULT_ERASER_SIZE,
  MAX_BRUSH_SIZE,
  MAX_ERASER_SIZE,
  MIN_BRUSH_SIZE,
  MIN_ERASER_SIZE,
  TOOL_LIST,
} from "../editor-config";
import { ToolName } from "./../../../../libs/enums";
import React, { useContext, useEffect, useState } from "react";
import ToolDropItem from "../ToolDropItem";
import { useTranslation } from "react-i18next"; // 导入 useTranslation 钩子

interface IToolDropProps {}

const ToolDrop: React.FC<
  IToolDropProps
> = ({}: IToolDropProps) => {
  const { t } = useTranslation(); // 添加 useTranslation 钩子
  const editorContexts: IEditorContexts =
    useContext<IEditorContexts>(EditorContexts);

  const [currTool, setCurrTool] = useState(null);
  const onBrushSizeChange = (brushSize: number) => {
    editorContexts.setBrushSize(brushSize);
  };
  const onEraserSizeChange = (eraserSize: number) => {
    editorContexts.setEraserSize(eraserSize);
  };
  useEffect(() => {
    setCurrTool(
      arrayUtils.getRecordById(TOOL_LIST, "id", editorContexts.toolActiveId)
    );
  }, [editorContexts.toolActiveId]);
  return (
    <>
      {currTool?.name === ToolName.Brush ? (
        <ToolDropItem
          label={t("tool_drop_brush_size")} // 使用翻译键替换硬编码的中文
          minSize={MIN_BRUSH_SIZE}
          maxSize={MAX_BRUSH_SIZE}
          onSliderChange={onBrushSizeChange}
          defaultValue={DEFAULT_BRUSH_SIZE}
          value={editorContexts.brushSize}
        />
      ) : null}
      {currTool?.name === ToolName.Eraser ? (
        <ToolDropItem
          label={t("tool_drop_eraser_size")} // 使用翻译键替换硬编码的中文
          minSize={MIN_ERASER_SIZE}
          maxSize={MAX_ERASER_SIZE}
          onSliderChange={onEraserSizeChange}
          defaultValue={DEFAULT_ERASER_SIZE}
          value={editorContexts.eraserSize}
        />
      ) : null}
    </>
  );
};

export default ToolDrop;
