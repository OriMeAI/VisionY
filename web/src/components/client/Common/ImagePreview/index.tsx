/**
 * Dashboard详情页Layout组件
 */

import downloadIcon from "./../../../../../assets/images/pages/roleView/role_download_icon.svg";
import resetIcon from "./../../../../../assets/images/pages/roleView/reset_icon.svg";
import rotateLeftIcon from "./../../../../../assets/images/pages/roleView/rotate_left_icon.svg";
import rotateRightIcon from "./../../../../../assets/images/pages/roleView/rotate_right_icon.svg";
import zoomInIcon from "./../../../../../assets/images/pages/roleView/zoom_in_icon.svg";
import zoomOutIcon from "./../../../../../assets/images/pages/roleView/zoom_out_icon.svg";
import { Button, Image, Space } from "antd";
import React, { useEffect, useState } from "react";
import IconOnlyBtn from "../../Common/IconOnlyBtn";
import style from "./style.module.css";
import { LeftOutlined, RightOutlined } from "@ant-design/icons";

interface IProps {
  imageList: Array<{ id?: string; src?: string; alt?: string }>;
  current: number;
  // setCurrent: React.Dispatch<React.SetStateAction<number>>;
  previewImageVisible: boolean;
  setPreviewImageVisible: React.Dispatch<React.SetStateAction<boolean>>;
}
interface TransformType {
  x: number;
  y: number;
  rotate: number;
  scale: number;
  flipX: boolean;
  flipY: boolean;
}
interface ImgInfo {
  url: string;
  alt: string;
  width: string | number;
  height: string | number;
}

const ImagePreview: React.FC<IProps> = ({
  imageList,
  current,
  previewImageVisible,
  setPreviewImageVisible,
}: IProps) => {
  const [images, setImages] = useState<
    { id?: string; src?: string; alt?: string }[]
  >([]);

  useEffect(() => {
    setImages(imageList);
  }, [imageList]);

  const onDownload = () => {
    const url = images[current]?.src;
    if (!url) return;
    let imageUrl = url;
    if (imageUrl.indexOf("?") > -1) {
      imageUrl = imageUrl.slice(0, imageUrl.indexOf("?"));
    }
    const suffix = imageUrl.slice(imageUrl.lastIndexOf("."));
    const filename = Date.now() + suffix;

    fetch(url)
      .then((response) => response.blob())
      .then((blob) => {
        const blobUrl = URL.createObjectURL(new Blob([blob]));
        const link = document.createElement("a");
        link.href = blobUrl;
        link.download = filename;
        document.body.appendChild(link);
        link.click();
        URL.revokeObjectURL(blobUrl);
        link.remove();
      });
  };

  return (
    <Image.PreviewGroup
      preview={{
        visible: previewImageVisible,
        current: current,
        countRender: () => null, // 返回 null 来隐藏计数器
        onVisibleChange: (value) => {
          setPreviewImageVisible(value);
        },
        // onChange: (index) => {
        //   setCurrent(index);
        // },
        // imageRender: (
        //   originalNode: React.ReactElement,
        //   info: { transform: TransformType; image: ImgInfo }
        // ) => {
        //   return (
        //     <>
        //       <Button
        //         disabled={current === 0}
        //         className={
        //           current === 0 ? style.leftBtnDisabled : style.leftBtn
        //         }
        //         onClick={() => {
        //           if (current === 0) return;
        //           setCurrent(current - 1);
        //         }}
        //       >
        //         <LeftOutlined />
        //       </Button>
        //       {originalNode}
        //       <Button
        //         disabled={current === images.length - 1}
        //         className={
        //           current === images.length - 1
        //             ? style.rightBtnDisabled
        //             : style.rightBtn
        //         }
        //         onClick={() => {
        //           if (current === images.length - 1) return;
        //           setCurrent(current + 1);
        //         }}
        //       >
        //         <RightOutlined />
        //       </Button>
        //     </>
        //   );
        // },
        toolbarRender: (
          _,
          {
            transform: { scale },
            actions: {
              onRotateLeft,
              onRotateRight,
              onZoomOut,
              onZoomIn,
              onReset,
            },
          }
        ) => (
          <Space size={12} className={style.toolbarWrapper}>
            <IconOnlyBtn
              width={24}
              height={24}
              icon={downloadIcon}
              handleClick={onDownload}
            />
            <IconOnlyBtn
              width={24}
              height={24}
              icon={rotateLeftIcon}
              handleClick={onRotateLeft}
            />
            <IconOnlyBtn
              width={24}
              height={24}
              icon={rotateRightIcon}
              handleClick={onRotateRight}
            />
            <IconOnlyBtn
              disabled={scale === 1}
              width={24}
              height={24}
              icon={zoomOutIcon}
              handleClick={onZoomOut}
            />
            <IconOnlyBtn
              disabled={scale === 50}
              width={24}
              height={24}
              icon={zoomInIcon}
              handleClick={onZoomIn}
            />
            <IconOnlyBtn
              width={24}
              height={24}
              icon={resetIcon}
              handleClick={onReset}
            />
          </Space>
        ),
      }}
    >
      {previewImageVisible ? (
        <>
          {Array.isArray(images) && images.length > 0
            ? images.map((item, index) => (
                <Image
                  key={`image_preview_${item.id}_${index}`}
                  draggable="false"
                  alt={item.alt}
                  src={item.src}
                  width={0}
                  height={0}
                  style={{
                    objectFit: "contain",
                    display: previewImageVisible ? "block" : "none",
                    position: "absolute",
                    opacity: 0,
                    pointerEvents: "none",
                  }}
                />
              ))
            : null}
        </>
      ) : null}
    </Image.PreviewGroup>
  );
};

export default ImagePreview;
