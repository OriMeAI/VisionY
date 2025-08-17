/**
 * 通用头部组件
 */

import { Button, Carousel } from "antd";
import React, { Suspense, useEffect } from "react";
import { useTranslation } from "react-i18next";
import { LazyLoadImage } from "react-lazy-load-image-component";
import "react-lazy-load-image-component/src/effects/blur.css";
import homeApi from "../../../api/homeApi";
import BannerCarousel from "../BannerCarousel";
import IncrementingNumber from "../IncrementingNumber";
import avatar1Img from "./../../../../assets/images/pages/home/avatar1-BMpzPZLz.png";
import avatar2Img from "./../../../../assets/images/pages/home/avatar2-bo87VwB3.png";
import avatar3Img from "./../../../../assets/images/pages/home/avatar3-X-vM_Kde.png";
import avatar4Img from "./../../../../assets/images/pages/home/avatar4-B9NcKTuQ.png";
import cameraMinImg from "./../../../../assets/images/pages/home/Camera.min-Bs13TxHW.png";
import cardInfo1Img from "./../../../../assets/images/pages/home/CardInfo-1-D28OBWXR.png";
import cardInfo2Img from "./../../../../assets/images/pages/home/CardInfo-2-Dfe-Hfm5.png";
import cardInfo3Img from "./../../../../assets/images/pages/home/CardInfo-3-BIWs_31v.png";
import cardInfo4Img from "./../../../../assets/images/pages/home/CardInfo-4-BzSklUCN.png";
import case1Img from "./../../../../assets/images/pages/home/case1-CmU6hAeI.png";
import case2Img from "./../../../../assets/images/pages/home/case2-B6iMtAJ9.png";
import case3Img from "./../../../../assets/images/pages/home/case3-tFxgFiee.png";
import feature1Img from "./../../../../assets/images/pages/home/feature1-BM47CrJW.png";
import feature2Img from "./../../../../assets/images/pages/home/feature2-GOTUkU-L.png";
import feature3Img from "./../../../../assets/images/pages/home/feature3-CG-Z1I8e.png";
import feature4Img from "./../../../../assets/images/pages/home/feature4-C6CzdxDo.png";
import lampMinImg from "./../../../../assets/images/pages/home/Lamp.min-vHwIqAfr.png";
import priceBg from "./../../../../assets/images/pages/home/price-bg-BavbOUcV.png";
import style from "./style.module.css";

