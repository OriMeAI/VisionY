/**
 * 案例展示列表
 */
import { Button, Divider, Tooltip } from "antd";
import React, { useEffect, useRef, useState } from "react";
import { useTranslation } from "react-i18next";
import "swiper/css";
import "swiper/css/navigation";
import { Navigation } from "swiper/modules";
import { Swiper, SwiperSlide } from "swiper/react";
import UseTemplateBtn from "../UseTemplateBtn";
import templateArrowLeftIcon from "./../../../../assets/images/pages/workspace/template_arrow_left_icon.svg";
import templateArrowRightIcon from "./../../../../assets/images/pages/workspace/template_arrow_right_icon.svg";
import templateLightCloseIcon from "./../../../../assets/images/pages/workspace/template_light_close.svg";
import templateLightOpenIcon from "./../../../../assets/images/pages/workspace/template_light_open.svg";
import dashboardApi from "./../../../api/dashboardApi";
import { IUserContexts, UserContexts } from "./../../../contexts/user-contexts";
import { TemplateItem } from "./../../../libs/interfaces";
import style from "./style.module.css";

interface IProps {
  usedCount: number;
  totalCount: number;
}

const TemplateList: React.FC<IProps> = ({ usedCount, totalCount }) => {
  const { t } = useTranslation();
  const userContexts: IUserContexts =
    React.useContext<IUserContexts>(UserContexts);
  const [isShowTemplate, setIsShowTemplate] = React.useState(true);
  const [templateList, setTemplateList] = React.useState([]);
  const containerRef = useRef<HTMLDivElement>(null);
  const [isLoading, setIsLoading] = React.useState(true);
  const [isResizing, setIsResizing] = useState(false);
  const resizeTimerRef = useRef<NodeJS.Timeout | null>(null);
  const slideRefs = useRef<(HTMLDivElement | null)[]>([]);

  // 检查元素是否在视口内
  const isElementInViewport = (el: HTMLDivElement | null) => {
    if (!el) return false;
    const rect = el.getBoundingClientRect();
    return (
      rect.top >= 0 &&
      rect.left >= 0 &&
      rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
      rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
  };

  // 处理resize事件
  useEffect(() => {
    const handleResize = () => {
      setIsResizing(true);
      
      // 更新所有slide的可见性
      slideRefs.current.forEach((slide) => {
        if (slide) {
          slide.style.visibility = isElementInViewport(slide) ? 'visible' : 'hidden';
        }
      });
      
      // 清除之前的定时器
      if (resizeTimerRef.current) {
        clearTimeout(resizeTimerRef.current);
      }
      
      // 设置新的定时器
      resizeTimerRef.current = setTimeout(() => {
        setIsResizing(false);
        // 恢复所有slide的可见性
        slideRefs.current.forEach((slide) => {
          if (slide) {
            slide.style.visibility = 'visible';
          }
        });
      }, 200);
    };

    window.addEventListener('resize', handleResize);
    
    return () => {
      window.removeEventListener('resize', handleResize);
      if (resizeTimerRef.current) {
        clearTimeout(resizeTimerRef.current);
      }
    };
  }, []);

  // 获取案例展示列表
  useEffect(() => {
    (async () => {
      const data = await dashboardApi.getTemplateList();
      if (!data.success) return;
      setTemplateList(data.result?.data);
      setIsLoading(false);
    })();
  }, []);

  return (
    <div className={`relative ${style.templateListWrapper}`}>
      <div
        className={`transition-all duration-300 ease-in-out ${
          isShowTemplate ? "h-[331px]" : "h-0"
        } opacity-${isShowTemplate ? 100 : 0}`}
      >
        <div className="bg-gray-100 px-2 pt-3 pb-8 rounded-lg ">
          <div className="flex justify-between items-center px-4">
            <div>
              <h2 className="text-lg font-semibold">{t("case_display")}</h2>
              <p className="text-slate-600">{t("rich_story_cases")}</p>
            </div>
          </div>
          <Divider className="mt-3 mb-6 mx-4 w-[calc(100%-2rem)] min-w-[calc(100%-2rem)]" />
          <div
            className="relative rounded-lg overflow-hidden"
            ref={containerRef}
          >
            <div className="group/hover relative">
              <div id="swiper-container" className="overflow-hidden">
                {isLoading ? (
                  <div className="flex justify-center items-center h-[200px]">
                    {t("loading")}
                  </div>
                ) : templateList.length > 0 ? (
                  <Swiper
                    breakpoints={{
                      1004: {
                        slidesPerView: 2,
                        spaceBetween: 0,
                      },
                      1506: {
                        slidesPerView: 3,
                        spaceBetween: 0,
                      },
                      2008: {
                        slidesPerView: 4,
                        spaceBetween: 0,
                      },
                      2510: {
                        slidesPerView: 5,
                        spaceBetween: 0,
                      },
                      3012: {
                        slidesPerView: 6,
                        spaceBetween: 0,
                      },
                    }}
                    breakpointsBase="container"
                    modules={[Navigation]}
                    navigation={{
                      disabledClass: style.swiperButtonDisabled,
                      lockClass: style.swiperButtonLock,
                      nextEl: ".custom-next-button",
                      prevEl: ".custom-prev-button",
                    }}
                    className="mySwiper"
                  >
                    {templateList.map((item: TemplateItem, index: number) => {
                      return (
                        <SwiperSlide key={`template_item_${item.id}_${index}`}>
                          <div
                            key={`template_item_${item.id}_${index}`}
                            className="shrink-0 grow-0 overflow-hidden px-10"
                            ref={(el) => {
                              slideRefs.current[index] = el;
                            }}
                          >
                            <div
                              className="flex space-x-5 h-[200px] max-w-[1000px]"
                            >
                              <div className="w-[45%] rounded-lg overflow-hidden relative">
                                <img
                                  src={item.cover}
                                  className="w-full h-full max-inline-full block-auto object-cover transition-all duration-300 ease-in-out group-hover:scale-110"
                                />
                              </div>
                              <div className="w-[55%] flex flex-col justify-between">
                                <div className="space-y-2 mb-6">
                                  <h2 className="text-primary font-semibold">
                                    {item.coverTitle}
                                  </h2>
                                  <h2 className="truncate text-lg font-semibold">
                                    {item.name}
                                  </h2>
                                  <p className="text-slate-600 line-clamp-3">
                                    {item.intro}
                                  </p>
                                </div>
                                <div className="space-x-1">
                                  <Button
                                    type="default"
                                    variant="outlined"
                                    onClick={() => {
                                      window.open(`/share/${item.id}`);
                                      // location.href = `/share/${item.id}`;
                                    }}
                                  >
                                    <span>{t("preview")}</span>
                                  </Button>
                                  {userContexts.isAuthenticated ? (
                                    <UseTemplateBtn
                                      templateId={item.id}
                                      usedCount={usedCount}
                                      totalCount={totalCount}
                                    />
                                  ) : (
                                    <Button
                                      type="default"
                                      variant="outlined"
                                      className="text-primary"
                                      onClick={() => {
                                        userContexts.setIsShowLoginModal(true);
                                      }}
                                    >
                                      <span>{t("use_case")}</span>
                                    </Button>
                                  )}
                                </div>
                              </div>
                            </div>
                          </div>
                        </SwiperSlide>
                      );
                    })}
                    {/** CarouselNextArrow */}
                    <button className="custom-next-button absolute right-0 top-1/2 -translate-y-1/2 z-10 pointer-events-auto h-[32px] w-[32px] rounded-full bg-white dark:!bg-white p-2 border-none shadow-sm">
                      <img
                        src={templateArrowRightIcon}
                        alt="template_arrow_right_icon"
                      />
                    </button>

                    {/** CarouselPrevArrow */}
                    <button className="custom-prev-button absolute left-0 top-1/2 -translate-y-1/2 z-10 pointer-events-auto h-[32px] w-[32px] rounded-full bg-white dark:!bg-white p-2 border-none shadow-sm">
                      <img
                        src={templateArrowLeftIcon}
                        alt="template_arrow_left_icon"
                      />
                    </button>
                  </Swiper>
                ) : (
                  <div className="flex justify-center items-center h-[200px]">
                    {t("loading")}
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
      <Tooltip
        title={isShowTemplate ? t("collapse") : t("case_display")}
        placement="top"
      >
        <Button
          type="default"
          size="large"
          variant="outlined"
          className="absolute right-6 top-5 ml-6 z-10"
          style={{ padding: "0 8px" }}
          onClick={() => {
            setIsShowTemplate(!isShowTemplate);
          }}
        >
          <div className="w-5 h-5">
            {isShowTemplate ? (
              <img src={templateLightOpenIcon} alt="template_light_open_icon" />
            ) : (
              <img
                src={templateLightCloseIcon}
                alt="template_light_close_icon"
              />
            )}
          </div>
        </Button>
      </Tooltip>
    </div>
  );
};

export default TemplateList;
