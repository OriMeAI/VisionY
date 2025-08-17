/**
 * 局部重绘页头部工具栏
 */

import React, { useContext, useState, useEffect } from "react";
import SizeSelect from "../../SizeSelect";
import Toolbar from "../../Toolbar";
import ToolDrop from "../../ToolDrop";
import { RepaintStatus, ToolName } from "../../../../../libs/enums";
import { EditorContexts, IEditorContexts } from "../../../../../contexts/editor-contexts";
import { TOOL_LIST } from "../../editor-config";
import arrayUtils from "../../../../../libs/array-utils";

interface IProps {
  repaintStatus: RepaintStatus;
}

const EditorTopMenu: React.FC<IProps> = ({ repaintStatus }: IProps) => {
  const editorContexts = useContext<IEditorContexts>(EditorContexts);
  
  // 获取当前工具
  const currentTool = arrayUtils.getRecordById(TOOL_LIST, "id", editorContexts.toolActiveId);
  
  // 判断是否应该显示 ToolDrop
  const shouldShowToolDrop = currentTool?.name === ToolName.Brush || currentTool?.name === ToolName.Eraser;
  
  // 跟踪当前工具类型，用于动画
  const [toolType, setToolType] = useState<ToolName | null>(currentTool?.name as ToolName);
  // 跟踪工具是否正在变化
  const [isToolChanging, setIsToolChanging] = useState(false);
  
  // 监听工具变化
  useEffect(() => {
    if (currentTool?.name !== toolType && shouldShowToolDrop) {
      // 工具发生变化，触发过渡动画
      setIsToolChanging(true);
      
      // 设置短暂延迟后更新工具类型，让动画有时间执行
      const timer = setTimeout(() => {
        setToolType(currentTool?.name as ToolName);
        setIsToolChanging(false);
      }, 150); // 动画持续时间的一半
      
      return () => clearTimeout(timer);
    } else if (shouldShowToolDrop) {
      // 初始化工具类型
      setToolType(currentTool?.name as ToolName);
    }
  }, [currentTool?.name, shouldShowToolDrop]);
  
  // 根据工具类型和变化状态确定CSS类
  const getToolDropClasses = () => {
    let baseClasses = "absolute left-0 transition-all duration-300 ease-in-out";
    
    if (!shouldShowToolDrop) {
      return `${baseClasses} opacity-0 -translate-x-4 pointer-events-none`;
    }
    
    if (isToolChanging) {
      return `${baseClasses} opacity-50 scale-95`;
    }
    
    return `${baseClasses} opacity-100 translate-x-0 scale-100`;
  };

  return (
    <div className="relative flex items-center justify-center px-4 py-2 bg-white border-b border-gray-200">
      <div className={getToolDropClasses()}>
        <ToolDrop />
      </div>
      <div className="mr-2 mt-[2px]">
        <Toolbar />
      </div>
      <div className="absolute right-0">
        <SizeSelect />
      </div>
    </div>
  );
};

export default EditorTopMenu;
