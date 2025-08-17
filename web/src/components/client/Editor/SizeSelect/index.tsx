/**
 * 编辑页工具栏尺寸选择下拉框
 */

import {
  EditorApiContexts,
  IEditorApiContexts,
} from "./../../../../contexts/editor-api-contexts";
import {
  EditorContexts,
  IEditorContexts,
} from "./../../../../contexts/editor-contexts";
import {
  DEFAULT_IMAGE_SIZE,
} from "../editor-config";
import stringUtils from "./../../../../libs/string-utils";
import { Select } from "antd";
import React, { useContext } from "react";
import { useTranslation } from "react-i18next";

const SizeSelect: React.FC = () => {
  const {t} = useTranslation();
  // 编辑页工具栏图片尺寸选择下拉框列表
  const IMAGE_SIZE_SELECT_OPTIONS = [
    { value: "reset", label: t("reset") },
    { value: "20%", label: "20%" },
    { value: "50%", label: "50%" },
    { value: "100%", label: "100%" },
    { value: "150%", label: "150%" },
    { value: "200%", label: "200%" },
    { value: "300%", label: "300%" },
  ];

  const editorContexts: IEditorContexts = useContext<IEditorContexts>(EditorContexts);
  const editorApiContexts: IEditorApiContexts = useContext(EditorApiContexts);

  const onImageSizeChange = (imageSize: string) => {
    const newImageSize =
      imageSize === "reset"
        ? stringUtils.getPercentStrByNum(editorContexts.initImageSize)
        : imageSize;

    editorContexts.setImageSize(newImageSize);
    editorApiContexts.onImageSizeChange(newImageSize);
  };

  return (
    <Select
      value={editorContexts.imageSize}
      defaultValue={DEFAULT_IMAGE_SIZE}
      style={{ width: 120 }}
      onChange={onImageSizeChange}
      options={IMAGE_SIZE_SELECT_OPTIONS}
    />
  );
};

export default SizeSelect;
