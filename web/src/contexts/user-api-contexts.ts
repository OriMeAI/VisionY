import { createContext } from "react";

export interface IUserApiContexts {
  updateUserInfo: () => void;
}

export const UserApiContexts = createContext<IUserApiContexts>({} as IUserApiContexts);
