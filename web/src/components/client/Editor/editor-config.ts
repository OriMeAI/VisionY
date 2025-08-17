import brushIcon from "./../../../../assets/images/icons/brush.svg";
import brushActiveIcon from "./../../../../assets/images/icons/brush_active.svg";
import brushHoverIcon from "./../../../../assets/images/icons/brush_hover.svg";
import enlargeIcon from "./../../../../assets/images/icons/enlarge.svg";
import enlargeActiveIcon from "./../../../../assets/images/icons/enlarge_active.svg";
import enlargeHoverIcon from "./../../../../assets/images/icons/enlarge_hover.svg";
import eraserIcon from "./../../../../assets/images/icons/eraser.svg";
import eraserActiveIcon from "./../../../../assets/images/icons/eraser_active.svg";
import eraserHoverIcon from "./../../../../assets/images/icons/eraser_hover.svg";
import gripperIcon from "./../../../../assets/images/icons/gripper.svg";
import gripperActiveIcon from "./../../../../assets/images/icons/gripper_active.svg";
import gripperHoverIcon from "./../../../../assets/images/icons/gripper_hover.svg";
import lessenIcon from "./../../../../assets/images/icons/lessen.svg";
import lessenActiveIcon from "./../../../../assets/images/icons/lessen_active.svg";
import lessenHoverIcon from "./../../../../assets/images/icons/lessen_hover.svg";
import pointerIcon from "./../../../../assets/images/icons/pointer.svg";
import pointerActiveIcon from "./../../../../assets/images/icons/pointer_active.svg";
import pointerHoverIcon from "./../../../../assets/images/icons/pointer_hover.svg";

import { EditorToolItem } from "./../../../libs/interfaces";
import { ToolName } from "./../../../libs/enums";

// 默认画笔尺寸
export const DEFAULT_BRUSH_SIZE = 50;
// 默认橡皮擦尺寸
export const DEFAULT_ERASER_SIZE = 50;
// 默认图片尺寸
export const DEFAULT_IMAGE_SIZE = "100%";
// 默认工具栏选中项
export const DEFAULT_TOOL_ACTIVE_ID = 1;
// 默认图片初始缩放比例
export const DEFAULT_IMAGE_INIT_SCALE = 1;
// 默认图片X轴坐标, Y轴坐标
export const DEFAULT_IMAGE_POS_X = 50;
export const DEFAULT_IMAGE_POS_Y = 60;


// 工具栏
export const TOOL_LIST: EditorToolItem[] = [
  // {
  //   id: 1,
  //   icon: pointerIcon,
  //   hoverIcon: pointerHoverIcon,
  //   activeIcon: pointerActiveIcon,
  //   tip: i18n.t("pointer_tool"),
  //   name: ToolName.Pointer,
  // },
  {
    id: 1,
    icon: gripperIcon,
    hoverIcon: gripperHoverIcon,
    activeIcon: gripperActiveIcon,
    tip: "grippe",
    name: ToolName.Gripper,
  },
  {
    id: 2,
    icon: brushIcon,
    hoverIcon: brushHoverIcon,
    activeIcon: brushActiveIcon,
    tip: "brush",
    name: ToolName.Brush,
  },
  {
    id: 3,
    icon: eraserIcon,
    hoverIcon: eraserHoverIcon,
    activeIcon: eraserActiveIcon,
    tip: "eraser",
    name: ToolName.Eraser,
  },
  {
    id: 4,
    icon: enlargeIcon,
    hoverIcon: enlargeHoverIcon,
    activeIcon: enlargeActiveIcon,
    tip: "enlarge",
    name: ToolName.Enlarge,
  },
  {
    id: 5,
    icon: lessenIcon,
    hoverIcon: lessenHoverIcon,
    activeIcon: lessenActiveIcon,
    tip: "lessen",
    name: ToolName.Lessen,
  },
];

// 画笔尺寸范围
export const MIN_BRUSH_SIZE = 1;
export const MAX_BRUSH_SIZE = 200;

// 橡皮擦尺寸范围
export const MIN_ERASER_SIZE = 1;
export const MAX_ERASER_SIZE = 200;