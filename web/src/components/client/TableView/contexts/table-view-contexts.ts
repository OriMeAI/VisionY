import { createContext } from "react";

export interface ITableViewContexts {
  setIsTourOpen: React.Dispatch<React.SetStateAction<boolean>>;
  tourRef1: React.MutableRefObject<null>;
  tourRef2: React.MutableRefObject<null>;
  tourRef3: React.MutableRefObject<null>;
  tableLoading: boolean;
  setTableLoading: React.Dispatch<React.SetStateAction<boolean>>;
  isRepaintModalOpen: boolean;
  setIsRepaintModalOpen: React.Dispatch<React.SetStateAction<boolean>>;
}

export const TableViewContexts = createContext<ITableViewContexts>(
  {} as ITableViewContexts
);
