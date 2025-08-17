import React, { useEffect, useRef, useState } from "react";
import banner1Img from "./../../../../assets/images/pages/home/banner1-B1BE1Tb_.jpg";
import banner2Img from "./../../../../assets/images/pages/home/banner2-DY_ZTFPn.jpg";
import banner3Img from "./../../../../assets/images/pages/home/banner3-D6LvcrZc.jpg";

const images = [banner1Img, banner2Img, banner3Img];

const BannerCarousel: React.FC = () => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const bannerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          const interval = setInterval(() => {
            setCurrentIndex((prevIndex) => (prevIndex + 1) % images.length);
          }, 3000); // 每3秒切换一次图片

          return () => clearInterval(interval);
        }
      },
      { threshold: 0.5 }
    );

    if (bannerRef.current) {
      observer.observe(bannerRef.current);
    }

    return () => {
      if (bannerRef.current) {
        observer.unobserve(bannerRef.current);
      }
    };
  }, []);

  return (
    <div ref={bannerRef} className="hidden md:block h-[520px] mt-[90px] relative">
      <div className="w-[calc(100%-2rem)] min-w-[calc(100%-2rem)] h-px bg-gray-200 mx-auto" />
      {images.map((image, index) => (
        <img
          key={index}
          src={image}
          alt=""
          className={`w-full h-full absolute top-0 left-0 transition-opacity duration-500 ${
            index === currentIndex ? 'opacity-100' : 'opacity-0'
          }`}
          loading="eager"
          decoding="async"
        />
      ))}
    </div>
  );
};

export default BannerCarousel;
