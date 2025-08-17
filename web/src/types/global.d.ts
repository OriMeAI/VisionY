// src/types/global.d.ts
import { FC, DetailedHTMLProps, ImgHTMLAttributes } from 'react';

declare global {
  // 扩展 window 对象
  interface Window {
    SafeImage: FC<DetailedHTMLProps<ImgHTMLAttributes<HTMLImageElement>, HTMLImageElement>>;
  }

  // 扩展 JSX 内在元素
  namespace JSX {
    interface IntrinsicElements {
      SafeImage: DetailedHTMLProps<ImgHTMLAttributes<HTMLImageElement>, HTMLImageElement>;
    }
  }
}