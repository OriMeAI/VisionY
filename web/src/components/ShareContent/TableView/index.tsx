/**
 * 分镜表页面(预览不可编辑)
 */

import type { TableColumnsType } from "antd";
import { Flex, Spin, Table,Tooltip } from "antd";
import { StoryHeadIdType } from "./../../../libs/enums";
import { StoryboardShot } from "./../../../types/storyboard";
import { useTranslation } from "react-i18next"; // 添加 useTranslation 导入

import React from "react";
import drawHelper from "./../../../libs/draw-helper";
import CellMainFigure from "./../../client/Common/CellMainFigure";
import StoryboardFigureImg from "./../../client/Common/StoryboardFigureImg";
import StoryboardPictureDesc from "./../../client/Common/StoryboardPictureDesc";
import StoryboardDialogues from "./../../client/Common/StoryboardDialogues";
import style from "./style.module.css";

interface IProps {
  tableData: StoryboardShot[];
  isNew?: boolean;
}

const TableView: React.FC<IProps> = ({ tableData, isNew }: IProps) => {
  const { t } = useTranslation(); // 使用 useTranslation hook
  const [tableLoading, setTableLoading] = React.useState<boolean>(true);

  const columns: TableColumnsType = [
    {
      title: (
        <Tooltip placement="top" title={t("storyboard_shot_number")}>
          <div className={`text-center w-full ${style.tableHeaderClickable}`}>
            {t("storyboard_shot_number")}
          </div>
        </Tooltip>
      ),
      key: StoryHeadIdType.BoardNumber.toString(),
      width: 70,
      fixed: "left",
      align: "center",
      render: (text, record: StoryboardShot, index) => (
        <div className="flex items-center justify-center">
          <div className="text-center">{index + 1}</div>
        </div>
      ),
    },
    {
      title: (
        <Tooltip placement="top" title={t("storyboard_picture")}>
          <div className={`text-center w-full ${style.tableHeaderClickable}`}>
            {t("storyboard_picture")}
          </div>
        </Tooltip>
      ),
      dataIndex: StoryHeadIdType.Picture.toString(),
      key: StoryHeadIdType.Picture.toString(),
      width: 300,
      fixed: "left",
      align: "center",
      render: (text: any, record: StoryboardShot, index: number) => (
        <div className="flex items-center justify-center">
          <StoryboardFigureImg
            boardItem={record}
            isEdit={false}
          />
        </div>
      ),
    },
    {
      title: (
        <Tooltip placement="top" title={t("scene_description")}>
          <div className={`text-center w-full ${style.tableHeaderClickable}`}>
            {t("scene_description")}
          </div>
        </Tooltip>
      ),
      dataIndex: StoryHeadIdType.PictureDesc.toString(),
      key: StoryHeadIdType.PictureDesc.toString(),
      width: 260,
      align: "center",
      render: (text, record: StoryboardShot) => (
        <div className="flex items-center justify-center">
          <StoryboardPictureDesc boardItem={record} isEdit={false} />
        </div>
      ),
    },
    {
      title: (
        <Tooltip placement="top" title={t("storyboard_dialogues")}>
          <div className={`text-center w-full ${style.tableHeaderClickable}`}>
            {t("storyboard_dialogues")}
          </div>
        </Tooltip>
      ),
      dataIndex: StoryHeadIdType.Lines.toString(),
      key: StoryHeadIdType.Lines.toString(),
      width: 260,
      align: "center",
      render: (text, record: StoryboardShot) => (
        <div className="flex items-center justify-center">
          <StoryboardDialogues boardItem={record} isEdit={false}/>
        </div>
      ),
    },
    {
      title: (
        <Tooltip placement="top" title={t("storyboard_main_figure")}>
          <div className={`text-center w-full ${style.tableHeaderClickable}`}>
            {t("storyboard_main_figure")}
          </div>
        </Tooltip>
      ),
      dataIndex: StoryHeadIdType.MainFigure.toString(),
      key: StoryHeadIdType.MainFigure.toString(),
      width: 140,
      align: "center",
      render: (text, record: StoryboardShot) => (
        <div className="flex items-center justify-center">
          <CellMainFigure boardItem={record} isEdit={false} />
        </div>
      ),
    },
    {
      title: (
        <Tooltip placement="top" title={t("storyboard_shot_size")}>
          <div className={`text-center w-full ${style.tableHeaderClickable}`}>
            {t("storyboard_shot_size")}
          </div>
        </Tooltip>
      ),
      dataIndex: StoryHeadIdType.Scene.toString(),
      key: StoryHeadIdType.Scene.toString(),
      width: 100,
      align: "center",
      render: (text, record: StoryboardShot) => (
        <div className="flex items-center justify-center">
          <div className="cursor-default" style={{ width: 80 }}>
            {record.shot_size.value}
          </div>
        </div>
      ),
    },
    {
      title: (
        <Tooltip placement="top" title={t("storyboard_camera_angle")}>
          <div className={`text-center w-full ${style.tableHeaderClickable}`}>
            {t("storyboard_camera_angle")}
          </div>
        </Tooltip>
      ),
      dataIndex: StoryHeadIdType.CameraAngle.toString(),
      key: StoryHeadIdType.CameraAngle.toString(),
      width: 120,
      align: "center",
      render: (text, record: StoryboardShot) => (
        <div className="flex items-center justify-center">
          <div className="cursor-default" style={{ width: 100 }}>
            {record.camera_angle.value}
          </div>
        </div>
      ),
    },
    {
      title: (
        <Tooltip placement="top" title={t("storyboard_shot_type")}>
          <div className={`text-center w-full ${style.tableHeaderClickable}`}>
            {t("storyboard_shot_type")}
          </div>
        </Tooltip>
      ),
      dataIndex: StoryHeadIdType.ShotType.toString(),
      key: StoryHeadIdType.ShotType.toString(),
      width: 140,
      align: "center",
      render: (text, record: StoryboardShot) => (
        <div className="flex items-center justify-center">
          <div className="cursor-default" style={{ width: 120 }}>
            {record.shot_type.value}
          </div>
        </div>
      ),
    },
    {
      title: (
        <Tooltip placement="top" title={t("storyboard_duration")}>
          <div className={`text-center w-full ${style.tableHeaderClickable}`}>
            {t("storyboard_duration")}
          </div>
        </Tooltip>
      ),
      dataIndex: StoryHeadIdType.Duration.toString(),
      key: StoryHeadIdType.Duration.toString(),
      width: 100,
      align: "center",
      render: (text, record: StoryboardShot) => (
        <div className="flex items-center justify-center">
          <div className="cursor-default" style={{ width: 67 }}>
            {record.shot_time.value}
          </div>
        </div>
      ),
    },
  ];

  React.useEffect(() => {
    setTableLoading(false);
  }, []);

  return (
    <div
      className={`relative ${isNew ? "mt-[0px]" : "mt-[72px]"} ${style.shareTableViewWrapper}`}
      style={{ height: isNew ? drawHelper.getWinH() - 144 : drawHelper.getWinH() - 72 }}
    >
      {!tableLoading && Array.isArray(tableData) && tableData.length > 0 ? (
        <Table
          rowKey="shot_id"
          columns={columns}
          dataSource={tableData}
          pagination={false}
          scroll={{ x: "max-content", y: isNew ? "calc(100vh - 200px)" : "calc(100vh - 126px)" }}
          rowClassName={() => "fixed-height-row"}
          onRow={() => ({
            style: {
              height: "224px",
              maxHeight: "224px",
              lineHeight: "normal",
            },
          })}
        />
      ) : (
        <Flex
          justify="center"
          align="center"
          style={{
            height: drawHelper.getWinH() - 72,
            width: "100%",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <Spin />
        </Flex>
      )}
    </div>
  );
};

export default TableView;
