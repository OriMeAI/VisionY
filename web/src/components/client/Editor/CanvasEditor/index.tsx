/**
 * 局部重绘编辑页
 */
import {
  Button,
  Flex,
  Image,
  List,
  message,
  Spin,
  Tabs,
  TabsProps,
  Tooltip,
  App,
} from "antd";


import previewIcon from "./../../../../../assets/images/pages/boardView/preview_icon.svg";
import previewIconHover from "./../../../../../assets/images/pages/boardView/preview_icon_hover.svg";
import ImagePreview from "../../Common/ImagePreview";

import React, { useContext, useEffect, useState, useRef } from "react";
import { createPortal } from "react-dom";
import {
  DetailContexts,
  IDetailContexts,
} from "../../Common/DetailContainer/contexts/detail-contexts";
import DrawPanel from "../DrawPanel";
import editorApi from "../../../../api/editorApi";
import projectApi from "../../../../api/projectApi";
import { RepaintStatus } from "../../../../libs/enums";
import { ImageGenerateHistoryItem } from "../../../../libs/interfaces";
import EditorTopMenu from "./EditorTopMenu";
import style from "./style.module.css";

import { AppstoreOutlined, EyeOutlined } from "@ant-design/icons";
import { useTranslation } from "react-i18next";
import { useImmer } from "use-immer";
import {
  EditorApiContexts,
  IEditorApiContexts,
} from "../../../../contexts/editor-api-contexts";
import {
  EditorContexts,
  IEditorContexts,
} from "../../../../contexts/editor-contexts";
import {
  DEFAULT_BRUSH_SIZE,
  DEFAULT_ERASER_SIZE,
  DEFAULT_IMAGE_SIZE,
  DEFAULT_TOOL_ACTIVE_ID,
} from "../editor-config";
import stringUtils from "../../../../libs/string-utils";
import drawHelper from "../../../../libs/draw-helper";

interface IProps {
  storyboardId: string; // 故事板id
  outerHistoryItems: ImageGenerateHistoryItem[];
  applyHistoryImage: (resourceId: string) => void;
}

