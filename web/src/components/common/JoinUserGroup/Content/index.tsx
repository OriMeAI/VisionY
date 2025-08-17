/**
 * 加入用户群内容
 */
import * as React from "react";
import ucLogo from "./../../../../../assets/images/pages/usercenter/CYLogoVe-BYw8-5am.png";
import { useTranslation } from "react-i18next";

interface IProps {}

const Content: React.FC<IProps> = ({}) => {
  const {t} = useTranslation();
  return (
    <div className="w-[400px] overflow-hidden">
      <div className="flex flex-col items-center">
        <div className="relative w-[336px] flex justify-center">
          <img
            className="h-[336px] w-[336px] absolute -top-[78px]"
            src="data:image/svg+xml,%3csvg%20width='336'%20height='218'%20viewBox='0%200%20336%20218'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cmask%20id='mask0_5265_104284'%20style='mask-type:alpha'%20maskUnits='userSpaceOnUse'%20x='0'%20y='-118'%20width='336'%20height='336'%3e%3crect%20width='336'%20height='336'%20transform='translate(0%20-118)'%20fill='url(%23paint0_radial_5265_104284)'/%3e%3c/mask%3e%3cg%20mask='url(%23mask0_5265_104284)'%3e%3ccircle%20cx='168'%20cy='50'%20r='47.5'%20stroke='%23EAECF0'/%3e%3ccircle%20cx='168'%20cy='50'%20r='47.5'%20stroke='%23EAECF0'/%3e%3ccircle%20cx='168'%20cy='50'%20r='71.5'%20stroke='%23EAECF0'/%3e%3ccircle%20cx='168'%20cy='50'%20r='95.5'%20stroke='%23EAECF0'/%3e%3ccircle%20cx='168'%20cy='50'%20r='119.5'%20stroke='%23EAECF0'/%3e%3ccircle%20cx='168'%20cy='50'%20r='143.5'%20stroke='%23EAECF0'/%3e%3ccircle%20cx='168'%20cy='50'%20r='167.5'%20stroke='%23EAECF0'/%3e%3c/g%3e%3cdefs%3e%3cradialGradient%20id='paint0_radial_5265_104284'%20cx='0'%20cy='0'%20r='1'%20gradientUnits='userSpaceOnUse'%20gradientTransform='translate(168%20168)%20rotate(90)%20scale(168%20168)'%3e%3cstop/%3e%3cstop%20offset='1'%20stop-opacity='0'/%3e%3c/radialGradient%3e%3c/defs%3e%3c/svg%3e"
            alt=""
          />
          <img
            className="w-12 h-12 mt-2"
            src={ucLogo}
            alt=""
          />
        </div>
        <div className="relative z-10 mt-4">
          <h2 className="text-center font-semibold text-lg">{t('join_user_group2')}</h2>
          <p className="text-slate-600 text-center text-sm">
            {t('join_user_group_info')}
          </p>
        </div>
        <div className="bg-background w-[304px] mt-5 flex flex-col items-center py-6 rounded-lg">
          <img
            className="w-[120px] h-[120px]"
            src="https://static.chuangyi-keji.com/home/qrcodeVideoGroup.png"
            alt=""
          />
          <p className="text-sm text-slate-600 mt-3">{t('scan_qr_code')}</p>
        </div>
      </div>
    </div>
  );
};

export default Content;
