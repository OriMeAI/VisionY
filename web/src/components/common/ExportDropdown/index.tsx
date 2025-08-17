/**
 * 导出按钮组件
 */
import { App, Button, Dropdown, MenuProps, Progress } from "antd";
import * as React from "react";
import { createPortal } from "react-dom";
import { useTranslation } from "react-i18next";
import ModalBase from "../../client/Common/ModalBase";
import ShareProjectModal from "../../Workspace/ShareProjectModal";
import downloadIcon from "./../../../../assets/images/pages/export/download_icon.svg";
import excelIcon from "./../../../../assets/images/pages/export/excel_icon.svg";
import exportIcon from "./../../../../assets/images/pages/export/export_icon.svg";
import exportIconDisabled from "./../../../../assets/images/pages/export/export_icon_disabled.svg";
import videoPlayIcon from "./../../../../assets/images/pages/export/export_video_play_icon.svg";
import linkIcon from "./../../../../assets/images/pages/export/link_icon.svg";
import exportApi from "./../../../api/exportApi";
interface IProps {
  projectId: string; // 项目id
  btnDisabled?: boolean;
}

const ExportDropdown: React.FC<IProps> = ({ projectId, btnDisabled }) => {
  const { t } = useTranslation();
  const { message: messageApi } = App.useApp();
  const [isExportVideoModalOpen, setIsExportVideoModalOpen] =
    React.useState<boolean>(false);
  const [isExportImgModalOpen, setIsExportImgModalOpen] =
    React.useState<boolean>(false);
  const [isExportExcelModalOpen, setIsExportExcelModalOpen] =
    React.useState<boolean>(false);
  const [isExportPdfModalOpen, setIsExportPdfModalOpen] =
    React.useState<boolean>(false);
  const [isExporting, setIsExporting] = React.useState<boolean>(false);
  const [isExportImgLoading, setIsExportImgLoading] =
    React.useState<boolean>(false);
  const [isExportExcelLoading, setIsExportExcelLoading] =
    React.useState<boolean>(false);
  const [isExportPdfLoading, setIsExportPdfLoading] =
    React.useState<boolean>(false);
  const [percent, setPercent] = React.useState<number>(0);
  const interval = React.useRef<NodeJS.Timeout | null>(null);
  const [isShareProjectModalOpen, setIsShareProjectModalOpen] =
    React.useState<boolean>(false);

  const [isExportContent, setIsExportContent] = React.useState<boolean>(false);

  const showExportVideoModal = () => {
    setIsExportVideoModalOpen(true);
  };
  const handleExportVideoModalCancel = async () => {
    setIsExportVideoModalOpen(false);
  };

  const showExportImgModal = () => {
    setIsExportImgModalOpen(true);
  };
  const handleExportImgModalCancel = async () => {
    setIsExportImgModalOpen(false);
  };

  const showExportExcelModal = () => {
    setIsExportExcelModalOpen(true);
  };
  const handleExportExcelModalCancel = async () => {
    setIsExportExcelModalOpen(false);
  };
  const showExportPdfModal = () => {
    setIsExportPdfModalOpen(true);
  };
  const handleExportPdfModalCancel = async () => {
    setIsExportPdfModalOpen(false);
  };
  const calculatePercent = () => {
    // 计算每次增加的百分比
    const duration = 5 * 60 * 1000; // 5分钟
    const intervalTime = 100; // 每100毫秒更新一次
    const increment = 99 / (duration / intervalTime);

    interval.current = setInterval(() => {
      setPercent((prevPercent) => {
        if (prevPercent >= 99) {
          return 99;
        }
        return prevPercent + increment;
      });
    }, intervalTime);
  };

  const exportImg = async () => {
    setIsExportImgLoading(true);
    handleExportImgModalCancel();
    const res = await exportApi.exportImg({
      projectId: projectId,
    });
    setIsExportImgLoading(false);
  };
  const exportExcel = async () => {
    setIsExportContent(true);
    const res = await exportApi.exportExcel({
      projectId: projectId,
    });
    setIsExportContent(false);
    if (res.success) {
      messageApi.success(t("export_success"));
    } else {
      messageApi.error(t("export_fail"));
    }
  };
  const exportPdf = async () => {
    setIsExportContent(true);
    const res = await exportApi.exportPdf({
      projectId: projectId,
    });
    // setIsExportContent(false);
  };
  const exportVideo = async (exportAllTracks?: boolean) => {
    setIsExporting(true);
    handleExportVideoModalCancel();
    calculatePercent();
    let params: { projectId: string; exportAllTracks?: boolean } = {
      projectId: projectId,
    };
    if (exportAllTracks) {
      params = {
        ...params,
        exportAllTracks: exportAllTracks,
      };
    }
    const res = await exportApi.exportVideo(params);
    if (res.success && res.result?.code === 0) {
      if (isExporting) {
        // TODO
        // 导出视频
        setPercent(100);
        clearInterval(interval.current);
        setIsExporting(false);
        setPercent(0);
      }
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
        clearInterval(interval.current);
        setIsExporting(false);
        setPercent(0);
      }
    }
  };
  const items: MenuProps["items"] = [
    // {
    //   icon: <img src={videoIcon} />,
    //   label: t("export_dubbed_video"),
    //   key: "0",
    //   onClick: () => {
    //     showExportVideoModal();
    //   },
    // },
    // {
    //   icon: <img src={imageIcon} />,
    //   label: t("export_all_images"),
    //   key: "1",
    //   onClick: () => {
    //     showExportImgModal();
    //   },
    // },
    // {
    //   icon: <img src={downloadIcon} />,
    //   label: t("export_pdf_file"),
    //   key: "2",
    //   onClick: () => {
    //     showExportPdfModal();
    //     exportPdf();
    //   },
    // },
    // {
    //   type: "divider",
    // },
    {
      icon: <img src={excelIcon} />,
      label: t("export_excel_file"),
      key: "3",
      onClick: () => {
        // showExportExcelModal();
        exportExcel();
      },
    },
    {
      type: "divider",
    },
    {
      icon: <img src={linkIcon} />,
      label: t("share_project_link"),
      key: "4",
      onClick: () => {
        setIsShareProjectModalOpen(true);
      },
    },
  ];
  return (
    <>
      <Dropdown menu={{ items }} trigger={["click"]} className="mr-3">
        <Button
          type="primary"
          variant="solid"
          size="middle"
          loading={isExportContent}
          disabled={btnDisabled}
          icon={
            !isExportContent && (
              <img
                className="w-4 h-4"
                src={btnDisabled ? exportIconDisabled : exportIcon}
              />
            )
          }
        >
          <span>{isExportContent ? t("exporting") : t("export")}</span>
        </Button>
        {/* <Button type="primary" variant="solid" size="middle">
          <span className="ant-btn-icon">
            <div className="w-4 h-4">
              {isExportContent? (<LoadingOutlined color="#ffffff" />) : (<img src={exportIcon} />)}
            </div>
          </span>
          <span>{isExportContent? t("export") : t("export") }</span>
        </Button> */}
      </Dropdown>
      {createPortal(
        <ModalBase
          open={isExportVideoModalOpen}
          onCancel={handleExportVideoModalCancel}
          width={520}
          height={undefined}
          showFooter={false}
          footer={null}
        >
          <div
            className="w-auto grid gap-4"
            style={{ padding: "24px 24px 0 24px" }}
          >
            <div className="space-y-1.5">
              <div className="text-lg font-semibold">
                {t("export_dubbed_video")}
              </div>
            </div>
            <div className="text-center my-8 w-full space-x-4 flex items-center justify-center">
              <Button
                type="primary"
                variant="solid"
                size="large"
                onClick={() => {
                  exportVideo();
                }}
              >
                <span>
                  <img
                    className="w-5 h-5 brightness-0 invert"
                    src={downloadIcon}
                  />
                </span>
                <span>{t("export_video")}</span>
              </Button>
              <Button
                type="primary"
                variant="solid"
                size="large"
                onClick={() => {
                  exportVideo(true);
                }}
              >
                <span>
                  <img
                    className="w-5 h-5 brightness-0 invert"
                    src={downloadIcon}
                  />
                </span>
                <span>{t("export_tracks")}</span>
              </Button>
            </div>
          </div>
        </ModalBase>,
        document.body
      )}
      {createPortal(
        <ModalBase
          open={isExportImgModalOpen}
          onCancel={handleExportImgModalCancel}
          width={520}
          height={undefined}
          showFooter={false}
          footer={null}
        >
          <div
            className="w-auto grid gap-4"
            style={{ padding: "24px 24px 0 24px" }}
          >
            <div className="space-y-1.5">
              <div className="text-lg font-semibold">
                {t("export_all_images")}
              </div>
            </div>
            <div className="text-center my-8 w-full">
              <Button
                onClick={exportImg}
                loading={isExportImgLoading}
                type="primary"
                variant="solid"
                size="large"
              >
                <span>
                  <img
                    className="w-5 h-5 brightness-0 invert"
                    src={downloadIcon}
                  />
                </span>
                <span>{t("export_all_images")}</span>
              </Button>
            </div>
          </div>
        </ModalBase>,
        document.body
      )}
      {createPortal(
        <ModalBase
          open={isExportPdfModalOpen}
          onCancel={handleExportPdfModalCancel}
          width={520}
          height={undefined}
          showFooter={false}
          footer={null}
        >
          <div
            className="w-auto grid gap-4"
            style={{ padding: "24px 24px 0 24px" }}
          >
            <div className="space-y-1.5">
              <div className="text-lg font-semibold">
                {t("export_pdf_file")}
              </div>
            </div>
            <div className="text-center my-8 w-full">
              <Button
                onClick={exportPdf}
                loading={isExportPdfLoading}
                type="primary"
                variant="solid"
                size="large"
              >
                <span>
                  <img
                    className="w-5 h-5 brightness-0 invert"
                    src={downloadIcon}
                  />
                </span>
                <span>{t("export_pdf_file")}</span>
              </Button>
            </div>
          </div>
        </ModalBase>,
        document.body
      )}
      {createPortal(
        <ModalBase
          open={isExportExcelModalOpen}
          onCancel={handleExportExcelModalCancel}
          width={520}
          height={undefined}
          showFooter={false}
          footer={null}
        >
          <div
            className="w-auto grid gap-4"
            style={{ padding: "24px 24px 0 24px" }}
          >
            <div className="space-y-1.5">
              <div className="text-lg font-semibold">
                {t("export_excel_file")}
              </div>
            </div>
            <div className="text-center my-8 w-full">
              <Button
                onClick={exportExcel}
                loading={isExportExcelLoading}
                type="primary"
                variant="solid"
                size="large"
              >
                <span>
                  <img
                    className="w-5 h-5 brightness-0 invert"
                    src={downloadIcon}
                  />
                </span>
                <span>{t("export_excel_file")}</span>
              </Button>
            </div>
          </div>
        </ModalBase>,
        document.body
      )}
      {isExporting ? (
        <div
          style={{ top: 300 }}
          className="absolute left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-10"
        >
          <div className="animate-enter max-w-md w-full bg-white shadow-lg rounded-lg pointer-events-auto flex-col ring-1 ring-black ring-opacity-5">
            <div className="flex-1 p-4">
              <div className="flex items-start">
                <div className="border p-2 rounded-lg">
                  <img src={videoPlayIcon} />
                </div>
                <div className="ml-4 flex-1">
                  <p className="text-sm font-medium text-gray-900">
                    {t("exporting_video_tracks")}
                  </p>
                  <p className="mt-1 text-sm text-gray-500">
                    {t("generating_video_tracks")}
                  </p>
                  <Progress
                    showInfo={false}
                    percent={percent}
                    className="h-2 mt-4"
                  />
                  <div className="mt-4">
                    <span
                      className="text-sm text-primary cursor-pointer"
                      onClick={() => {
                        setIsExporting(false);
                        setPercent(0);
                      }}
                    >
                      {t("stop_export")}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      ) : null}
      <ShareProjectModal
        projectId={projectId}
        isModalOpen={isShareProjectModalOpen}
        setIsModalOpen={setIsShareProjectModalOpen}
      />
    </>
  );
};

export default ExportDropdown;
