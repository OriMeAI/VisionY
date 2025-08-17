import { createContext } from "react";

export interface IModalContexts {
  isShowCreditsModal: boolean;
  setIsShowCreditsModal: React.Dispatch<React.SetStateAction<boolean>>;
  isShowCreditsLoading: boolean;
  setIsShowCreditsLoading: React.Dispatch<React.SetStateAction<boolean>>;

  isShowMembershipModal: boolean;
  setIsShowMembershipModal: React.Dispatch<React.SetStateAction<boolean>>;
  isShowMembershipLoading: boolean;
  setIsShowMembershipLoading: React.Dispatch<React.SetStateAction<boolean>>;
}

export const ModalContexts = createContext<IModalContexts>(
  {} as IModalContexts
);
