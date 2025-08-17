import { createContext } from "react";
import { UserInfoType } from "../libs/interfaces";

export interface IUserContexts {
  userInfo: UserInfoType;
  setUserInfo: (userInfo: UserInfoType | undefined) => void;
  isAuthenticated: boolean;
  setIsAuthenticated: (isAuthenticated: boolean) => void;
  isShowLoginModal: boolean;
  setIsShowLoginModal: React.Dispatch<React.SetStateAction<boolean>>;
  isShowLoginModelLoading: boolean;
  setIsShowLoginModelLoading: React.Dispatch<React.SetStateAction<boolean>>;
}

export const UserContexts = createContext<IUserContexts>({} as IUserContexts);
