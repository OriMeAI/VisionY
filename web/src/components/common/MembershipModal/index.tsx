/**
 * VIP会员订阅
 */
import { Button, Tag,Segmented,App } from "antd";
import * as React from "react";
import { createPortal } from "react-dom";
import { useTranslation } from "react-i18next";
import ModalBase from "../../client/Common/ModalBase";
// import pricingApi from "../../../api/pricingPaypalApi";
import pricingApi from "../../../api/pricingStripeApi";
import { IUserContexts, UserContexts } from "../../../contexts/user-contexts";
import { IModalContexts, ModalContexts } from "../../../contexts/modal-contexts";
import { PLAN_ICON_MAPS } from "./../../../libs/global-config";
import { MemberType } from "./../../../libs/enums";
import { PlanItemType } from "./../../../libs/interfaces";
import userApi from "../../../api/userApi";

interface IProps {
  membershipPlanList:PlanItemType[];
  currentMemberType: MemberType;
  handleSubscription:(planId:number)=>void;
}

const SubscribeOptionList: React.FC<IProps> = ({
  membershipPlanList,
  currentMemberType,
  handleSubscription
}: IProps) => {
  const { t } = useTranslation();
  const userContexts: IUserContexts = React.useContext<IUserContexts>(UserContexts);
  const modalContexts: IModalContexts =React.useContext<IModalContexts>(ModalContexts);

  return (
      <div className="grid grid-cols-3 gap-6 mx-auto auto-rows-fr">
        {Array.isArray(membershipPlanList) && membershipPlanList.length > 0
          ? membershipPlanList
              .filter((item) => item.cycle === currentMemberType)
              .map((planItem: PlanItemType, index: number) => (
                <div
                  key={`plan_item_${planItem.id}_${index}`}
                  className="flex flex-col rounded-2xl border justify-self-center w-full max-w-[310px]"
                >
                  <div className="flex flex-col items-center justify-center px-8 pt-8">
                    <div className="w-12 h-12 flex items-center justify-center rounded-full bg-purple-100">
                      {planItem.icon ? (
                        <img
                          src={
                            PLAN_ICON_MAPS[
                              planItem.icon as keyof typeof PLAN_ICON_MAPS
                            ]
                          }
                        />
                      ) : null}
                    </div>
                    <p className="text-xl font-semibold mt-4 text-violet-700 flex items-center">
                      {planItem.name}
                      {planItem.strikePrice &&
                      planItem.strikePrice > planItem.price ? (
                        <Tag
                          color="purple"
                          className="ml-2 rounded-full text-primary font-normal"
                        >
                          {t('half_price_discount')}
                        </Tag>
                      ) : null}
                    </p>

                    <div className="text-5xl font-semibold text-gray-900 leading-[60px] mt-2">
                      <div className="text-2xl text-[#101828]/20 ml-1 inline mr-1">
                        {planItem.strikePrice &&
                        planItem.strikePrice > planItem.price ? (
                          <p className="inline">
                            <span className="text-2xl line-through">$</span>
                            <span className="text-4xl line-through">
                              {planItem.strikePrice}
                            </span>
                          </p>
                        ) : null}
                      </div>
                      {planItem.price ? (
                        <span className="text-2xl">$</span>
                      ) : null}
                      <span className="ml-1">
                        {planItem.price ? planItem.price : "定制"}
                      </span>
                    </div>
                    <p className="text-slate-600 mt-2">
                      {planItem.description}
                    </p>
                  </div>
                  <div className="flex flex-col items-center justify-center px-8 pt-8 pb-8 flex-1">
                    <ul className="self-stretch flex-1 space-y-4">
                      {Array.isArray(planItem?.features) &&
                      planItem?.features.length > 0
                        ? planItem?.features.map(
                            (featureItem: string, index) => (
                              <li
                                key={`feature_item_${index}`}
                                className="flex justify-start items-start space-x-3"
                              >
                                <img
                                  className="w-6 h-6"
                                  src="data:image/svg+xml,%3csvg%20width='24'%20height='24'%20viewBox='0%200%2024%2024'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cg%20id='Check%20icon'%3e%3cpath%20d='M0%2012C0%205.37258%205.37258%200%2012%200C18.6274%200%2024%205.37258%2024%2012C24%2018.6274%2018.6274%2024%2012%2024C5.37258%2024%200%2018.6274%200%2012Z'%20fill='%23F9F5FF'/%3e%3cpath%20id='Icon'%20fill-rule='evenodd'%20clip-rule='evenodd'%20d='M17.096%207.38967L9.93602%2014.2997L8.03602%2012.2697C7.68602%2011.9397%207.13602%2011.9197%206.73602%2012.1997C6.34602%2012.4897%206.23602%2012.9997%206.47602%2013.4097L8.72602%2017.0697C8.94602%2017.4097%209.32601%2017.6197%209.75601%2017.6197C10.166%2017.6197%2010.556%2017.4097%2010.776%2017.0697C11.136%2016.5997%2018.006%208.40967%2018.006%208.40967C18.906%207.48967%2017.816%206.67967%2017.096%207.37967V7.38967Z'%20fill='%237F56D9'/%3e%3c/g%3e%3c/svg%3e"
                                  alt=""
                                />
                                <span className="text-sm text-slate-600 leading-tight">
                                  {featureItem}
                                </span>
                              </li>
                            )
                          )
                        : null}
                    </ul>
                  </div>
                  <div className="px-8 mb-8">
                    {planItem.strikePrice && planItem.strikePrice > planItem.price ? (
                      <Button
                        size="large"
                        type="primary"
                        className="w-full"
                        onClick={ async () => {
                          modalContexts.setIsShowMembershipModal(false);
                          if(userContexts.isAuthenticated){ // bysoongxl 订阅会员
                            const planId = planItem.id;
                            console.log("subscribe planId is:",planId)
                            await handleSubscription(planId);
                          }else{
                            userContexts.setIsShowLoginModal(true)
                          }
                        }}
                      >
                        <span>{userContexts.isAuthenticated?t('subscribe_now'): t('login_to_subscribe')}</span>
                      </Button>
                    ) : null}
                    {planItem.price && parseFloat(planItem.price) === 0 ? (
                      <Button
                        size="large"
                        type="primary"
                        ghost
                        className="w-full"
                        onClick={() => {
                          modalContexts.setIsShowMembershipModal(false);
                        }}
                      >
                        <span>{t('free_trial')}</span>
                      </Button>
                    ) : null}
                  </div>
                </div>
              ))
          : null}
      </div>
  );
};

