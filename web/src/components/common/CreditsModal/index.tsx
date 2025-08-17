/**
 * 购买生图次数
 */
import { Button, Input, Tag, App } from "antd";
import * as React from "react";
import { createPortal } from "react-dom";
import { useTranslation } from "react-i18next";
import ModalBase from "../../client/Common/ModalBase";
// import pricingApi from "../../../api/pricingPaypalApi";
import pricingApi from "../../../api/pricingStripeApi";
import { CreditsItemType } from "../../../libs/interfaces";
import { IUserContexts, UserContexts } from "../../../contexts/user-contexts";
import { IModalContexts, ModalContexts } from "../../../contexts/modal-contexts";
import userApi from "../../../api/userApi";

interface IProps {
  
}

const CreditsModal: React.FC<IProps> = ({
  
}: IProps) => {
  const { t } = useTranslation();
  const userContexts: IUserContexts = React.useContext<IUserContexts>(UserContexts);
  const modalContexts: IModalContexts = React.useContext<IModalContexts>(ModalContexts);
  const [creditsItemList, setCreditsItemList] = React.useState<CreditsItemType[]>([]);
  const { message: messageApi } = App.useApp();

  const [isShowModal, setIsShowModal] = React.useState(false);

  //处理前进或者后退导致的loading显示问题
  React.useEffect(() => {
    const handlePopState = (event: PopStateEvent) => {
      modalContexts.setIsShowCreditsLoading(false);
    };

    window.addEventListener('popstate', handlePopState);
    
    return () => {
      window.removeEventListener('popstate', handlePopState);
    };
  }, []);

  React.useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const credits_result = params.get("credits_result");

    if(credits_result){
      console.log("window.location.search:",window.location.search)
      const token = params.get("token");

      window.history.replaceState({}, "", window.location.pathname);
  
      if (credits_result === "success") {
        capturePayment(token,);
      }else if (credits_result === "cancel") {
        cancelPayment(token);
      }
    }
  }, []);

  React.useEffect(() => {
    (async () => {
      if (modalContexts.isShowCreditsModal) {
        const data = await pricingApi.getCreditsItem();
        setCreditsItemList(data.result?.data);
        setIsShowModal(true);
      }else{
        setIsShowModal(false);
      }
    })();
  }, [modalContexts.isShowCreditsModal]);

  const handlePayment = async (itemId:number,amount:number) => {
    modalContexts.setIsShowCreditsLoading(true);
    const res = await pricingApi.createPayment({
      itemId: itemId,
      amount: amount,
      returnUrl: window.location.href,
      cancelUrl: window.location.href,
    });
    if (res.success && res.result?.code === 0) {
      if (res.result?.data) {
        window.location.href = res.result.data.approval_url;
      }
    } else {
      modalContexts.setIsShowCreditsLoading(false);
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };

  const capturePayment = async (token:string) => {
    modalContexts.setIsShowCreditsLoading(true);
    const res = await pricingApi.capturePayment({
      token: token
    });
    modalContexts.setIsShowCreditsLoading(false);
    if (res.success && res.result?.code === 0) {
      if (res.result?.msg) {
        messageApi.success(res.result.msg);

        // 只有当前路径包含 usercenter 时才重新加载页面
        if (window.location.pathname.includes('usercenter')) {
          setTimeout(() => {
            window.location.reload();
          }, 1000);
        }else{
          const data = await userApi.getUserInfo();
          if (data.result?.data) {
            userContexts.setUserInfo(data.result.data);
          }
        }
      }
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };

  const cancelPayment = async (token:string) => {
    await pricingApi.cancelPayment({
      token: token
    });
    messageApi.error(t('payment_cancelled'));

    // 只有当前路径包含 usercenter 时才重新加载页面
    // if (window.location.pathname.includes('usercenter')) {
    //   setTimeout(() => {
    //     window.location.reload();
    //   }, 1000);
    // }
  }

  const handleModalCancel = async () => {
    modalContexts.setIsShowCreditsModal(false);
  };

  return (
    <>
      {createPortal(
        <ModalBase
          open={isShowModal}
          width={600}
          height={undefined}
          onCancel={handleModalCancel}
          showFooter={false}
        >
          <div className="grid gap-4 min-w-[600px] pt-[24px] px-[24px]">
            <h2 className="text-3xl font-semibold text-indigo-900 mt-3 mb-5 text-center">
              {t("purchase_generate_credits")}
            </h2>
            <p className="text-center mb-5 text-slate-600">
              {t("purchase_note")}
            </p>
            <ul className="grid grid-cols-2 gap-4 justify-center">
              {Array.isArray(creditsItemList) && creditsItemList.length > 0
                ? creditsItemList.map(
                    (item: CreditsItemType, index: number) => (
                      <li
                        key={`credits_item_${item.id}_${index}`}
                        className="rounded-xl border px-5 py-4 flex flex-col items-center justify-between relative h-[164px]"
                      >
                        <p className="h-[40px] leading-[40px]">
                          <span className="text-lg font-semibold">
                            {item.name}
                          </span>
                        </p>
                        {item.isFirstRecharge ? (
                          <Tag
                            color="purple"
                            className="text-primary cursor-pointer rounded-lg rounded-tl-none rounded-br-none m-0 absolute top-0 right-0"
                            style={{ marginTop: 0 }}
                          >
                            {t("first_recharge_discount")}
                          </Tag>
                        ) : null}
                        <h2 className="text-base text-primary font-bold">
                          ${item.price}
                        </h2>
                        <Button
                          type="primary"
                          size="large"
                          className="px-8"
                          onClick={async () => {
                            modalContexts.setIsShowCreditsModal(false);
                            if(userContexts.isAuthenticated){
                              const itemId = item.id;
                              const price = item.price;
                              console.log("buy item info :",itemId,price)
                              await handlePayment(itemId,Number(price));
                            }else{
                              userContexts.setIsShowLoginModal(true)
                            }
                          }}
                        >
                          <span>{userContexts.isAuthenticated?t('buy_now'): t('login_to_buy')}</span>
                        </Button>
                      </li>
                    )
                  )
                : null}
            </ul>
            <p className="mt-6 text-slate-600 text-sm">{t("usage_note")}</p>
            <p className="mt-1 mb-10 text-slate-600 text-sm">{t("credits_used_rules")}</p>
          </div>
        </ModalBase>,
        document.body
      )}
    </>
  );
};

export default CreditsModal;
