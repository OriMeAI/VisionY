/**
 * 创建新作品按钮
 */

import { Button } from "antd";
import plusIcon from "./../../../../../assets/images/icons/plus.svg";
import plusHoverIcon from "./../../../../../assets/images/icons/plus_hover.svg";

import React from "react";
import {
  IUserContexts,
  UserContexts,
} from "./../../../../contexts/user-contexts";

interface IProps {
  onBtnClick?: () => void;
  buttonText?: React.ReactNode;
}

const CreateNewBtn: React.FC<IProps> = ({ onBtnClick, buttonText }: IProps) => {
  const userContexts: IUserContexts =
    React.useContext<IUserContexts>(UserContexts);

  return (
    <div>
      {userContexts.isAuthenticated ? (
        <Button
          type="dashed"
          className="h-[328px] w-full bg-background flex flex-col text-gray-500 border-2 hover:text-primary group"
          onClick={() => {
            onBtnClick && onBtnClick();
          }}
        >
          <div className="w-9 h-9 relative">
            <img
              src={plusIcon}
              alt="Create New Story Icon"
              className="w-9 h-9 absolute inset-0 transition-opacity duration-200 group-hover:opacity-0"
            />
            <img
              src={plusHoverIcon}
              alt="Create New Story Icon Hover"
              className="w-9 h-9 absolute inset-0 opacity-0 transition-opacity duration-200 group-hover:opacity-100"
            />
          </div>
          {buttonText}
        </Button>
      ) : (
        <Button
          type="dashed"
          className="h-[328px] w-full bg-background flex flex-col text-gray-500 border-2 hover:text-primary group"
          onClick={() => {
            userContexts.setIsShowLoginModal(true);
          }}
        >
          <div className="w-9 h-9 relative">
            <img
              src={plusIcon}
              alt="Create New Story Icon"
              className="w-9 h-9 absolute inset-0 transition-opacity duration-200 group-hover:opacity-0"
            />
            <img
              src={plusHoverIcon}
              alt="Create New Story Icon Hover"
              className="w-9 h-9 absolute inset-0 opacity-0 transition-opacity duration-200 group-hover:opacity-100"
            />
          </div>
          {buttonText}
        </Button>
      )}
    </div>
  );
};

export default CreateNewBtn;
