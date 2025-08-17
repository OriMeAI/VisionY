import { createContext } from "react";
import { RepaintStatus } from "../libs/enums";

export interface IEditorContexts {
  toolActiveId: number;
  setToolActiveId: React.Dispatch<React.SetStateAction<number>>;
  brushSize: number;
  setBrushSize: React.Dispatch<React.SetStateAction<number>>;
  eraserSize: number;
  setEraserSize: React.Dispatch<React.SetStateAction<number>>;
  imageSize: string;
  setImageSize: React.Dispatch<React.SetStateAction<string>>;
  initImageSize: number;
  setInitImageSize: React.Dispatch<React.SetStateAction<number>>;
  repaintStatus: RepaintStatus;
  setRepaintStatus: React.Dispatch<React.SetStateAction<RepaintStatus>>;
  canvasLoading: boolean;
  setCanvasLoading: React.Dispatch<React.SetStateAction<boolean>>;
  isRepaintModalOpen: boolean;
  setIsRepaintModalOpen: React.Dispatch<React.SetStateAction<boolean>>;
}

export const EditorContexts = createContext<IEditorContexts>(
  {} as IEditorContexts
);
