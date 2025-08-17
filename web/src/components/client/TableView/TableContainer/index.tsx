/**
 * 分镜表页面
 */
import type { DragEndEvent } from "@dnd-kit/core";
import { DndContext } from "@dnd-kit/core";
import type { SyntheticListenerMap } from "@dnd-kit/core/dist/hooks/utilities";
import { restrictToVerticalAxis } from "@dnd-kit/modifiers";
import {
  arrayMove,
  SortableContext,
  useSortable,
  verticalListSortingStrategy,
} from "@dnd-kit/sortable";
import { CSS } from "@dnd-kit/utilities";
import type { TableColumnsType } from "antd";
import { Button, Flex, App, Popconfirm, Spin, Table,Tooltip } from "antd";
import projectApi from "./../../../../api/projectApi";
import { StoryHeadIdType } from "./../../../../libs/enums";
import {
  StoryboardCopyPayload,
  StoryboardDeletePayload,
  StoryboardSortPayload,
} from "./../../../../libs/interfaces";
import { ShotResource, StoryboardShot } from "./../../../../types/storyboard";

import { MinusOutlined, PlusOutlined } from "@ant-design/icons";
import React, { useContext, useEffect, useMemo, useRef } from "react";
import { createPortal } from "react-dom";
import CellInputNumber from "../../Common/CellInputNumber";
import CellMainFigure from "../../Common/CellMainFigure";
import CellSelect from "../../Common/CellSelect";
import {
  DetailContexts,
  IDetailContexts,
} from "../../Common/DetailContainer/contexts/detail-contexts";
import ModalBase from "../../Common/ModalBase";
import StoryboardDialogues from "../../Common/StoryboardDialogues";
import StoryboardFigureImg from "../../Common/StoryboardFigureImg";
import StoryboardPictureDesc from "../../Common/StoryboardPictureDesc";
import {
  ITableViewContexts,
  TableViewContexts,
} from "../contexts/table-view-contexts";
import sortIcon from "./../../../../../assets/images/pages/boardView/sort_icon.svg";
import {
  aierhubFetchEventSourceWithAuth
} from "./../../../../api/aierhubFetch";
import dashboardApi from "./../../../../api/dashboardApi";
import drawHelper from "./../../../../libs/draw-helper";
import style from "./style.module.css";

import { useTranslation } from "react-i18next";
import loadingIcon from "./../../../../../assets/images/layout/loading_icon.svg";
import tourHelper from "./../../../../libs/tour-helper";
import { useLocation } from "react-router-dom";

import userApi from "./../../../../api/userApi";
import { IUserContexts, UserContexts } from "./../../../../contexts/user-contexts";

interface RowContextProps {
  setActivatorNodeRef?: (element: HTMLElement | null) => void;
  listeners?: SyntheticListenerMap;
}

const RowContext = React.createContext<RowContextProps>({});

const DragHandle: React.FC = () => {
  const { setActivatorNodeRef, listeners } = useContext(RowContext);
  return (
    <Button
      type="default"
      size="small"
      icon={<img src={sortIcon} />}
      style={{ cursor: "move" }}
      ref={setActivatorNodeRef}
      {...listeners}
    />
  );
};

interface RowProps extends React.HTMLAttributes<HTMLTableRowElement> {
  "data-row-key": string;
}

const Row: React.FC<RowProps> = (props) => {
  const {
    attributes,
    listeners,
    setNodeRef,
    setActivatorNodeRef,
    transform,
    transition,
    isDragging,
  } = useSortable({ id: props["data-row-key"] });

  const style: React.CSSProperties = {
    ...props.style,
    transform: CSS.Translate.toString(transform),
    transition,
    height: "224px",
    maxHeight: "224px",
    ...(isDragging ? { position: "relative", zIndex: 9999 } : {}),
  };

  const contextValue = useMemo<RowContextProps>(
    () => ({ setActivatorNodeRef, listeners }),
    [setActivatorNodeRef, listeners]
  );

  return (
    <RowContext.Provider value={contextValue}>
      <tr {...props} ref={setNodeRef} style={style} {...attributes} />
    </RowContext.Provider>
  );
};

