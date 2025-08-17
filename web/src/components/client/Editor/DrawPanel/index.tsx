/**
 * 局部重绘面板
 */
"use client";
import { Spin } from "antd";
import Konva from "konva";
import React, {
  Fragment,
  RefObject,
  useCallback,
  useContext,
  useEffect,
  useRef,
  useState,
} from "react";
import { useTranslation } from "react-i18next";
import { Circle, Image, Layer, Line, Rect, Stage } from "react-konva";
import useImage from "use-image";
import BottomTools from "../BottomTools";
import {
  DEFAULT_BRUSH_SIZE,
  DEFAULT_IMAGE_INIT_SCALE,
  DEFAULT_IMAGE_POS_X,
  DEFAULT_IMAGE_POS_Y,
  TOOL_LIST,
} from "../editor-config";
import {
  EditorApiContexts,
  IEditorApiContexts,
} from "./../../../../contexts/editor-api-contexts";
import {
  EditorContexts,
  IEditorContexts,
} from "./../../../../contexts/editor-contexts";
import arrayUtils from "./../../../../libs/array-utils";
import drawHelper from "./../../../../libs/draw-helper";
import { MinSide, RepaintStatus, ToolName } from "./../../../../libs/enums";
import imageHelper from "./../../../../libs/image-helper";
import { EditorToolItem } from "./../../../../libs/interfaces";
import stringUtils from "./../../../../libs/string-utils";
import style from "./style.module.css";

import { ImageGenerateHistoryItem } from "../../../../libs/interfaces";

interface IProps {
  storyboardShotDetailImg: string; // 故事板详情图片
  storyboardId: string; // 故事板id
  lines: any[];
  setLines: (draft: any) => void;
  clearMaskCanvas: () => void;
  onRepaintSuccessCallback?: (historyItems: ImageGenerateHistoryItem[]) => void;
}

