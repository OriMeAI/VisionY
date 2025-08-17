import { createContext } from "react";

export interface IDashboardContexts {
  isShowUpgradeModal: boolean;
  setIsShowUpgradeModal: React.Dispatch<React.SetStateAction<boolean>>;
}

export const DashboardContexts = createContext<IDashboardContexts>(
  {} as IDashboardContexts
);
