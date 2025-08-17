/**
 * 用户中心权益信息组件
 */
import type { TableColumnsType } from "antd";
import { Button, Table, App, Spin } from "antd";
import React, { useRef, useState, useContext, useEffect, useCallback } from "react";
import { useTranslation } from "react-i18next";
import userApi from "./../../../../api/userApi";
import {
  UsageRecordDataItemType,
} from "./../../../../libs/interfaces";
import {
  IModalContexts,
  ModalContexts,
} from "./../../../../contexts/modal-contexts";

interface IProps {
}

const UsageLogContent: React.FC<IProps> = () => {
  const { t } = useTranslation();
  const { message: messageApi } = App.useApp();

  const columns: TableColumnsType<UsageRecordDataItemType> = [
    {
      title: t("usage_time"),
      dataIndex: "usedTime",
      align: 'center',
    },
    {
      title: t("usage_token"),
      dataIndex: "usedToken",
      // align: 'center',
    },
    {
      title: t("usage_name"),
      dataIndex: "typeDesc",
      // align: 'center',
    },
    {
      title: t("credits_source"),
      dataIndex: "creditsSource",
      align: 'center',
    },
    {
      title: t("usage_credits"),
      dataIndex: "quantity",
      align: 'center',
      render: (text, record) => {
        return (
          <span>{`-${record.quantity}`}</span>
        );
      },
    },
  ];

  const containerRef = useRef<HTMLDivElement>(null);
  const scrollTimeoutRef = useRef<NodeJS.Timeout | null>(null);
  const modalContexts: IModalContexts = useContext<IModalContexts>(ModalContexts);

  const [tableHeight, setTableHeight] = useState(0);
  const [loading, setLoading] = useState<boolean>(false);
  const [initialLoading, setInitialLoading] = useState<boolean>(true);
  const [hasMore, setHasMore] = useState<boolean>(true);
  const [records, setRecords] = useState<UsageRecordDataItemType[]>([]);
  const [currentPage, setCurrentPage] = useState<number>(1);
  const [pageSize] = useState<number>(20);

  // 计算表格高度
  useEffect(() => {
    const updateHeight = () => {
      if (containerRef.current) {
        const containerHeight = containerRef.current.offsetHeight;
        const tableHeaderHeight = 55;
        const tableFooterHeight = 54;
        const contentMarginBottom = 0; //24;
        const newHeight = containerHeight - tableHeaderHeight - tableFooterHeight - contentMarginBottom;
        setTableHeight(newHeight > 0 ? newHeight : 0);
      }
    };

    updateHeight();
    window.addEventListener("resize", updateHeight);
    return () => window.removeEventListener("resize", updateHeight);
  }, []);

  // 加载数据函数
  const loadMoreData = useCallback(async (pageNum: number, isInitial = false) => {
    if (loading || (!hasMore && !isInitial)) return;
    
    setLoading(true);
    if (isInitial) setInitialLoading(true);
    
    try {
      const res = await userApi.getUsageRecordByPage({
        pageSize: pageSize,
        pageNum: pageNum,
      });
      
      if (res.success && res.result?.code === 0) {
        const newRecords = res.result?.data.records || [];
        
        if (pageNum === 1) {
          setRecords(newRecords);
        } else {
          setRecords(prev => [...prev, ...newRecords]);
        }
        
        // 更新分页状态
        setCurrentPage(pageNum);
        
        // 判断是否还有更多数据
        const total = res.result?.data.total || 0;
        setHasMore(newRecords.length === pageSize && total > pageNum * pageSize);
      } else {
        if (res.result?.msg) {
          messageApi.error(res.result.msg);
        }
      }
    } catch (error) {
      console.error("Load usage log failed:", error);
    } finally {
      setLoading(false);
      if (isInitial) setInitialLoading(false);
    }
  }, [loading, hasMore, pageSize, messageApi]);

  // 初始化加载第一页数据
  useEffect(() => {
    loadMoreData(1, true);
  }, []);

  // 滚动加载处理函数
  const handleScroll = useCallback((e: Event) => {
    const target = e.target as HTMLElement;
    if (!target) return;
    
    // 防抖处理
    if (scrollTimeoutRef.current) {
      clearTimeout(scrollTimeoutRef.current);
    }
    
    scrollTimeoutRef.current = setTimeout(() => {
      const { scrollTop, scrollHeight, clientHeight } = target;
      const threshold = 100; // 提前100px开始加载
      
      // 检查是否接近底部
      const isNearBottom = scrollHeight - scrollTop - clientHeight < threshold;
      
      if (isNearBottom && !loading && hasMore) {
        const nextPage = currentPage + 1;
        loadMoreData(nextPage);
      }
    }, 150); // 150ms防抖
  }, [loading, hasMore, currentPage, loadMoreData]);

  // 监听滚动事件
  useEffect(() => {
    const scrollContainer = document.querySelector('.ant-table-body');
    if (!scrollContainer) return;
    
    scrollContainer.addEventListener('scroll', handleScroll, { passive: true });
    
    return () => {
      scrollContainer.removeEventListener('scroll', handleScroll);
      if (scrollTimeoutRef.current) {
        clearTimeout(scrollTimeoutRef.current);
      }
    };
  }, [handleScroll]);

  // 自定义表格底部加载提示
  const renderFooter = () => {
    if (loading && records.length > 0) {
      return (
        <div className="text-center">
          <Spin size="small" />
          <span className="ml-2 text-gray-500">{t('loading_more')}</span>
        </div>
      );
    }
    
    if (!hasMore) {
      return (
        <div className="text-center text-gray-500">
          {t('no_more_data')}
        </div>
      );
    }
    
    return (
      <div className="text-center text-gray-500">
        {t('reach_bottom_load_more')}
      </div>
    );
  };

  return (
    <div className="flex-1 flex flex-col w-full space-y-6">
      <div className="flex justify-between items-center">
        <div className="px-2 text-sm text-slate-600">
          {t("credits_usage_log_desc")}
        </div>
        <Button
          type="primary"
          size="large"
          variant="solid"
          ghost={true}
          onClick={() => {
            modalContexts.setIsShowCreditsModal(true);
          }}
        >
          <span>{t("purchase_generate_credits")}</span>
        </Button>
      </div>
      
      <div className="flex-1 flex flex-col" ref={containerRef}>
        <Spin spinning={initialLoading} tip={t('loading_more')}>
          <Table<UsageRecordDataItemType>
            columns={columns}
            dataSource={records.map((record,index) => ({
              ...record,
              usedTime: new Date(record.usedTime).toLocaleString('sv-SE'),
              key: record.usedToken + index,
            }))}
            pagination={false}
            scroll={{ y: tableHeight }}
            footer={renderFooter}
            locale={{
              emptyText: initialLoading ? '' : t('no_data'),
            }}
          />
        </Spin>
      </div>
    </div>
  );
};

export default UsageLogContent;