const DrawPanel: React.FC<IProps> = ({
  storyboardShotDetailImg,
  storyboardId,
  lines,
  setLines,
  clearMaskCanvas,
  onRepaintSuccessCallback,
}: IProps) => {
  const { t } = useTranslation();
  const editorContexts: IEditorContexts = useContext(EditorContexts);

  const editorEditorApiContexts: IEditorApiContexts =
    useContext(EditorApiContexts);
  // 原始图片
  const [editorImgSrc, setEditorImgSrc] = useState<string>(
    storyboardShotDetailImg
  );
  useEffect(() => {
    setEditorImgSrc(storyboardShotDetailImg);
  }, [storyboardShotDetailImg]);
  const [stageCursorStyle, setStageCursorStyle] = useState<string>("");
  // 舞台是否可拖动
  const [draggable, setDraggable] = useState<boolean>(false);
  // 舞台尺寸自适应屏幕大小

  const containerRef = useRef<HTMLDivElement>(null);

  const [stageWidth, setStageWidth] = useState<number>(0);
  const [stageHeight, setStageHeight] = useState<number>(0);
  const [imageWidth, setImageWidth] = useState<number>(0);
  const [imageHeight, setImageHeight] = useState<number>(0);
  const originImageWidth = useRef<number>(0);
  const originImageHeight = useRef<number>(0);
  const originImagePosX = useRef<number>(0);
  const originImagePosY = useRef<number>(0);
  const minSide = useRef<MinSide>(MinSide.Width);
  // 图片尺寸大小（注意：这里是画布中的缩放比例，与下拉框的图片百分比不一样，下拉框的图片百分比是相对原始图片尺寸而言的，这里的百分比是相对于画布初始化时的图片大小而言的）
  const [currScale, setCurrScale] = useState<number>(DEFAULT_IMAGE_INIT_SCALE);
  const initScale = useRef<number>(DEFAULT_IMAGE_INIT_SCALE);

  const modalWidth = 1400;
  const modalHeight = 1091
  // const [modalWidth] = useState(() => {
  //   const winWidth = drawHelper.getWinW();
  //   if (winWidth <= 1024) return 1024;
  //   if (winWidth >= 1400) return 1400;
  //   return winWidth;
  // });
  // const [modalHeight] = useState(() => {
  //   const winHeight = drawHelper.getWinH();
  //   if (winHeight <= 833) return 833;
  //   if (winHeight >= 1091) return 1091;
  //   return winHeight;
  // });
  const containerWidth: number = modalWidth - 272;
  let initImageWidth: number = containerWidth - DEFAULT_IMAGE_POS_X * 2;
  const initCalImageHeight: number =
    modalHeight - 310 - DEFAULT_IMAGE_POS_Y * 2;
  let initImageHeight: number =
    initCalImageHeight > 480 ? initCalImageHeight : 480;
  const fitStageIntoParentContainer = async () => {
    const calContainerWidth: number = modalWidth - 272;
    const calContainerHeight: number = modalHeight - 310;
    // 改成弹窗后宽度固定
    setStageWidth(calContainerWidth);
    setStageHeight(calContainerHeight);
    // calculateScale();
    setPosX(0);
    setPosY(0);
  };

  // 计算图片缩放比例
  const calculateScale = async () => {
    editorContexts.setRepaintStatus(RepaintStatus.Loading);
    // 通过预加载图片获取图片的原始宽高
    const { width, height } = await imageHelper.preloadImage(
      storyboardShotDetailImg
    );

    originImageWidth.current = width;
    originImageHeight.current = height;
    let scale: number = 1;
    if (width && height) {
      // 初始化时候以宽高比例中较小的为准，以确保初始化时在屏幕中能显示完整图片
      const widthScale = initImageWidth / width;
      const heightScale = initImageHeight / height;
      if (widthScale < heightScale) {
        scale = Number(widthScale.toFixed(2));
      } else {
        scale = Number(heightScale.toFixed(2));
        minSide.current = MinSide.Height;
      }
      // scale = Number(
      //   Math.min(initImageWidth / width, initImageHeight / height).toFixed(2)
      // );
      const newImageSize = stringUtils.getPercentStrByNum(scale);
      editorContexts.setImageSize(newImageSize);
      let newCurrScale: number = 1;
      if (widthScale < heightScale) {
        newCurrScale =
          (stringUtils.getNumByPercentStr(newImageSize) *
            originImageWidth.current) /
          (imageWidth || 1); // 防止除以0
      } else {
        newCurrScale =
          (stringUtils.getNumByPercentStr(newImageSize) *
            originImageHeight.current) /
          (imageHeight || 1); // 防止除以0
      }
      // 确保 newCurrScale 是有效数值
      newCurrScale = isFinite(newCurrScale) ? newCurrScale : 1;
      setCurrScale(newCurrScale);
      initScale.current = newCurrScale;
      editorContexts.setInitImageSize(scale);
    }
    const newImageWidth = Math.round(width * scale);
    const newImageHeight = Math.round(height * scale);
    setImageWidth(newImageWidth);
    setImageHeight(newImageHeight);
    const stageCalHeight: number = modalHeight - 310;
    originImagePosX.current = (containerWidth - newImageWidth) / 2;
    originImagePosY.current = (stageCalHeight - newImageHeight) / 2;

    editorContexts.setRepaintStatus(RepaintStatus.UnStart);
  };

  useEffect(() => {
    (async () => {
      if (typeof window !== "undefined") {
        editorContexts.setRepaintStatus(RepaintStatus.Loading);
        await fitStageIntoParentContainer();
      }
    })();
  }, []); // 只在组件挂载时执行一次

  useEffect(() => {
    if (storyboardShotDetailImg) {
      calculateScale();
    }
  }, [storyboardShotDetailImg]); // 只在 storyboardShotDetailImg 变化时执行
  // 图片x轴坐标
  const [posX, setPosX] = useState<number>(0);
  // 图片y轴坐标
  const [posY, setPosY] = useState<number>(0);
  // 画笔/橡皮擦尺寸
  const [strokeWidth, setStrokeWidth] = useState<number>(DEFAULT_BRUSH_SIZE);
  const stageRef: RefObject<Konva.Stage> = useRef(null);
  const originStageRef: RefObject<Konva.Stage> = useRef(null);
  const originLayerRef: RefObject<Konva.Layer> = useRef(null);
  const maskLayerRef: RefObject<Konva.Layer> = useRef(null);
  const isDrawing = useRef(false);
  const [currTool, setCurrTool] = useState<EditorToolItem | null>(null);

  const [circlePos, setCirclePos] = useState({ x: 0, y: 0 });
  // 通过缩放比例计算stage平移位置(以点击时的鼠标位置为基准点)
  const calculateImagePos = (oldScale: number, newCurrScale: number) => {
    const stage = stageRef.current;
    const pointer = stage.getPointerPosition();

    const mousePointTo = {
      x: (pointer.x - stage.x()) / oldScale,
      y: (pointer.y - stage.y()) / oldScale,
    };
    setPosX(pointer.x - mousePointTo.x * newCurrScale);
    setPosY(pointer.y - mousePointTo.y * newCurrScale);
  };
  // 添加防抖函数
  const debounceRAF = (callback: () => void) => {
    let frameId: number | null = null;
    return () => {
      if (frameId) {
        return;
      }
      frameId = requestAnimationFrame(() => {
        callback();
        frameId = null;
      });
    };
  };

  // 优化 getRelativePointerPosition 函数的性能
  const getRelativePointerPosition = useCallback((node: Konva.Layer) => {
    if (!node) return { x: 0, y: 0 };
    // 缓存 transform 对象
    const transform = node.getAbsoluteTransform().copy();
    transform.invert();
    const pos = node.getStage()?.getPointerPosition() || { x: 0, y: 0 };
    return transform.point(pos);
  }, []);

  // 优化 Circle 位置更新
  const updateCirclePosition = useCallback(
    (layer: Konva.Layer) => {
      const point = getRelativePointerPosition(layer);
      setCirclePos(point);
    },
    [getRelativePointerPosition]
  );

  // 工具栏操作
  const toolOperationMaps = {
    // [ToolName.Pointer]: {
    //   onToolChange: () => {
    //     isDrawing.current = false;
    //     setStageCursorStyle(style.cursorDefault);
    //     setDraggable(false);
    //   },
    //   onMouseMove: () => {},
    //   onClick: () => {},
    // },
    [ToolName.Gripper]: {
      onToolChange: () => {
        isDrawing.current = false;
        setStageCursorStyle(style.cursorGripper);
        setDraggable(true);
      },
      onMouseMove: () => {},
      onClick: () => {},
    },
    [ToolName.Brush]: {
      onToolChange: () => {
        isDrawing.current = false;
        setStageCursorStyle(style.cursorDefault);
        setDraggable(false);
        setTool(ToolName.Brush);
        setStrokeWidth(editorContexts.brushSize);
      },
      onMouseMove: () => {
        const layer = maskLayerRef.current;
        if (!layer) return;

        // 直接更新圆圈位置，不使用 debounce
        updateCirclePosition(layer);

        if (!isDrawing.current) return;

        // 绘制线条时使用 debounce
        requestAnimationFrame(() => {
          const point = getRelativePointerPosition(layer);
          setLines((draft: any) => {
            const lastLine = draft[draft.length - 1];
            lastLine.points = lastLine.points.concat([point.x, point.y]);
          });
        });
      },
      onClick: () => {},
    },
    [ToolName.Eraser]: {
      onToolChange: () => {
        isDrawing.current = false;
        setStageCursorStyle(style.cursorDefault);
        setDraggable(false);
        setTool(ToolName.Eraser);
        setStrokeWidth(editorContexts.eraserSize);
      },
      onMouseMove: debounceRAF(() => {
        const layer = maskLayerRef.current;
        if (!layer) return;

        const point = getRelativePointerPosition(layer);
        setCirclePos(point);

        if (!isDrawing.current) return;

        setLines((draft: any) => {
          const lastLine = draft[draft.length - 1];
          lastLine.points = lastLine.points.concat([point.x, point.y]);
          draft.splice(draft.length - 1, 1, lastLine);
        });
      }),
      onClick: () => {}, // Add the missing onClick handler
    },
    [ToolName.Enlarge]: {
      onToolChange: () => {
        isDrawing.current = false;
        setStageCursorStyle(style.cursorEnlarge);
        setDraggable(false);
      },
      onMouseMove: () => {},
      onClick: () => {
        if (stringUtils.getNumByPercentStr(editorContexts.imageSize) < 3) {
          const nextCurrScale = currScale * 1.2;
          let newImageSize = Number(
            ((imageWidth * nextCurrScale) / originImageWidth.current).toFixed(2)
          );

          const newCurrScale =
            newImageSize > 3
              ? (3 * originImageWidth.current) / imageWidth
              : nextCurrScale;
          calculateImagePos(currScale, newCurrScale);
          setCurrScale(newCurrScale);
          editorContexts.setImageSize(
            stringUtils.getPercentStrByNum(newImageSize > 3 ? 3 : newImageSize)
          );
        }
      },
    },
    [ToolName.Lessen]: {
      onToolChange: () => {
        isDrawing.current = false;
        setStageCursorStyle(style.cursorLessen);
        setDraggable(false);
      },
      onMouseMove: () => {},
      onClick: () => {
        if (stringUtils.getNumByPercentStr(editorContexts.imageSize) > 0.2) {
          const nextCurrScale = currScale * 0.8;
          let newImageSize = Number(
            ((imageWidth * nextCurrScale) / originImageWidth.current).toFixed(2)
          );

          const newCurrScale =
            nextCurrScale < 0.2
              ? (0.2 * originImageWidth.current) / imageWidth
              : nextCurrScale;
          calculateImagePos(currScale, newCurrScale);
          setCurrScale(newCurrScale);
          editorContexts.setImageSize(
            stringUtils.getPercentStrByNum(
              newImageSize < 0.2 ? 0.2 : newImageSize
            )
          );
        }
      },
    },
  };

  useEffect(() => {
    const newImageSize = stringUtils.getNumByPercentStr(
      editorContexts.imageSize
    );
    let newCurrScale = 1;
    if (minSide.current === MinSide.Width) {
      newCurrScale =
        (newImageSize * originImageWidth.current) / (imageWidth || 1);
    } else {
      newCurrScale =
        (newImageSize * originImageHeight.current) / (imageHeight || 1);
    }
    // 确保 newCurrScale 是有效数值
    newCurrScale = isFinite(newCurrScale) ? newCurrScale : 1;
    setCurrScale(newCurrScale);
  }, [editorContexts.imageSize]);
  // 仅在通过下拉框切换缩放比例时才调整坐标,将位置居中
  editorEditorApiContexts.onImageSizeChange = (imageSize: string) => {
    const newImageSize = stringUtils.getNumByPercentStr(imageSize);
    const stage = stageRef.current;
    let newCurrScale = 1;
    if (minSide.current === MinSide.Width) {
      newCurrScale =
        (newImageSize * originImageWidth.current) / (imageWidth || 1);
    } else {
      newCurrScale =
        (newImageSize * originImageHeight.current) / (imageHeight || 1);
    }
    newCurrScale = isFinite(newCurrScale) ? newCurrScale : 1;

    // 计算缩放后的图片尺寸
    const scaledImageWidth = imageWidth * newCurrScale;
    const scaledImageHeight = imageHeight * newCurrScale;

    const stageCalHeight: number = modalHeight - 310;
    // 计算图片在舞台中的居中位置
    originImagePosX.current =
      (containerWidth - scaledImageWidth) / (2 * newCurrScale);
    originImagePosY.current =
      (stageCalHeight - scaledImageHeight) / (2 * newCurrScale);

    // 重置舞台位置
    stage.x(0);
    stage.y(0);
    setPosX(0);
    setPosY(0);

    // 更新缩放比例
    setCurrScale(newCurrScale);

    // 强制重新渲染
    requestAnimationFrame(() => {
      stage.batchDraw();
    });
  };
  useEffect(() => {
    if (currTool?.name === ToolName.Brush) {
      setStrokeWidth(editorContexts.brushSize);
    }
  }, [editorContexts.brushSize]);
  useEffect(() => {
    if (currTool?.name === ToolName.Eraser) {
      setStrokeWidth(editorContexts.eraserSize);
    }
  }, [editorContexts.eraserSize]);
  useEffect(() => {
    const tempCurrTool: EditorToolItem = arrayUtils.getRecordById(
      TOOL_LIST,
      "id",
      editorContexts.toolActiveId
    );
    setCurrTool(tempCurrTool);
    toolOperationMaps[tempCurrTool.name].onToolChange();
  }, [editorContexts.toolActiveId]);
  const [tool, setTool] = useState(ToolName.Brush);
  const [image] = useImage(editorImgSrc, "anonymous");

  const handleMouseDown = () => {
    isDrawing.current = true;
    const layer = maskLayerRef.current;
    const pos = getRelativePointerPosition(layer);
    // setLines([...lines, { tool, strokeWidth, points: [pos.x, pos.y] }]);
    setLines((draft: any) => {
      draft.push({ tool, strokeWidth, points: [pos.x, pos.y] });
    });
  };

  const handleMouseMove = () => {
    toolOperationMaps[currTool?.name].onMouseMove();
  };

  const handleMouseUp = () => {
    isDrawing.current = false;
  };
  const onRepaintSuccess = (historyItems: ImageGenerateHistoryItem[]) => {
    clearMaskCanvas();
    onRepaintSuccessCallback && onRepaintSuccessCallback(historyItems);
  };
  // ... 在其他 state 声明后添加
  const handleDragMove = (e: Konva.KonvaEventObject<DragEvent>) => {
    setPosX(e.target.x());
    setPosY(e.target.y());
  };
  return (
    <div>
      <Spin
        spinning={
          editorContexts.repaintStatus === RepaintStatus.Rendering ||
          editorContexts.repaintStatus === RepaintStatus.Loading
        }
        tip={
          editorContexts.repaintStatus === RepaintStatus.Rendering
            ? t("resource_repainting")
            : editorContexts.repaintStatus === RepaintStatus.Loading
            ? t("resource_loading")
            : ""
        }
        style={{ height: "100%", maxHeight: "none" }} // Override max-height
      >
        <div
          ref={containerRef}
          className={`bg-black relative rounded-lg ${style.drawPanelWrapper}`}
        >
          {/* 原始stage，用来最终生成黑白图像，页面不可见，因为当我们对stage做平移，缩放操作时候，canvas的宽高不会跟着改变，因此生成黑白图像时候会导致数据丢失，此stage专门用来存储画笔绘制路径的原始数据，使之不会因为用户手动的平移缩放操作导致数据丢失 */}
          <Stage
            ref={originStageRef}
            width={imageWidth}
            height={imageHeight}
            style={{ display: "none" }}
          >
            <Layer ref={originLayerRef} id="originMaskLayer">
              {lines.map((line, i) => (
                <Fragment key={i}>
                  {/* 每绘制一条新的Line，都会生成两个Line，一个用于擦除，一个用于绘制，目的是为了解决绘制多条线时候透明度重叠的问题 */}
                  {line.tool === ToolName.Brush ? (
                    <Line
                      points={line.points}
                      stroke={"white"}
                      strokeWidth={line.strokeWidth}
                      tension={0.5}
                      lineCap="round"
                      lineJoin="round"
                      globalCompositeOperation={"destination-out"}
                    />
                  ) : null}
                  <Line
                    points={line.points}
                    stroke={
                      line.tool === ToolName.Eraser
                        ? "white"
                        : "rgb(104, 58, 205, .3)"
                    }
                    strokeWidth={line.strokeWidth}
                    tension={0.5}
                    lineCap="round"
                    lineJoin="round"
                    globalCompositeOperation={
                      line.tool === ToolName.Eraser
                        ? "destination-out"
                        : "source-over"
                    }
                  />
                </Fragment>
              ))}
            </Layer>
          </Stage>
          <Stage
            ref={stageRef}
            width={stageWidth}
            height={stageHeight}
            x={posX}
            y={posY}
            onClick={
              currTool?.name
                ? toolOperationMaps[currTool.name].onClick
                : () => {}
            }
            className={`${stageCursorStyle}`}
            draggable={draggable}
            onDragMove={handleDragMove}
            scaleX={isFinite(currScale) ? currScale : 1}
            scaleY={isFinite(currScale) ? currScale : 1}
          >
            <Layer>
              <Image
                image={image}
                width={imageWidth}
                height={imageHeight}
                x={originImagePosX.current}
                y={originImagePosY.current}
              />
            </Layer>
            <Layer
              ref={maskLayerRef}
              clip={{
                x: 0,
                y: 0,
                width: imageWidth,
                height: imageHeight,
              }}
              x={originImagePosX.current}
              y={originImagePosY.current}
              onMouseDown={handleMouseDown}
              onMouseMove={handleMouseMove}
              onMouseUp={handleMouseUp}
            >
              <Rect width={imageWidth} height={imageHeight} />

              {lines.map((line, i) => (
                <Fragment key={i}>
                  {/* 每绘制一条新的Line，都会生成两个Line，一个用于擦除，一个用于绘制，目的是为了解决绘制多条线时候透明度重叠的问题 */}
                  {line.tool === ToolName.Brush ? (
                    <Line
                      points={line.points}
                      stroke={"white"}
                      strokeWidth={line.strokeWidth}
                      tension={0.5}
                      lineCap="round"
                      lineJoin="round"
                      globalCompositeOperation={"destination-out"}
                    />
                  ) : null}
                  <Line
                    points={line.points}
                    stroke={
                      line.tool === ToolName.Eraser
                        ? "white"
                        : "rgb(104, 58, 205, .3)"
                    }
                    strokeWidth={line.strokeWidth}
                    tension={0.5}
                    lineCap="round"
                    lineJoin="round"
                    globalCompositeOperation={
                      line.tool === ToolName.Eraser
                        ? "destination-out"
                        : "source-over"
                    }
                  />
                </Fragment>
              ))}
              {/* 在画笔和橡皮擦工具下，鼠标移动时，会在鼠标位置生成一个白色圆圈，用于指示画笔和橡皮擦的绘制位置 */}
              {currTool?.name &&
              (currTool?.name === ToolName.Brush ||
                currTool?.name === ToolName.Eraser) ? (
                <Circle
                  x={circlePos.x}
                  y={circlePos.y}
                  radius={strokeWidth / 2}
                  stroke="rgba(255, 255, 255, 0.5)"
                  strokeWidth={3}
                  fill="transparent"
                />
              ) : null}
            </Layer>
          </Stage>
        </div>
      </Spin>
      <BottomTools
        originStageRef={originStageRef}
        originImageWidth={originImageWidth}
        originImageHeight={originImageHeight}
        originImgSrc={storyboardShotDetailImg}
        onRepaintSuccess={onRepaintSuccess}
        storyboardId={storyboardId}
        lines={lines}
      />
    </div>
  ); // 删除多余的括号
};

export default DrawPanel;