const Content: React.FC = () => {
  const { t } = useTranslation();
  const [imgCount, setImgCount] = React.useState<number>(0);
  const [projectCount, setProjectCount] = React.useState<number>(0);
  // 获取生图数量和作品数量
  useEffect(() => {
    (async () => {
      const data = await homeApi.getStatistics();
      setImgCount(data.result?.data?.imgCount);
      setProjectCount(data.result?.data?.projectCount);
    })();
  }, []);
  return (
    <div className="flex-grow flex-1">
      <section className="relative min-h-screen flex items-center">
        <div className="w-full h-full absolute top-0 -z-[1] flex items-center opacity-75">
          <Suspense fallback={<p>Loading video...</p>}>
            <video
              autoPlay
              loop
              // 加上muted属性，否则无法自动播放
              muted
              playsInline
              className={`w-full h-full absolute top-0 bottom-0 right-0 left-0 -z-[100] m-auto object-cover ${style.videoBg}`}
            >
              <source
                src={
                  // videoBgSrc
                  "https://static.chuangyi-keji.com/home/AIGCSH0010aev06.mp4"
                }
                type="video/mp4"
              />
              Your browser does not support the video tag.
            </video>
          </Suspense>
        </div>
        <div
          className={`${style.container} mx-auto flex flex-col custom:flex-row custom:justify-between custom:items-center mt-[86px] custom:mt-0 space-y-8`}
        >
          <div className="flex flex-col">
            <div>
              <div className="px-[18px] custom:px-0 relative text-[70px] leading-[85px] custom:text-[125px] custom:leading-[150px] font-bold text-[#F0F1D8] text-left">
                ONE STORY
              </div>
              <div className="px-[18px] custom:px-0 text-[50px] leading-[64px] custom:text-[70px] custom:leading-[84px] text-[#F0F1D8] font-bold relative text-left">
                {t("ai_story_generator")}
              </div>
              <div className="flex text-white mt-10 space-x-10">
                <div className="min-w-[160px]">
                  <h2 className="text-base relative text-center">
                    {t("image_count")}
                    <span className="absolute -bottom-1 right-0 left-0 w-1/5 h-[2px] mx-auto bg-white"></span>
                  </h2>
                  <p className="text-[40px] leading-[75px] font-semibold text-center">
                    <span className="inline-block tabular-nums tracking-wider">
                      {imgCount ? (
                        <IncrementingNumber
                          start={0}
                          end={imgCount}
                          duration={3000}
                        />
                      ) : null}
                    </span>
                  </p>
                </div>
                <div className="min-w-[160px]">
                  <h2 className="text-base relative text-center">
                    {t("project_count")}
                    <span className="absolute -bottom-1 right-0 left-0 w-1/5 h-[2px] mx-auto bg-white"></span>
                  </h2>
                  <p className="text-[40px] leading-[75px] font-semibold text-center">
                    <span className="inline-block tabular-nums tracking-wider">
                      {projectCount ? (
                        <IncrementingNumber
                          start={0}
                          end={projectCount}
                          duration={3000}
                        />
                      ) : null}
                    </span>
                  </p>
                </div>
              </div>
            </div>
            <div className="w-[85vw] custom:w-[56vw] 2xl:w-[43vw] custom:mt-24">
              <div className="relative flex w-full flex-col items-center justify-center overflow-hidden rounded-lg">
                <div className="group flex overflow-hidden p-4 [--gap:1rem] [gap:var(--gap)] flex-row [--duration:40s]">
                  <div className="flex shrink-0 justify-around [gap:var(--gap)] animate-marquee flex-row group-hover:[animation-play-state:paused]">
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/17b4ea2be9684eb186e67252352f71a0.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_1")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/236e5256319a4e3e852f88af028788d3.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_2")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/21fe2ad0106a46e7930cb2c4719bab56.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_3")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/0f8e3aed1457438280e3236ab5d4a493.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_4")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/f9c5bb94968b4ca9aa074d9f9e54743f.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_5")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/307597e173034511bf6ffee1da5070c0.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_6")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/b056dc61a855424788ba19c1df673f6c.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_7")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/ca03d0ed8a2346f9ba6b578a639284c2.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_8")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/37ee1173089c4b7fa40c46b7f87efa62.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_9")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/410b347a67044bb4a3a0ae1e6b2c6372.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_10")}
                        </blockquote>
                      </div>
                    </figure>
                  </div>
                  <div className="flex shrink-0 justify-around [gap:var(--gap)] animate-marquee flex-row group-hover:[animation-play-state:paused]">
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/17b4ea2be9684eb186e67252352f71a0.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_1")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/236e5256319a4e3e852f88af028788d3.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_2")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/21fe2ad0106a46e7930cb2c4719bab56.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_3")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/0f8e3aed1457438280e3236ab5d4a493.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_4")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/f9c5bb94968b4ca9aa074d9f9e54743f.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_5")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/307597e173034511bf6ffee1da5070c0.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_6")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/b056dc61a855424788ba19c1df673f6c.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_7")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/ca03d0ed8a2346f9ba6b578a639284c2.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_8")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/37ee1173089c4b7fa40c46b7f87efa62.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_9")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/410b347a67044bb4a3a0ae1e6b2c6372.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_10")}
                        </blockquote>
                      </div>
                    </figure>
                  </div>
                  <div className="flex shrink-0 justify-around [gap:var(--gap)] animate-marquee flex-row group-hover:[animation-play-state:paused]">
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/17b4ea2be9684eb186e67252352f71a0.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_1")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/236e5256319a4e3e852f88af028788d3.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_2")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/21fe2ad0106a46e7930cb2c4719bab56.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_3")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/0f8e3aed1457438280e3236ab5d4a493.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_4")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/f9c5bb94968b4ca9aa074d9f9e54743f.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_5")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/307597e173034511bf6ffee1da5070c0.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_6")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/b056dc61a855424788ba19c1df673f6c.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_7")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/ca03d0ed8a2346f9ba6b578a639284c2.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_8")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/37ee1173089c4b7fa40c46b7f87efa62.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_9")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/410b347a67044bb4a3a0ae1e6b2c6372.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_10")}
                        </blockquote>
                      </div>
                    </figure>
                  </div>
                  <div className="flex shrink-0 justify-around [gap:var(--gap)] animate-marquee flex-row group-hover:[animation-play-state:paused]">
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/17b4ea2be9684eb186e67252352f71a0.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_1")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/236e5256319a4e3e852f88af028788d3.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_2")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/21fe2ad0106a46e7930cb2c4719bab56.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_3")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/0f8e3aed1457438280e3236ab5d4a493.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_4")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/f9c5bb94968b4ca9aa074d9f9e54743f.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_5")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/307597e173034511bf6ffee1da5070c0.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_6")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/b056dc61a855424788ba19c1df673f6c.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_7")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/ca03d0ed8a2346f9ba6b578a639284c2.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_8")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/37ee1173089c4b7fa40c46b7f87efa62.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_9")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/410b347a67044bb4a3a0ae1e6b2c6372.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_10")}
                        </blockquote>
                      </div>
                    </figure>
                  </div>
                </div>
                <div className="group flex overflow-hidden p-4 [--gap:1rem] [gap:var(--gap)] flex-row [--duration:40s]">
                  <div className="flex shrink-0 justify-around [gap:var(--gap)] animate-marquee flex-row group-hover:[animation-play-state:paused] [animation-direction:reverse]">
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/48beba4cc56344c4a7e6efaeb0629108.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_11")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/63078b0a097e4aa1abffa11fc28286c9.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_12")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/3d9f6bca4eed4e47a4238b3d1a59ef8f.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_13")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/53ea2c68bf8243d385352e1e356d737e.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_14")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/754f436e39c54572a1b803834a7e1465.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_15")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/1261595db4e046be989c777c827f888c.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_16")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/b4ba930f7f204888a20b49350ddddc1d.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_17")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/878916f08b23456a85df0eb29fc1e1b2.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_18")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/4b48c41efd9d4838aaa86a3a7b431762.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_19")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/f92ce29816d34c94bbaae66f57459786.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_20")}
                        </blockquote>
                      </div>
                    </figure>
                  </div>
                  <div className="flex shrink-0 justify-around [gap:var(--gap)] animate-marquee flex-row group-hover:[animation-play-state:paused] [animation-direction:reverse]">
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/48beba4cc56344c4a7e6efaeb0629108.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_11")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/63078b0a097e4aa1abffa11fc28286c9.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_12")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/3d9f6bca4eed4e47a4238b3d1a59ef8f.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_13")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/53ea2c68bf8243d385352e1e356d737e.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_14")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/754f436e39c54572a1b803834a7e1465.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_15")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/1261595db4e046be989c777c827f888c.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_16")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/b4ba930f7f204888a20b49350ddddc1d.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_17")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/878916f08b23456a85df0eb29fc1e1b2.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_18")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/4b48c41efd9d4838aaa86a3a7b431762.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_19")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/f92ce29816d34c94bbaae66f57459786.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_20")}
                        </blockquote>
                      </div>
                    </figure>
                  </div>
                  <div className="flex shrink-0 justify-around [gap:var(--gap)] animate-marquee flex-row group-hover:[animation-play-state:paused] [animation-direction:reverse]">
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/48beba4cc56344c4a7e6efaeb0629108.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_11")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/63078b0a097e4aa1abffa11fc28286c9.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_12")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/3d9f6bca4eed4e47a4238b3d1a59ef8f.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_13")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/53ea2c68bf8243d385352e1e356d737e.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_14")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/754f436e39c54572a1b803834a7e1465.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_15")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/1261595db4e046be989c777c827f888c.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_16")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/b4ba930f7f204888a20b49350ddddc1d.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_17")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/878916f08b23456a85df0eb29fc1e1b2.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_18")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/4b48c41efd9d4838aaa86a3a7b431762.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_19")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/f92ce29816d34c94bbaae66f57459786.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_20")}
                        </blockquote>
                      </div>
                    </figure>
                  </div>
                  <div className="flex shrink-0 justify-around [gap:var(--gap)] animate-marquee flex-row group-hover:[animation-play-state:paused] [animation-direction:reverse]">
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/48beba4cc56344c4a7e6efaeb0629108.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_11")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/63078b0a097e4aa1abffa11fc28286c9.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_12")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/3d9f6bca4eed4e47a4238b3d1a59ef8f.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_13")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/53ea2c68bf8243d385352e1e356d737e.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_14")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/754f436e39c54572a1b803834a7e1465.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_15")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/1261595db4e046be989c777c827f888c.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_16")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/b4ba930f7f204888a20b49350ddddc1d.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_17")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/878916f08b23456a85df0eb29fc1e1b2.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_18")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/4b48c41efd9d4838aaa86a3a7b431762.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_19")}
                        </blockquote>
                      </div>
                    </figure>
                    <figure className="relative w-64 h-14 cursor-pointer overflow-hidden py-2 pr-2 rounded-full flex items-center bg-gray-950/25 backdrop-blur">
                      <div className="flex flex-row items-center space-x-2">
                        <img
                          className="rounded-full"
                          width="56"
                          height="56"
                          alt=""
                          src="https://static.chuangyi-keji.com/2024/08/02/assets/file/f92ce29816d34c94bbaae66f57459786.png"
                        />
                        <blockquote className="text-sm text-white">
                          {t("user_comment_20")}
                        </blockquote>
                      </div>
                    </figure>
                  </div>
                </div>
              </div>
            </div>
          </div>
          {/* <div className="bg-white/60 backdrop-blur-sm rounded-lg p-4 custom:px-14 custom:py-10">
            <LoginForm
              onLoginSuccess={() => {
                location.reload();
              }}
            />
          </div> */}
        </div>
      </section>
      <section className="hidden custom:block pt-16">
        <div className={`${style.container} mx-auto`}>
          <div className="rounded-[10px] border-2 border-neutral-400 pt-[84px] pb-[100px]">
            <div className="px-[74px]">
              <div className="flex justify-between flex-wrap lg:flex-nowrap">
                <div className="w-[508px] text-[80px] text-[#F0F1D8] leading-[100px] font-semibold">
                  {t("use_ai_brush")}
                  <br />
                  {t("draw_your_story")}
                </div>
                <div className="w-[508px] text-xl text-white self-end p-5 mb-4 border-b-2 border-black border-t-2">
                  {t("convert_text_to_storyboard")}
                </div>
              </div>
              <div className="flex mt-11 text-white flex-wrap">
                <div className="h-[480px] px-[60px] border-t-2 border-b-2 border-black flex justify-center items-center w-full lg:w-1/2">
                  <div className="space-y-6">
                    <img
                      className="w-[140px] h-[140px]"
                      src={feature1Img}
                      alt=""
                    />
                    <div>
                      <h2 className="text-4xl mb-2">
                        {t("generate_professional_storyboard")}
                      </h2>
                      <p>{t("generate_professional_storyboard_desc")}</p>
                    </div>
                  </div>
                </div>
                <div className="h-[480px] mt-[50px] flex justify-center items-center w-full lg:w-1/2 lg:mt-0">
                  <img className="h-full" src={cardInfo1Img} alt="" />
                </div>
              </div>
              <div className="flex mt-[50px] text-white flex-wrap flex-col-reverse lg:flex-row">
                <div className="h-[480px] mt-[50px] border-r-0 border-black flex justify-center items-center w-full lg:w-1/2 lg:mt-0">
                  <img className="w-full h-full" src={cardInfo2Img} alt="" />
                </div>
                <div className="h-[480px] px-[60px] border-t-2 border-b-2 border-l-0 border-r-2 border-black flex justify-center items-center w-full lg:w-1/2 lg:border-r-0 lg:mt-0">
                  <div className="space-y-6">
                    <img
                      className="w-[140px] h-[140px]"
                      src={feature2Img}
                      alt=""
                    />
                    <div>
                      <h2 className="text-4xl mb-2">
                        {t("produce_film_level_images")}
                      </h2>
                      <p>{t("produce_film_level_images_desc")}</p>
                    </div>
                  </div>
                </div>
              </div>
              <div className="flex mt-11 text-white flex-wrap">
                <div className="h-[480px] px-[60px] border-t-2 border-b-2 border-black flex justify-center items-center w-full lg:w-1/2">
                  <div className="space-y-6">
                    <img
                      className="w-[140px] h-[140px]"
                      src={feature3Img}
                      alt=""
                    />
                    <div>
                      <h2 className="text-4xl mb-2">
                        {t("control_image_elements")}
                      </h2>
                      <p>{t("control_image_elements_desc")}</p>
                    </div>
                  </div>
                </div>
                <div className="h-[480px] mt-[50px] border-r-0 border-l-2 border-black flex justify-center items-center w-full lg:w-1/2 lg:border-l-0 lg:mt-0">
                  <img className="w-full h-full" src={cardInfo3Img} alt="" />
                </div>
              </div>
              <div className="flex mt-[50px] text-white flex-wrap flex-col-reverse lg:flex-row">
                <div className="h-[480px] mt-[50px] border-r-0 border-black flex justify-center items-center w-full lg:w-1/2 lg:mt-0">
                  <img className="w-full h-full" src={cardInfo4Img} alt="" />
                </div>
                <div className="h-[480px] px-[60px] border-t-2 border-b-2 border-l-0 border-r-2 border-black flex justify-center items-center w-full lg:w-1/2 lg:border-r-0 lg:mt-0">
                  <div className="space-y-6">
                    <img
                      className="w-[140px] h-[140px]"
                      src={feature4Img}
                      alt=""
                    />
                    <div>
                      <h2 className="text-4xl mb-2">
                        {t("build_character_assets")}
                      </h2>
                      <p>{t("build_character_assets_desc")}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <BannerCarousel />
      <section className="hidden custom:block py-20 relative">
        <div className="text-white absolute left-[60%] top-[100px] blur-[1000px] z-[1]">
          <div className="w-[280px] h-[280px] rounded-full bg-[#FDFF86]"></div>
        </div>
        <div className={`${style.container} mx-auto`}>
          <div className="relative z-10">
            <div className="text-center text-white relative">
              <img
                className="w-[240px] h-[240px] hidden absolute right-0 -top-16 lg:block"
                src={cameraMinImg}
                alt=""
              />
              <h2 className="text-[64px] font-semibold text-[#F0F1D8]">
                {t("rich_case_display")}
              </h2>
              <p className="text-[#F0F1D8]">
                {t("suitable_for_various_scenarios")}
              </p>
            </div>
            <div className="flex mt-11 flex-col items-center space-y-5 lg:space-x-5 lg:justify-center lg:flex-row lg:space-y-0">
              <div className="w-[330px] h-[573px] border border-neutral-600 rounded-lg overflow-hidden bg-neutral-900 bg-opacity-60">
                <div className="h-[426px] overflow-hidden">
                  <img
                    className="w-full h-full  transition-all hover:scale-105"
                    src={case1Img}
                    alt=""
                  />
                </div>
                <div className="h-[147px] flex flex-col items-center justify-center">
                  <h2 className="text-2xl font-medium mb-4 text-white">
                    {t("name_1")}
                  </h2>
                  <p className="text-stone-300">{t("series_qiliang")}</p>
                </div>
              </div>
              <div className="w-[330px] h-[573px] border border-neutral-600 rounded-lg overflow-hidden bg-neutral-900 bg-opacity-60">
                <div className="h-[426px] overflow-hidden">
                  <img
                    className="w-full h-full transition-all hover:scale-105"
                    src={case2Img}
                    alt=""
                  />
                </div>
                <div className="h-[147px] flex flex-col items-center justify-center">
                  <h2 className="text-2xl font-medium mb-4 text-white">
                    {t("name_2")}
                  </h2>
                  <p className="text-stone-300">{t("series_dizhi")}</p>
                </div>
              </div>
              <div className="w-[330px] h-[573px] border border-neutral-600 rounded-lg overflow-hidden bg-neutral-900 bg-opacity-60">
                <div className="h-[426px] overflow-hidden">
                  <img
                    className="w-full h-full transition-all hover:scale-105"
                    src={case3Img}
                    alt=""
                  />
                </div>
                <div className="h-[147px] flex flex-col items-center justify-center">
                  <h2 className="text-2xl font-medium mb-4 text-white">
                    {t("name_3")}
                  </h2>
                  <p className="text-stone-300">{t("series_suanming")}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section className="hidden custom:block pt-11 mb-8">
        <div className={`${style.container} mx-auto`}>
          <div>
            <div className="text-center mb-8 relative">
              <img
                className="w-[240px] h-[240px] hidden absolute left-0 -top-[50px] lg:block"
                src={lampMinImg}
                alt=""
              />
              <h2 className="text-[64px] font-semibold text-[#F0F1D8]">
                {t("user_experience")}
              </h2>
              <p className="text-[#F0F1D8]">{t("professional_feedback")}</p>
            </div>
            <div
              className="flex justify-center items-center flex-wrap lg:justify-between lg:flex-nowrap h-[340px] px-9 pb-24 relative"
              style={{
                backgroundImage: `url("data:image/png;base64,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")`,
                backgroundSize: "100% 340px",
                backgroundRepeat: "no-repeat",
              }}
            >
              <div className="w-[449px] bg-gradient-to-r from-yellow-300 to-yellow-50 bg-clip-text text-transparent text-[40px] font-medium leading-[70px]">
                “{t("one_story_visionyty")}”
              </div>
              <div>
                <Carousel className="w-[650px]" autoplay>
                  <div style={{ width: 650, height: 174 }}>
                    <div>
                      <div style={{ width: "100%", display: "inline-block" }}>
                        <div className="w-[650px] text-orange-100 text-xl font-normal font-['PingFang SC'] leading-[30px]">
                          “{t("testimonial_1")}”
                        </div>
                        <div className="mt-5 flex space-x-2">
                          <img
                            className="w-16 h-16 rounded-full"
                            src={avatar1Img}
                            alt=""
                          />
                          <div>
                            <h2 className="text-2xl text-yellow-300 font-medium">
                              Alex
                            </h2>
                            <p className="text-xl text-yellow-100">
                              -- {t("testimonial_author_1")}
                            </p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div style={{ width: 650, height: 174 }}>
                    <div>
                      <div style={{ width: "100%", display: "inline-block" }}>
                        <div className="w-[650px] text-orange-100 text-xl font-normal font-['PingFang SC'] leading-[30px]">
                          “{t("testimonial_2")}”
                        </div>
                        <div className="mt-5 flex space-x-2">
                          <img
                            className="w-16 h-16 rounded-full"
                            src={avatar2Img}
                            alt=""
                          />
                          <div>
                            <h2 className="text-2xl text-yellow-300 font-medium">
                              Jennifer
                            </h2>
                            <p className="text-xl text-yellow-100">
                              -- {t("testimonial_author_2")}
                            </p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div style={{ width: 650, height: 174 }}>
                    <div>
                      <div style={{ width: "100%", display: "inline-block" }}>
                        <div className="w-[650px] text-orange-100 text-xl font-normal font-['PingFang SC'] leading-[30px]">
                          “{t("testimonial_3")}”
                        </div>
                        <div className="mt-5 flex space-x-2">
                          <img
                            className="w-16 h-16 rounded-full"
                            src={avatar3Img}
                            alt=""
                          />
                          <div>
                            <h2 className="text-2xl text-yellow-300 font-medium">
                              Ben
                            </h2>
                            <p className="text-xl text-yellow-100">
                              -- {t("testimonial_author_3")}
                            </p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div style={{ width: 650, height: 174 }}>
                    <div>
                      <div style={{ width: "100%", display: "inline-block" }}>
                        <div className="w-[650px] text-orange-100 text-xl font-normal font-['PingFang SC'] leading-[30px]">
                          “{t("testimonial_4")}”
                        </div>
                        <div className="mt-5 flex space-x-2">
                          <img
                            className="w-16 h-16 rounded-full"
                            src={avatar4Img}
                            alt=""
                          />
                          <div>
                            <h2 className="text-2xl text-yellow-300 font-medium">
                              Chloe
                            </h2>
                            <p className="text-xl text-yellow-100">
                              -- {t("testimonial_author_4")}
                            </p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </Carousel>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section className="hidden custom:flex h-[342px] items-center relative">
        <LazyLoadImage
          src={priceBg}
          alt="Price background"
          effect="blur"
          className="absolute top-0 left-0 w-full h-full object-cover z-[-1]"
          wrapperClassName="absolute top-0 left-0 w-full h-full"
          threshold={200}
        />
        <div className={`${style.container} mx-auto`}>
          <div className="flex flex-wrap items-center justify-center lg:justify-between">
            <div className="w-auto text-white text-center lg:w-[620px] lg:text-start relative z-10">
              <h2 className="text-[52px] font-medium leading-[70px]">
                {t("start_creative_journey")}
              </h2>
              <p className="text-xl mt-2">{t("believe_in_dreams")}</p>
            </div>
            <div className="space-x-0 flex flex-col space-y-4 justify-center mt-4 lg:flex-row lg:mt-0 lg:space-y-0 lg:space-x-6">
              <Button
                className="w-[268px] h-[70px] rounded-full bg-white text-black hover:bg-white text-lg"
                onClick={() => {
                  window.location.href = "/workspace";
                }}
              >
                <span>{t("try_now")}</span>
              </Button>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Content;
