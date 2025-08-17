import { createContext } from "react";

export interface IEditorApiContexts {
  onImageSizeChange: (newImageSize: string) => void;
}

export const EditorApiContexts = createContext<IEditorApiContexts>({} as IEditorApiContexts);
