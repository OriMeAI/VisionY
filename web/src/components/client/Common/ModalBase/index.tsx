import { Modal } from "antd";
import React, { ReactNode } from "react";
import style from "./style.module.css";
import { useTranslation } from "react-i18next";

interface IProps {
  children: React.ReactNode;
  title?: string;
  open?: boolean;
  onOk?: () => void;
  onCancel?: () => void;
  okText?: ReactNode;
  cancelText?: ReactNode;
  showFooter?: boolean;
  footer?: ReactNode;
  width: number;
  height: number | string;  // 修改为可选参数
  wrapperClassName?: string;
  okButtonDisabled?: boolean;
  closable?: boolean;
  destroyOnClose?: boolean;
  afterOpenChange?: (open: boolean) => void;
}

/** 弹窗容器 */
const ModalBase: React.FC<IProps> = (props: IProps) => {
  const { t } = useTranslation();
  const {
    children,
    title,
    open,
    onCancel,
    onOk,
    okText,
    cancelText,
    showFooter,
    footer,
    width,
    height,
    okButtonDisabled,
    closable = true,
    destroyOnClose = true,
    afterOpenChange
  } = props;

  const handleCancel = () => {
    onCancel && onCancel();
  };

  const handleConfirm = () => {
    onOk && onOk();
  };

  // 创建一个新变量来存储处理后的高度值
  const modalHeight = height || "auto";
  // 设置最大高度，当height为undefined时使用768px
  const maxModalHeight = height ? (typeof height === 'number' ? `${height}px` : height) : "auto";

  return (
    <Modal
    // getContainer={() => document.body} // 确保挂载到 body
    // getContainer={false}
    // style={{ minWidth: width ? `${width}px` : '700px' }}
    // wrapClassName={wrapperClassName || style.modalWrapper}
    wrapClassName={style.modalWrapper}
    title={title}
    open={open}
    footer={
      footer ? footer : (params) => { return showFooter !== false ? params : null;}
    }
    width={width}
    height={modalHeight}
    onOk={handleConfirm}
    okText={okText || t("confirm")}
    onCancel={handleCancel}
    cancelText={cancelText || t("confirm")}
    closable={closable}
    maskClosable={false}
    centered
    // loading
    cancelButtonProps={{
      size: "large",
    }}
    okButtonProps={{
      size: "large",
      disabled: okButtonDisabled ? true : false,
    }}
    destroyOnClose={destroyOnClose}
    afterOpenChange={afterOpenChange}
    style={{ 
      width,
      height: modalHeight,
      '--modal-width': `${width}px`,
      '--modal-height': typeof modalHeight === 'number' ? `${modalHeight}px` : modalHeight,
      maxWidth: '100vw',
      maxHeight: maxModalHeight
   } as React.CSSProperties}
  >
    {children}
  </Modal>
  );
};

export default ModalBase;
