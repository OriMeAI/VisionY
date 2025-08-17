/**
 * 通用底部组件
 */
import * as React from "react";

import { LOGO_BASE64_SRC_DARK } from "../../../../libs/global-config";
import { useTranslation } from "react-i18next";
import style from "./style.module.css";

const Footer: React.FC = () => {
  const {t} = useTranslation();
  const startYear = 2023;
  const currentYear = new Date().getFullYear();
  const yearDisplay = startYear === currentYear ? currentYear : `${startYear}-${currentYear}`;

  return (
    <>
      <div className={`${style.container} py-8 mx-auto flex md:items-center lg:items-start md:flex-row md:flex-nowrap flex-wrap flex-col`}>
        <div className="w-64 space-y-9 flex-shrink-0 md:mx-0 mx-auto text-center md:text-left">
          <a className="flex items-center md:justify-start justify-center text-gray-900">
            <img src={LOGO_BASE64_SRC_DARK} width={40} height={40} alt="" />
          </a>
          <p className="mt-2 text-sm text-gray-200">
            {t('visiony_slogan')}
          </p>
        </div>
        <div className="flex-grow flex flex-wrap md:pl-20 -mb-10 md:mt-0 mt-10 justify-center md:justify-end">
          <div className="lg:w-1/4 md:w-1/2 w-full text-center md:text-right">
            <h2 className="title-font font-medium text-[#F0F1D8] tracking-widest text-xl mb-3">
              {t('about_us')}
            </h2>
            <nav className="list-none mb-10 space-y-1">
              <li>
                <a
                  href="/aboutus"
                  className="text-stone-300 hover:text-stone-500"
                  target="_blank"
                >
                  VisionY
                </a>
              </li>
            </nav>
          </div>
          <div className="lg:w-1/4 md:w-1/2 w-full text-center md:text-right">
            <h2 className="title-font font-medium text-[#F0F1D8] tracking-widest text-xl mb-3">
              {t('support_and_service')}
            </h2>
            <nav className="list-none mb-10">
              <li>
                <a
                  href="/termsofuse"
                  target="_blank"
                  className="text-stone-300 hover:text-stone-500"
                >
                  {t('terms_of_use')}
                </a>
              </li>
              <li>
                <a
                  href="/privacypolicy"
                  target="_blank"
                  className="text-stone-300 hover:text-stone-500"
                >
                  {t('privacy_policy')}
                </a>
              </li>
            </nav>
          </div>
        </div>
      </div>
      <div className="border-t border-stone-600">
        <div className={`${style.container} mx-auto py-2 flex flex-wrap flex-row justify-center`}>
          <p className="text-neutral-400 text-xs text-center">
            Copyright © {yearDisplay} VisionY. All rights reserved.
          </p>
        </div>
      </div>
    </>
  );
};

export default Footer;