interface IMembershipModalProps {
  
}

const MembershipModal: React.FC<IMembershipModalProps> = ({
  
}: IMembershipModalProps) => {
  const { t } = useTranslation();
  const { message: messageApi } = App.useApp();
  const userContexts: IUserContexts = React.useContext<IUserContexts>(UserContexts);
  const modalContexts: IModalContexts =React.useContext<IModalContexts>(ModalContexts);
  const [currentMemberType, setCurrentMemberType] = React.useState<MemberType>(
    MemberType.ANNUAL
  );

  const [isShowModal, setIsShowModal] = React.useState(false);
  const [membershipPlanList, setMembershipPlanList] = React.useState<PlanItemType[]>([]);
  
  const handleModalCancel = async () => {
    modalContexts.setIsShowMembershipModal(false);
  };

  const onSegmentedChange = (value: MemberType) => {
    setCurrentMemberType(value);
  };

  React.useEffect(() => {
    (async () => {
      if (modalContexts.isShowMembershipModal) {
        const data = await pricingApi.getPlanList();
        setMembershipPlanList(data.result?.data || []);
        setIsShowModal(true);
      }else{
        setIsShowModal(false);
      }
    })();
  }, [modalContexts.isShowMembershipModal]);

  //处理前进或者后退导致的loading显示问题
  React.useEffect(() => {
    const handlePopState = (event: PopStateEvent) => {
      modalContexts.setIsShowMembershipLoading(false);
    };

    window.addEventListener('popstate', handlePopState);
    
    return () => {
      window.removeEventListener('popstate', handlePopState);
    };
  }, []);

  React.useEffect(() => {
    modalContexts.setIsShowMembershipLoading(false);
    const params = new URLSearchParams(window.location.search);
    const subscription_result = params.get("subscription_result");

    if(subscription_result){
      console.log("window.location.search:",window.location.search)
      const token = params.get("token");

      for (const [key, value] of params) {
        console.log(`window.location.search ${key}: ${value}`);
      }

      window.history.replaceState({}, "", window.location.pathname);
  
      if (subscription_result === "success" && token) {
        verifySubscription(token);
      }else if (subscription_result === "cancel" && token) {
        cancelSubscription(token);
      }
    }
  }, []);

  const handleSubscription = async (planId:number) => {
    modalContexts.setIsShowMembershipLoading(true);
    const res = await pricingApi.createSubscription({
      planId: planId,
      returnUrl: window.location.href,
      cancelUrl: window.location.href,
    });
    if (res.success && res.result?.code === 0) {
      if (res.result?.data) {
        window.location.href = res.result.data.approval_url;
      }
    } else {
      modalContexts.setIsShowMembershipLoading(false);
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };

  const verifySubscription = async (token:string) => {
    modalContexts.setIsShowMembershipLoading(true);
    const res = await pricingApi.verifySubscription({
      token: token,
    });
    modalContexts.setIsShowMembershipLoading(false);
    if (res.success && res.result?.code === 0) {
      if (res.result?.msg) {
        messageApi.success(res.result.msg);

        const data = await userApi.getUserInfo();
        if (data.result?.data) {
          userContexts.setUserInfo(data.result.data);
        }

        // 延迟一点时间让状态更新完成后再重新加载
        // setTimeout(() => {
        //   window.location.reload();
        // }, 1000);
      }
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };

  const cancelSubscription = async (token:string) => {
    await pricingApi.cancelSubscription({
      token: token
    });
    messageApi.error(t('subscription_cancelled'));

    // 延迟一点时间让状态更新完成后再重新加载
    // setTimeout(() => {
    //   window.location.reload();
    // }, 1000);
  }
  
  return (
    <>
      {createPortal(
        <ModalBase
          open={isShowModal}
          width={1026}
          height={undefined}
          onCancel={handleModalCancel}
          showFooter={false}
        >
          <div
            className="w-auto grid gap-4 pt-[24px] px-[24px]"
          >
            <div className="mb-4 space-y-4 text-center">
              <h2 className="text-3xl font-semibold text-indigo-900 mt-3 mb-5 text-center">
                {t("subscribe_membership")}
              </h2>
              <p className="text-center mb-5 text-slate-600">
                {t("subscribe_note")}
              </p>
              <div className="flex items-center justify-center space-x-3">
                <Segmented
                  className="p-1 font-semibold bg-background border-gray-300 rounded-full"
                  size="large"
                  options={[
                    {
                      label: t("monthly_membership"),
                      value: MemberType.MONTHLY,
                    },
                    {
                      label: (
                        <div className="flex items-center">
                          {t("annual_membership")}
                          <Tag
                            color="purple"
                            className="ml-1 cursor-pointer mr-0 rounded-full font-normal text-primary"
                          >
                            {t("extra_two_months_discount")}
                          </Tag>
                        </div>
                      ),
                      value: MemberType.ANNUAL,
                    },
                  ]}
                  value={currentMemberType}
                  onChange={onSegmentedChange}
                />
              </div>
            </div>
            <SubscribeOptionList 
              membershipPlanList = {membershipPlanList}
              currentMemberType={currentMemberType} 
              handleSubscription={handleSubscription}
            />
            <p className="mt-6 text-slate-600 text-sm">{t("membership_usage_note")}</p>
            <p className="mt-1 mb-10 text-slate-600 text-sm">{t("credits_used_rules")}</p>
          </div>
        </ModalBase>,
        document.body
      )}
    </>
  );
};

export default MembershipModal;