interface IProps {
  projectId: string;
}

const TableContainer: React.FC<IProps> = ({ projectId }: IProps) => {
  const { t } = useTranslation();
  let tableData: StoryboardShot[] = [];
  const detailContexts: IDetailContexts =
    useContext<IDetailContexts>(DetailContexts);
  const tableViewContexts: ITableViewContexts =
    useContext<ITableViewContexts>(TableViewContexts);
  const [subscribeLoading, setSubscribeLoading] =
    React.useState<boolean>(false);
  // 将中文文本替换为使用 t 函数
  const [subscribeLoadingText, setSubscribeLoadingText] = React.useState<string>(t("storyboard_generating"));

  const [storyboardTableData, setStoryboardTableData] = React.useState< StoryboardShot[] >([]);

  // 添加 AbortController 引用
  const abortControllerRef = useRef<AbortController | null>(null);

  const location = useLocation();
  const isTableViewNew = !location.pathname.includes('tableviewold');

  const userContexts: IUserContexts =React.useContext<IUserContexts>(UserContexts);

  const { message: messageApi } = App.useApp();

  // 添加清理函数
  useEffect(() => {
    return () => {
      if (abortControllerRef.current) {
        abortControllerRef.current.abort();
        abortControllerRef.current = null;
      }
    };
  }, []);

  const onAdd = async (obj: StoryboardShot) => {
    const storyboardCopyPayload: StoryboardCopyPayload = {
      projectId: projectId,
      storyboardId: obj.shot_id,
    };
    const res = await dashboardApi.storyboardCopy(storyboardCopyPayload);
    if (res.success && res.result?.code === 0) {
      setStoryboardTableData((prevState) => {
        const index = prevState.findIndex(
          (item) => item.shot_id === obj.shot_id
        );
        if (index === -1) return prevState;

        // 修改这里：将新数据插入到 index 之前
        return [
          ...prevState.slice(0, index), // 获取 index 之前的所有元素
          res.result.data, // 插入新元素
          ...prevState.slice(index), // 获取从 index 开始的所有元素（包括原 index 位置的元素）
        ];
      });
      messageApi.success(res.result?.msg);
    } else {
      messageApi.error(res.result?.msg);
    }
  };

  const onDelete = async (key: string) => {
    //需要等待服务器处理完毕，本地再做修改
    const storyboardDeletePayload: StoryboardDeletePayload = {
      projectId: projectId,
      storyboardId: key,
    };
    const res = await dashboardApi.storyboardDelete(storyboardDeletePayload);
    if (res.success && res.result?.code === 0) {
      setStoryboardTableData((prevState) => {
        return prevState.filter((item) => item.shot_id !== key);
      });
      messageApi.success(res.result?.msg);
    } else {
      messageApi.error(res.result?.msg);
    }
  };

  const onDragEnd = async ({ active, over }: DragEndEvent) => {
    // console.log("active", active, typeof active.id, typeof over?.id);
    // console.log("over", over);
    if (active.id !== over?.id) {
      // 从ID中提取shot_id（处理可能包含时间戳的情况）
      const extractShotId = (id: string | number) => {
        const idStr = id.toString();
        // 如果ID包含下划线，说明是 ${shot_id}_${timestamp} 格式
        return idStr.includes("_") ? idStr.split("_")[0] : idStr;
      };

      const currentShotId = extractShotId(active.id);
      const targetShotId = extractShotId(over?.id);

      // 直接在这里实现排序逻辑，不再调用单独的函数
      const storyboardSortPayload: StoryboardSortPayload = {
        projectId: projectId,
        currentId: currentShotId,
        targetId: targetShotId,
      };
      const res = await dashboardApi.storyboardSort(storyboardSortPayload);
      if (res.success && res.result?.code === 0) {
        //服务器处理完毕数据，本地再做修改
        setStoryboardTableData((prevState) => {
          const activeIndex = prevState.findIndex(
            (record) => record.shot_id === currentShotId
          );
          const overIndex = prevState.findIndex(
            (record) => record.shot_id === targetShotId
          );
          return arrayMove(prevState, activeIndex, overIndex);
        });
      } else {
        messageApi.error(res.result?.msg);
      }
    }
  };

  // 将 handleBoardItemChange 定义为单独的函数
  const handleBoardItemChange = (updatedBoardItem: StoryboardShot) => {
    console.log("updatedBoardItem", updatedBoardItem);

    // 使用函数式更新确保我们总是基于最新的状态进行更新
    setStoryboardTableData((prevState) => {
      // 创建一个全新的数组，避免引用问题
      const newState = [...prevState]; // 先创建整个数组的副本

      // 找到需要更新的项目索引
      const index = newState.findIndex(
        (item) => item.shot_id === updatedBoardItem.shot_id
      );
      if (index !== -1) {
        // 创建该项的深拷贝并添加一个额外的属性来强制更新
        const newItem = {
          ...updatedBoardItem,
          _updateTimestamp: Date.now(), // 添加一个时间戳属性强制更新
        };
        newState[index] = newItem; // 替换该项
      }

      console.log("新的状态数据", newState);
      return newState;
    });
  };

  const columns: TableColumnsType = [
    {
      key: "edit",
      align: "center",
      width: 50,
      fixed: "left",
      render: (obj, record, index) => {
        return (
          <Flex
            vertical
            justify="center"
            align="center"
            ref={index === 0 ? tableViewContexts.tourRef1 : null}
          >
            <Button
              type="text"
              style={{ color: "#7E2FFF" }}
              size="small"
              icon={<PlusOutlined style={{ fontSize: 10 }} />}
              className="mb-8"
              onClick={() => onAdd(obj)}
            />
            <DragHandle />
            <Popconfirm
              placement="rightTop"
              title={t("storyboard_delete_title")}
              description={t("storyboard_delete_confirm")}
              trigger="click"
              okText={t("common_confirm")}
              cancelText={t("common_cancel")}
              onConfirm={() => onDelete(obj.shot_id)}
            >
              <Button
                style={{ color: "red" }}
                type="text"
                size="small"
                icon={<MinusOutlined style={{ fontSize: 10 }} />}
                className="mt-8"
              />
            </Popconfirm>
          </Flex>
        );
      },
    },
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
        <div className="text-center">{index + 1}</div>
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
      fixed: true,
      align: "center",
      render: (text: ShotResource, record: StoryboardShot, index: number) => (
        <div
          className="flex items-center justify-center"
          ref={index === 0 ? tableViewContexts.tourRef2 : null}
        >
          <StoryboardFigureImg boardItem={record} />
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
      render: (text, record: StoryboardShot, index: number) => (
        <div
          className="flex items-center justify-center"
          ref={index === 0 ? tableViewContexts.tourRef3 : null}
        >
          <StoryboardPictureDesc boardItem={record} />
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
          <StoryboardDialogues boardItem={record} />
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
          <CellMainFigure
            boardItem={record}
            handleBoardItemChange={handleBoardItemChange}
          />
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
      render: (text, record: StoryboardShot) => {
        const cellValue = record.shot_size.value;
        return (
          <div className="flex items-center justify-center">
            <CellSelect
              cellValue={cellValue}
              dataObj={record.shot_size}
              valueKey="shot_size"
              storyboardId={record.shot_id}
              options={record.shot_size.size_values}
              selectWidth={100}
            />
          </div>
        );
      },
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
      width: 100,
      align: "center",
      render: (text, record: StoryboardShot) => {
        const cellValue = record.camera_angle.value;
        return (
          <div className="flex items-center justify-center">
            <CellSelect
              cellValue={cellValue}
              dataObj={record.camera_angle}
              valueKey="camera_angle"
              storyboardId={record.shot_id}
              options={record.camera_angle.angle_values}
              selectWidth={100}
            />
          </div>
        );
      },
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
      width: 100,
      align: "center",
      render: (text, record: StoryboardShot) => {
        const cellValue = record.shot_type.value;
        return (
          <div className="flex items-center justify-center">
            <CellSelect
              cellValue={cellValue}
              dataObj={record.shot_type}
              valueKey="shot_type"
              storyboardId={record.shot_id}
              options={record.shot_type.type_values}
              selectWidth={100}
            />
          </div>
        );
      },
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
          <CellInputNumber
            cellValue={record.shot_time.value}
            dataObj={record.shot_time}
            valueKey="shot_time"
            storyboardId={record.shot_id}
            inputWidth={78}
          />
        </div>
      ),
    },
  ];

  useEffect(() => {
    (async () => {

      if (userContexts.isAuthenticated) {
        const data = await userApi.getUserInfo();
        if (!data.success) return;
        userContexts.setUserInfo(data.result.data);
        if(data.result?.data?.credits < 1){
          messageApi.error(t("common_error_noCredits"));
          // return;
        }
      }else{
        messageApi.error(t("common_error_noLogin"));
        return;
      }

      if (!detailContexts.projectItemObj) {
        return;
      }

      // 如果有正在进行的请求，先取消
      if (abortControllerRef.current) {
        abortControllerRef.current.abort();
        abortControllerRef.current = null;
      }

      if (detailContexts.projectItemObj.hasShot) {
        const data = await projectApi.getStoryboardListById(projectId);
        setStoryboardTableData(data.result.data);
        tableViewContexts.setTableLoading(false);
      } else {
        setSubscribeLoading(true);
        // 创建新的 AbortController
        abortControllerRef.current = new AbortController();
        const signal = abortControllerRef.current.signal;

        try {
          // 使用封装的函数替代原来的fetchEventSource，并添加signal参数
          await aierhubFetchEventSourceWithAuth(
            `/api/storyboard/create/shot?projectId=${projectId}`,
            {
              method: "GET",
              signal, // 添加 signal 参数
              onmessage(ev) {
                switch (ev.event) {
                  case "message":
                    // 处理连接成功消息
                    if (ev.data === "Connection successful") {
                      console.log("SSE Connection successful");
                      return;
                    }else if (ev.data === "Complete") {
                      (async () => {
                        setSubscribeLoading(false);
                        tableViewContexts.setTableLoading(true);
                        //TODO: 更新项目信息
    
                        const projectInfoData = await projectApi.getProjectById(
                          projectId
                        );
                        if (
                          projectInfoData.success &&
                          projectInfoData.result?.code === 0
                        ) {
                          detailContexts.setProjectItemObj(
                            projectInfoData.result.data
                          );
                        }
                        const data = await projectApi.getStoryboardListById(
                          projectId
                        );
                        tableViewContexts.setTableLoading(false);
                        setStoryboardTableData(data.result.data);
                        const tableTourShown = tourHelper.getLocalTableTourShown();
                        if (!tableTourShown) {
                          tableViewContexts.setIsTourOpen(true);
                          tourHelper.setLocalTableTourShown("false");
                        }
                      })();
                      messageApi.success(t("storyboard_created_successfully"));
                      return;
                    }else{
                      const data = JSON.parse(ev.data);
                      setStoryboardTableData((prev) => {
                        tableData = prev ? [...prev, data] : [data];
                        console.log(
                          "setStoryboardTableData-prev",
                          prev,
                          data,
                          storyboardTableData
                        );
                        return tableData;
                      });
                    }
                  break;
                case "progress":
                  setSubscribeLoadingText(ev.data);
                  break;
                case "warning":
                  messageApi.warning(ev.data);
                  break;
                case "error":
                  messageApi.error(ev.data);
                  //TODO need more friendly function to handle error by soongxl
                  break;
                default:
                  break;
                }
              },
              onerror(err) {
                console.error("SSE Error:", err);
                throw err;
              },
              onclose: () => {
                // 确保在连接关闭时清理资源
                abortControllerRef.current = null;
              },
            }
          );
        } catch (error) {
          console.error("分镜表生成出错:", error);
          setSubscribeLoading(false);
          if (error instanceof Error && error.name !== "AbortError") {
            console.log(error.message);
            messageApi.error(t("common_error_dataReceive"));
          }
        } finally {
          if (abortControllerRef.current) {
            abortControllerRef.current.abort();
          }
          // 请求完成后清除 AbortController 引用
          abortControllerRef.current = null;
        }
      }
    })();

    // 组件卸载或依赖变化时清理
    return () => {
      if (abortControllerRef.current) {
        abortControllerRef.current.abort();
        abortControllerRef.current = null;
      }
    };
  }, [detailContexts.projectItemObj]);

  return (
    <div
      className={`relative ${style.tableContanerWrapper}`}
      // style={{ height: drawHelper.getWinH() - 72 }}
    >
      <Spin
        spinning={tableViewContexts.tableLoading}
        style={{
          position: "fixed",
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          zIndex: 1000,
        }}
      >
        {Array.isArray(storyboardTableData) &&
        storyboardTableData.length > 0 ? (
          <>
            <DndContext
              modifiers={[restrictToVerticalAxis]}
              onDragEnd={onDragEnd}
            >
              <SortableContext
                items={storyboardTableData.map((i) => {
                  // 使用类型断言来避免 TypeScript 错误
                  const item = i as StoryboardShot & {
                    _updateTimestamp?: number;
                  };
                  return item._updateTimestamp
                    ? `${i.shot_id}_${item._updateTimestamp}`
                    : i.shot_id;
                })}
                strategy={verticalListSortingStrategy}
              >
                <Table
                  rowKey={(record) => {
                    // 使用 shot_id 和可能存在的 _updateTimestamp 组合作为 key
                    return record._updateTimestamp
                      ? `${record.shot_id}_${record._updateTimestamp}`
                      : record.shot_id;
                  }}
                  components={{ body: { row: Row } }}
                  columns={columns}
                  dataSource={storyboardTableData}
                  pagination={false}
                  scroll={{ 
                    x: "max-content", 
                    y: isTableViewNew ? "calc(100vh - 200px)" : "calc(100vh - 128px)" 
                  }}
                  rowClassName={() => "fixed-height-row"}
                  onRow={() => ({
                    style: {
                      height: "224px",
                      maxHeight: "224px",
                      lineHeight: "normal",
                    },
                  })}
                />
              </SortableContext>
            </DndContext>
          </>
        ) : null}
      </Spin>

      {createPortal(
        <ModalBase
          // wrapperClassName={style.loadingModal}
          open={subscribeLoading}
          width={380}
          height={undefined}
          showFooter={false}
          footer={null}
          closable={false}
        >
          <div className="animate-enter max-w-md w-full bg-white shadow-2xl rounded-lg pointer-events-auto flex-col ring-1 ring-black ring-opacity-5">
            <div className="flex-1 p-4">
              <div className="flex items-start">
                <div className="border p-2 rounded-lg">
                  <img
                    className="animate-spin"
                    src={loadingIcon}
                    alt="loading"
                  />
                </div>
                <div className="ml-4 flex-1">
                  <p className="text-sm font-medium text-gray-900">
                    {subscribeLoadingText} <span className={style.dotsAnimation}></span>
                  </p>
                  <p className="mt-1 text-sm text-gray-500">
                    {t("storyboard_table_loading_message")}
                    <br />
                    {t("storyboard_table_loading_warning")}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </ModalBase>,
        document.body
      )}
    </div>
  );
};

export default TableContainer;
