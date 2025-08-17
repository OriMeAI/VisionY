/**
 * 分镜表页面
 */

import { Tour, TourProps } from "antd";
import React, { useRef, useState } from "react";
import { useTranslation } from "react-i18next";
import { useParams } from "react-router-dom";
import {
  ITableViewContexts,
  TableViewContexts,
} from "./../contexts/table-view-contexts";

import TableContainer from "./../TableContainer";

interface IProps {}

const TableView: React.FC<IProps> = ({}: IProps) => {
  const { t } = useTranslation();
  const { projectId } = useParams<{ projectId: string }>();
  const [tableLoading, setTableLoading] = useState<boolean>(true);
  const [isRepaintModalOpen, setIsRepaintModalOpen] = useState<boolean>(false);
  const tourRef1 = useRef(null);
  const tourRef2 = useRef(null);

  const tourRef3 = useRef(null);
  const [isTourOpen, setIsTourOpen] = useState<boolean>(false);

  const steps: TourProps["steps"] = [
    {
      title: t("tableview_tour_step1_title"),
      description: t("tableview_tour_step1_description"),
      target: () => tourRef1.current,
    },
    {
      title: t("tableview_tour_step2_title"),
      description: t("tableview_tour_step2_description"),
      target: () => tourRef2.current,
    },
    {
      title: t("tableview_tour_step3_title"),
      description: t("tableview_tour_step3_description"),
      target: () => tourRef3.current,
    },
  ];
  const value = React.useMemo(
    () => ({
      setIsTourOpen,
      tourRef1,
      tourRef2,
      tourRef3,
      setTableLoading,
      tableLoading,
      isRepaintModalOpen,
      setIsRepaintModalOpen,
    }),
    [tourRef1, tourRef2, tourRef3, tableLoading, isRepaintModalOpen]
  );
  return (
    <TableViewContexts.Provider value={value as ITableViewContexts}>
      <TableContainer projectId={projectId} />

      <Tour
        open={isTourOpen}
        onClose={() => setIsTourOpen(false)}
        steps={steps}
      />
    </TableViewContexts.Provider>
  );
};

export default TableView;
