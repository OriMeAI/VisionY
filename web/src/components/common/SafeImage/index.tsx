// src/components/SafeImage.tsx
import React from 'react';

const SafeImage: React.FC<
  React.DetailedHTMLProps<React.ImgHTMLAttributes<HTMLImageElement>, HTMLImageElement>
> = ({ src, alt, ...props }) => {
  if (!src) return null;
  // 使用 React.createElement 避免 <img> 被 Babel override
  return React.createElement('img', { src, alt, ...props });
};

export default SafeImage;