
import {
  EditorApiContexts,
  IEditorApiContexts,
} from "./../../../../contexts/editor-api-contexts";
import {
  EditorContexts,
  IEditorContexts,
} from "./../../../../contexts/editor-contexts";
import {
  DEFAULT_BRUSH_SIZE,
  DEFAULT_ERASER_SIZE,
  DEFAULT_IMAGE_SIZE,
  DEFAULT_TOOL_ACTIVE_ID,
} from "../editor-config";
import stringUtils from "./../../../../libs/string-utils";
import * as React from "react";

interface IProps {
  children: React.ReactNode;
}

const EditorProvider: React.FC<IProps> = (props: IProps) => {
  // 当前选中的工具
  const [toolActiveId, setToolActiveId] = React.useState<number>(
    DEFAULT_TOOL_ACTIVE_ID
  );
  // 当前画笔大小
  const [brushSize, setBrushSize] = React.useState<number>(DEFAULT_BRUSH_SIZE);
  // 当前橡皮擦大小
  const [eraserSize, setEraserSize] =
    React.useState<number>(DEFAULT_ERASER_SIZE);
  // 当前图片大小
  const [imageSize, setImageSize] = React.useState<string>(DEFAULT_IMAGE_SIZE);
  // 初始化图片缩放比例
  const [initImageSize, setInitImageSize] = React.useState<number>(
    stringUtils.getNumByPercentStr(DEFAULT_IMAGE_SIZE)
  );
  const value = React.useMemo(
    () => ({
      toolActiveId,
      setToolActiveId,
      brushSize,
      setBrushSize,
      eraserSize,
      setEraserSize,
      imageSize,
      setImageSize,
      initImageSize,
      setInitImageSize,
    }),
    [toolActiveId, brushSize, imageSize, eraserSize, initImageSize]
  );
  return (
    <EditorApiContexts.Provider value={{} as IEditorApiContexts}>
      <EditorContexts.Provider value={value as IEditorContexts}>
        {props.children}
      </EditorContexts.Provider>
    </EditorApiContexts.Provider>
  );
};

export default EditorProvider;
