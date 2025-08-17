/**
 * 用户中心内容区域
 */
import React, { useRef, useState,useContext,useEffect } from "react";
import { useTranslation } from "react-i18next";
import { Segmented , App, Tag } from "antd";
import { IUserContexts, UserContexts } from "./../../../contexts/user-contexts";
import RechargeLogContent from "./RechargeLogContent";
import UsageLogContent from "./UsageLogContent";
import ObtainedLogContent from "./ObtainedLogContent";

import userApi from "../../../api/userApi";
import {
  CreditsRecordItemType,
} from "../../../libs/interfaces";

interface IProps {}

const Content: React.FC<IProps> = () => {
  const { t } = useTranslation();
  const { message: messageApi } = App.useApp();
  const userContexts: IUserContexts = useContext<IUserContexts>(UserContexts);
  const [activeTab, setActiveTab] = useState<string>("usageLog");
  const segmentedRef = useRef<HTMLDivElement>(null);
  const [creditsRecords, setCreditsRecords] = useState<CreditsRecordItemType>(null);

  // 获取用户积分记录
  useEffect(() => {
    (async () => {
      if (userContexts.isAuthenticated) {
        const res = await userApi.getCreditsRecord();
        
        if (res.success && res.result?.code === 0) {
          const records = res.result?.data;

          setCreditsRecords(records);
        } else {
          if (res.result?.msg) {
            messageApi.error(res.result.msg);
          }
        }
      }
    })();
  }, [userContexts.isAuthenticated]);

  const onSegmentedChange = (value: string) => {
    setActiveTab(value);
  };

  const renderContent = () => {
    switch (activeTab) {
      case "usageLog":
        return <UsageLogContent />;
      case "rechargeLog":
        return <RechargeLogContent />;
      case "obtainedLog":
        return <ObtainedLogContent />;
      default:
        return <RechargeLogContent />;
    }
  };

  return (
    <div className="flex-1 flex flex-col w-full mx-auto max-w-[1024px] p-6">
      <div className="flex items-center justify-center gap-2 pt-2 pb-6 font-semibold">
        <span className=" text-gray-500">
          {t("membership_level")}
        </span>
        <Tag color="purple" className=" bg-purple-100 text-purple-700 text-base">
          {userContexts.userInfo?.planName}
        </Tag>
        {/* 如果planExpiryTime不是空字符串，那么显示 */}
        {userContexts.userInfo?.planExpiryTime && (
          <>
            <span className=" text-gray-500">
              {t("plan_expiry_time")}
            </span>
            <span className="text-sm text-gray-500">
              {new Date(userContexts.userInfo.planExpiryTime).toLocaleString('sv-SE')}
            </span>
          </>
        )}
      </div>
      {/* 积分信息展示区域 */}
      <div className="bg-gray-50 rounded-lg p-4  border-gray-200">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
          <div className="bg-white rounded-lg p-3 shadow-sm">
            <div className="text-sm text-gray-500 mb-1">{t("total_credits")}</div>
            <div className="text-xl font-bold text-indigo-900">
              {creditsRecords?.totalCredits?.toLocaleString() || 0}
            </div>
          </div>
                    
          <div className="bg-white rounded-lg p-3 shadow-sm">
            <div className="text-sm text-gray-500 mb-1">{t("free_credits")}</div>
            <div className="text-xl font-bold text-blue-600">
              {creditsRecords?.freeCredits?.toLocaleString() || 0}
            </div>
          </div>
          
          <div className="bg-white rounded-lg p-3 shadow-sm">
            <div className="text-sm text-gray-500 mb-1">{t("membership_credits")}</div>
            <div className="text-xl font-bold text-purple-600">
              {creditsRecords?.membershipCredits?.toLocaleString() || 0}
            </div>
          </div>

          <div className="bg-white rounded-lg p-3 shadow-sm">
            <div className="text-sm text-gray-500 mb-1">{t("purchase_credits")}</div>
            <div className="text-xl font-bold text-orange-600">
              {creditsRecords?.purchaseCredits?.toLocaleString() || 0}
            </div>
          </div>

        </div>
      </div>
      <div
        className="flex items-center justify-center my-6"
        ref={segmentedRef}
      >
        <Segmented
          className="p-1 font-semibold bg-background border-gray-300 rounded-full"
          size="large"
          options={[
            {
              label: t("usage_log"),
              value: "usageLog",
            },
            {
              label: t("obtained_log"),
              value: "obtainedLog",
            },
            {
              label: t("recharge_log"),
              value: "rechargeLog",
            },
          ]}
          value={activeTab}
          onChange={onSegmentedChange}
        />
      </div>
      <div className="flex-1 flex flex-col">
        {renderContent()}
      </div>
    </div>
  );
};

export default Content;