const CanvasEditor: React.FC<IProps> = ({
  storyboardId,
  outerHistoryItems,
  applyHistoryImage,
}: IProps) => {
  const { t } = useTranslation();
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
  const [repaintStatus, setRepaintStatus] = React.useState<RepaintStatus>(
    RepaintStatus.UnStart
  );
  // 引入useImmer解决对象不能及时更新的问题
  const [lines, setLines] = useImmer<any[]>([]);

  const [checkedImageGenerateHistory, setCheckedImageGenerateHistory] =
    useState<ImageGenerateHistoryItem>();
  // 预览图片
  const [previewImageVisible, setPreviewImageVisible] =
    React.useState<boolean>(false);

  const [storyboardShotDetailImg, setStoryboardShotDetailImg] =
    useState<string>("");

  // 添加一个状态来跟踪当前预览的图片
  const [previewImage, setPreviewImage] = useState<{
    id: string;
    url: string;
    alt: string;
  } | null>(null);

  //historyItems
  const [imageGenerateHistoryList, setImageGenerateHistoryList] =
    useState<ImageGenerateHistoryItem[]>(outerHistoryItems);

  //itemsKey
  const [itemKey, setItemKey] = useState<string>("1");

  // 添加一个 ref 来引用 scrollBar
  const scrollBarRef = useRef(null);

  // 获取 editorApiContexts
  const editorApiContexts = useContext(EditorApiContexts);

  const { message: messageApi } = App.useApp();

  // 清空画布，重置图片位置为初始位置
  const clearMaskCanvas = () => {
    setLines([]);
    // 重置图片位置为初始位置
    const newImageSize = stringUtils.getPercentStrByNum(initImageSize);
    setImageSize(newImageSize);
    editorApiContexts.onImageSizeChange(newImageSize);
  };

  // 在 checkedImageGenerateHistory 变化时滚动到对应元素
  useEffect(() => {
    if (checkedImageGenerateHistory) {
      const observer = new MutationObserver((mutations, obs) => {
        const element = document.getElementById(
          `history-item-${checkedImageGenerateHistory.id}`
        );
        if (element && scrollBarRef.current) {
          // 直接使用 DOM 元素的 scrollTo 方法
          scrollBarRef.current.scrollTo({
            top: element.offsetTop - 100,
            behavior: "smooth",
          });
          obs.disconnect(); // 停止观察
        }
      });

      observer.observe(document.body, {
        childList: true,
        subtree: true,
      });

      return () => observer.disconnect();
    }
  }, [checkedImageGenerateHistory]);

  // 监听 imageGenerateHistoryList 变化，更新 checkedImageGenerateHistory
  useEffect(() => {
    if (imageGenerateHistoryList && imageGenerateHistoryList.length > 0) {
      // 查找 selected 为 true 的项
      const selectedHistory = imageGenerateHistoryList.find(
        (history: ImageGenerateHistoryItem) => history.selected === true
      );

      // 如果找到了 selected 项，则更新 checkedImageGenerateHistory
      if (selectedHistory) {
        setCheckedImageGenerateHistory(selectedHistory);
        setStoryboardShotDetailImg(selectedHistory.url);
      } else if (
        imageGenerateHistoryList.length > 0 &&
        !checkedImageGenerateHistory
      ) {
        // 如果没有 selected 项但列表不为空，且当前没有选中项，则默认选择第一项
        setCheckedImageGenerateHistory(imageGenerateHistoryList[0]);
        setStoryboardShotDetailImg(imageGenerateHistoryList[0].url);
      }
    }

    //重置itemKey
    setItemKey((prevKey) => {
      // 生成一个随机数作为新的键
      const newKey = Math.random().toString(36).substring(2, 8);
      return newKey;
    });
  }, [imageGenerateHistoryList]);

  // 局部重绘结束后重新拉取图片历史
  const onRepaintSuccessCallback = async (
    historyItems: ImageGenerateHistoryItem[]
  ) => {
    setImageGenerateHistoryList(historyItems);
  };

  const historyHeight = 779;

  // const [historyHeight] = useState(() => {
  //   const winHeight = drawHelper.getWinH();
  //   // if (winHeight <= 833) return 521;
  //   // if (winHeight >= 1091) return 779;
  //   // return winHeight - 312;
  //   if (winHeight >= 1091) {
  //     return 779;
  //   }else{
  //     return 521;
  //   }
  // });
  const items: TabsProps["items"] = [
    {
      key: itemKey,
      label: t("synthesis_history"),
      children: (
        <div
          ref={scrollBarRef}
          className={`${style.synthesisHistory} overflow-y-auto bg-gray-100 rounded-md`}
          style={
            {
              "--history-height": `${historyHeight}px`,
            } as React.CSSProperties
          }
        >
          <List
            size="small"
            split={true}
            itemLayout="horizontal" // 或 "vertical"
            style={{ paddingTop: "8px" }}
          >
            {imageGenerateHistoryList.map(
              (item: ImageGenerateHistoryItem, index: number) => (
                <List.Item
                  key={item.id}
                  className="flex flex-row group bg-white"
                  id={`history-item-${item.id}`} // 这里设置了 ID
                  style={{
                    marginBottom: "8px", // 也可以使用内联样式
                    marginLeft: "8px", // 也可以使用内联样式
                    marginRight: "8px", // 也可以使用内联样式
                    padding: "8px", // 也可以使用内联样式
                    borderRadius: "8px", // 也可以使用内联样式
                    cursor: "pointer", // 也可以使用内联样式
                    border: checkedImageGenerateHistory?.id === item.id
                    ? "2px solid #7E2FFF"  // 选中项添加深紫色边框
                    : "2px solid transparent", // 非选中项添加透明边框保持布局一致
                  }}
                  onClick={(e: React.MouseEvent) => {
                    const target = e.target as Element;
                    // 检查点击是否在SVG元素上
                    if (
                      target.tagName.toLowerCase() === "svg" ||
                      target.tagName.toLowerCase() === "path"
                    ) {
                      return;
                    }
                    if (repaintStatus === RepaintStatus.Rendering) {
                      messageApi.info(t("resource_repainting"));
                    } else {
                      setToolActiveId(DEFAULT_TOOL_ACTIVE_ID);
                      setStoryboardShotDetailImg("");
                      setTimeout(() => {
                        clearMaskCanvas();
                        setCheckedImageGenerateHistory(item);
                        setRepaintStatus(RepaintStatus.UnStart);
                        setStoryboardShotDetailImg(item.url);
                      }, 10);
                    }
                  }}
                >
                  <div
                    className="w-7 flex text-base pl-[4px]"
                  >
                    {index + 1}
                  </div>
                  <div className="h-20 flex-1 overflow-hidden relative">
                    <div style={{ width: "100%", height: "100%" , }}>
                      <Image
                        placeholder={true}
                        src={item.url}
                        width="100%"
                        height="100%"
                        style={{ height: "100%", objectFit: "contain",backgroundColor: "bg-gray-100"}}
                        onClick={(e) => {
                          e.stopPropagation();
                        }}
                        preview={false} // 禁用内置预览功能
                      />
                    </div>
                    <div className="absolute top-0 left-0 w-full h-full bg-black bg-opacity-0 flex items-center justify-center group/div">
                      <div className="absolute top-0 right-0 flex items-center space-x-0.5 2xl:space-x-1 opacity-0 group-hover/div:opacity-100 transition-opacity duration-200">
                        <Tooltip placement="top" title={t("apply")}>
                          <Button
                            onClick={(e) => {
                              e.stopPropagation();
                              if (repaintStatus === RepaintStatus.Rendering) {
                                messageApi.info(t("resource_repainting"));
                              } else {
                                applyHistoryImage(item.id);
                              }
                            }}
                            className="disabled:bg-white/70 bg-white/80 group/apply"
                            icon={
                              <div className="relative w-6 h-6">
                                <AppstoreOutlined className="absolute top-1/2 -translate-y-1/2 left-1/2 -translate-x-1/2 inset-0 m-auto transition-opacity duration-200 group-hover/apply:opacity-0" />
                                <AppstoreOutlined className="absolute top-1/2 -translate-y-1/2 left-1/2 -translate-x-1/2 inset-0 m-auto opacity-0 transition-opacity duration-200 group-hover/apply:opacity-100" />
                              </div>
                            }
                          />
                        </Tooltip>

                        <Tooltip placement="top" title={t("view_large_image")}>
                          <Button
                            onClick={(e) => {
                              e.stopPropagation();
                              // 设置当前预览的图片
                              setPreviewImage({
                                id: item.id,
                                url: item.url,
                                alt: "",
                              });
                              // 打开预览
                              setPreviewImageVisible(true);
                            }}
                            className="disabled:bg-white/70 bg-white/80 group/view"
                            icon={
                              <div className="relative w-6 h-6">
                                <img
                                  src={previewIcon}
                                  alt="history"
                                  className="absolute top-1/2 -translate-y-1/2 left-1/2 -translate-x-1/2 inset-0 opacity-100 transition-opacity duration-200 group-hover/view:opacity-0"
                                />
                                <img
                                  src={previewIconHover}
                                  alt="history hover"
                                  className="absolute top-1/2 -translate-y-1/2 left-1/2 -translate-x-1/2 inset-0 opacity-0 transition-opacity duration-200 group-hover/view:opacity-100"
                                />
                              </div>
                            }
                          />
                        </Tooltip>
                      </div>
                    </div>
                  </div>
                </List.Item>
              )
            )}
          </List>
        </div>
      ),
    },
  ];

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
      repaintStatus,
      setRepaintStatus,
    }),
    [
      toolActiveId,
      brushSize,
      imageSize,
      eraserSize,
      initImageSize,
      repaintStatus,
    ]
  );

  return (
    <EditorContexts.Provider value={value as IEditorContexts}>
      <div className="overflow-hidden">
        <div className="w-full flex transition-opacity duration-100 opacity-100">
          <div className={style.storyboardX}>
            <EditorTopMenu repaintStatus={repaintStatus} />

            <Flex>
              <DrawPanel
                storyboardId={storyboardId}
                storyboardShotDetailImg={storyboardShotDetailImg}
                lines={lines}
                setLines={setLines}
                clearMaskCanvas={clearMaskCanvas}
                onRepaintSuccessCallback={onRepaintSuccessCallback}
              />
            </Flex>
          </div>
          <div className={style.rightSide}>
            <div className={style.inner}>
              <Tabs
                defaultActiveKey={itemKey}
                items={items}
                className={style.customTabs}
              />
            </div>
          </div>
        </div>

        {/* 单一的 ImagePreview 组件 */}
        {createPortal(
          <ImagePreview
            imageList={
              previewImage
                ? [
                    {
                      id: previewImage.id,
                      src: previewImage.url,
                      alt: previewImage.alt || "",
                    },
                  ]
                : []
            }
            current={0}
            previewImageVisible={previewImageVisible}
            setPreviewImageVisible={setPreviewImageVisible}
          />,
          document.body
        )}
      </div>
    </EditorContexts.Provider>
  );
};

export default CanvasEditor;
