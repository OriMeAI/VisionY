/**
 * 项目列表项组件
 */
import { DeleteOutlined, ExclamationCircleFilled } from "@ant-design/icons";
import { App, Button, Dropdown, MenuProps, Modal, Tag } from "antd";
import React from "react";
import { useTranslation } from "react-i18next";
import RenameProjectModal from "../RenameProjectModal";
import ShareProjectModal from "../ShareProjectModal";
import copyIcon from "./../../../../assets/images/icons/board_copy_icon.svg";
import extendIcon from "./../../../../assets/images/icons/extend_icon.svg";
import renameIcon from "./../../../../assets/images/icons/rename_icon.svg";
import shareIcon from "./../../../../assets/images/icons/share_icon.svg";
import dashboardApi from "./../../../api/dashboardApi";
import { ProjectItemObj } from "./../../../libs/interfaces";
import style from "./style.module.css";

// const { confirm } = Modal;

interface IProps {
  projectItem: ProjectItemObj;
  projectList: ProjectItemObj[];
  setProjectList: (projectList: ProjectItemObj[]) => void;
  refreshProjectBenefit: () => void;
}

const ProjectItem: React.FC<IProps> = ({
  projectItem,
  projectList,
  setProjectList,
  refreshProjectBenefit,
}: IProps) => {
  const { t } = useTranslation();
  const { message: messageApi,modal } = App.useApp();

  const [isShareProjectModalOpen, setIsShareProjectModalOpen] =
    React.useState<boolean>(false);
  const [isRenameProjectModalOpen, setIsRenameProjectModalOpen] =
    React.useState<boolean>(false);

  const copyProject = async () => {
    const res = await dashboardApi.copyProject(projectItem.id);
    if (res.success && res.result?.code === 0) {
      let newState = [...projectList];
      const index = projectList.findIndex(
        (item: ProjectItemObj) => item.id === projectItem.id
      );

      if (index !== -1) {
        const newItem = {
          ...projectList[index],
          id: res.result.data.projectId,
          name: res.result.data.projectName,
        }; // 复制对象并生成新的key
        newState.unshift(newItem); // 将新项目插入到数组最前面
      }
      setProjectList(newState);
      refreshProjectBenefit();
      messageApi.success(t("copy_success"));
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };

  const deleteProject = async () => {
    const res = await dashboardApi.deleteProject(projectItem.id);
    if (res.success && res.result?.code === 0) {
      messageApi.success(t("delete_success"));
      setProjectList(projectList.filter((item) => item.id !== projectItem.id));
      refreshProjectBenefit();
    } else {
      if (res.result?.msg) {
        messageApi.error(res.result.msg);
      }
    }
  };
  const showCopyProjectConfirm = () => {
    modal.confirm({
      wrapClassName: style.confirmWrapper,
      // title: t("copy_project"),
      icon: <ExclamationCircleFilled />,
      okText: t("confirm"),
      cancelText: t("cancel"),
      centered: true,
      okButtonProps: {
        className: "custom-ok-button",
        style: { backgroundColor: "#7E2FFF", borderColor: "#7E2FFF" },
      },
      cancelButtonProps: {
        className: "custom-cancel-button",
        style: { borderColor: "#7E2FFF", color: "#7E2FFF" },
      },
      content: (
        <p>
          {t("copy_project_content")}
          <span className="text-primary">{projectItem.name}</span>
        </p>
      ),
      onOk() {
        copyProject();
      },
      onCancel() {},
    });
  };
  const showDelProjectConfirm = () => {
    modal.confirm({
      wrapClassName: style.confirmWrapper,
      // title: t("delete_project"),
      icon: <DeleteOutlined />,
      okText: t("confirm"),
      cancelText: t("cancel"),
      centered: true,
      okButtonProps: {
        className: "custom-ok-button",
        style: { backgroundColor: "#7E2FFF", borderColor: "#7E2FFF" },
      },
      cancelButtonProps: {
        className: "custom-cancel-button",
        style: { borderColor: "#7E2FFF", color: "#7E2FFF" },
      },
      content: (
        <p>
          {t("delete_project_content")}
          <span className="text-red-500">{projectItem.name}</span>
          <br />
          <span className="text-gray-900 font-semibold text-lg">{t("delete_warning")}</span>
        </p>
      ),
      onOk() {
        deleteProject();
      },
      onCancel() {},
    });
  };
  const items: MenuProps["items"] = [
    {
      icon: <img src={shareIcon} />,
      label: t("share_project"),
      key: "0",
      onClick: () => {
        setIsShareProjectModalOpen(true);
      },
    },
    {
      icon: <img src={copyIcon} />,
      label: t("copy_project"),
      key: "1",
      onClick: () => {
        showCopyProjectConfirm();
      },
    },
    {
      icon: <img src={renameIcon} />,
      label: t("rename"),
      key: "2",
      onClick: () => {
        setIsRenameProjectModalOpen(true);
      },
    },
    {
      type: "divider",
    },

    {
      icon: <DeleteOutlined style={{ fontSize: 16 }} />,
      label: t("delete"),
      key: "3",
      danger: true,
      onClick: () => {
        showDelProjectConfirm();
      },
    },
  ];
  return (
    <div className="flex flex-col rounded-lg overflow-hidden cursor-pointer">
      {/* <a href={`/project/${projectItem.id}`}  target="_blank"> */}
      <a href={`/project/${projectItem.id}`}>
        <div className="h-[264px] bg-gray-100 flex items-center justify-center relative rounded-lg overflow-hidden group">
          {projectItem.cover ? (
            <img
              src={projectItem.cover}
              loading="lazy"
              className="w-full h-full max-inline-full block-auto object-cover transition-all duration-300 ease-in-out group-hover:scale-110"
              alt={t("cover_image")}
              draggable="false"
            />
          ) : (
            <div className="w-full h-[264px] relative transition-all duration-300 ease-in-out group-hover:scale-110">
              <img
                src="data:image/svg+xml,%3csvg%20width='334'%20height='264'%20viewBox='0%200%20334%20264'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cg%20clip-path='url(%23clip0_6887_52196)'%3e%3cpath%20d='M10%2020C10%2017.7909%2011.7909%2016%2014%2016H30C32.2091%2016%2034%2017.7909%2034%2020V28C34%2030.2091%2032.2091%2030%2032H14C11.7909%2032%2010%2030.2091%2010%2028V20Z'%20fill='white'/%3e%3cpath%20d='M10%2044C10%2041.7909%2011.7909%2040%2014%2040H30C32.2091%2040%2034%2041.7909%2034%2044V52C34%2054.2091%2032.2091%2056%2030%2056H14C11.7909%2056%2010%2054.2091%2010%2052V44Z'%20fill='white'/%3e%3cpath%20d='M10%2068C10%2065.7909%2011.7909%2064%2014%2064H30C32.2091%2064%2034%2065.7909%2034%2068V76C34%2078.2091%2032.2091%2080%2030%2080H14C11.7909%2080%2010%2078.2091%2010%2076V68Z'%20fill='white'/%3e%3cpath%20d='M10%2092C10%2089.7909%2011.7909%2088%2014%2088H30C32.2091%2088%2034%2089.7909%2034%2092V100C34%20102.209%2032.2091%20104%2030%20104H14C11.7909%20104%2010%20102.209%2010%20100V92Z'%20fill='white'/%3e%3cpath%20d='M10%20116C10%20113.791%2011.7909%20112%2014%20112H30C32.2091%20112%2034%20113.791%2034%20116V124C34%20126.209%2032.2091%20128%2030%20128H14C11.7909%20128%2010%20126.209%2010%20124V116Z'%20fill='white'/%3e%3cpath%20d='M10%20140C10%20137.791%2011.7909%20136%2014%20136H30C32.2091%20136%2034%20137.791%2034%20140V148C34%20150.209%2032.2091%20152%2030%20152H14C11.7909%20152%2010%20150.209%2010%20148V140Z'%20fill='white'/%3e%3cpath%20d='M10%20164C10%20161.791%2011.7909%20160%2014%20160H30C32.2091%20160%2034%20161.791%2034%20164V172C34%20174.209%2032.2091%20176%2030%20176H14C11.7909%20176%2010%20174.209%2010%20172V164Z'%20fill='white'/%3e%3cpath%20d='M10%20188C10%20185.791%2011.7909%20184%2014%20184H30C32.2091%20184%2034%20185.791%2034%20188V196C34%20198.209%2032.2091%20200%2030%20200H14C11.7909%20200%2010%20198.209%2010%20196V188Z'%20fill='white'/%3e%3cpath%20d='M10%20212C10%20209.791%2011.7909%20208%2014%20208H30C32.2091%20208%2034%20209.791%2034%20212V220C34%20222.209%2032.2091%20224%2030%20224H14C11.7909%20224%2010%20222.209%2010%20220V212Z'%20fill='white'/%3e%3cpath%20d='M10%20236C10%20233.791%2011.7909%20232%2014%20232H30C32.2091%20232%2034%20233.791%2034%20236V244C34%20246.209%2032.2091%20248%2030%20248H14C11.7909%20248%2010%20246.209%2010%20244V236Z'%20fill='white'/%3e%3crect%20x='39'%20y='16'%20width='256'%20height='232'%20rx='4'%20fill='white'/%3e%3cpath%20d='M300%2020C300%2017.7909%20301.791%2016%20304%2016H320C322.209%2016%20324%2017.7909%20324%2020V28C324%2030.2091%20322.209%2032%20320%2032H304C301.791%2032%20300%2030.2091%20300%2028V20Z'%20fill='white'/%3e%3cpath%20d='M300%2044C300%2041.7909%20301.791%2040%20304%2040H320C322.209%2040%20324%2041.7909%20324%2044V52C324%2054.2091%20322.209%2056%20320%2056H304C301.791%2056%20300%2054.2091%20300%2052V44Z'%20fill='white'/%3e%3cpath%20d='M300%2068C300%2065.7909%20301.791%2064%20304%2064H320C322.209%2064%20324%2065.7909%20324%2068V76C324%2078.2091%20322.209%2080%20320%2080H304C301.791%2080%20300%2078.2091%20300%2076V68Z'%20fill='white'/%3e%3cpath%20d='M300%2092C300%2089.7909%20301.791%2088%20304%2088H320C322.209%2088%20324%2089.7909%20324%2092V100C324%20102.209%20322.209%20104%20320%20104H304C301.791%20104%20300%20102.209%20300%20100V92Z'%20fill='white'/%3e%3cpath%20d='M300%20116C300%20113.791%20301.791%20112%20304%20112H320C322.209%20112%20324%20113.791%20324%20116V124C324%20126.209%20322.209%20128%20320%20128H304C301.791%20128%20300%20126.209%20300%20124V116Z'%20fill='white'/%3e%3cpath%20d='M300%20140C300%20137.791%20301.791%20136%20304%20136H320C322.209%20136%20324%20137.791%20324%20140V148C324%20150.209%20322.209%20152%20320%20152H304C301.791%20152%20300%20150.209%20300%20148V140Z'%20fill='white'/%3e%3cpath%20d='M300%20164C300%20161.791%20301.791%20160%20304%20160H320C322.209%20160%20324%20161.791%20324%20164V172C324%20174.209%20322.209%20176%20320%20176H304C301.791%20176%20300%20174.209%20300%20172V164Z'%20fill='white'/%3e%3cpath%20d='M300%20188C300%20185.791%20301.791%20184%20304%20184H320C322.209%20184%20324%20185.791%20324%20188V196C324%20198.209%20322.209%20200%20320%20200H304C301.791%20200%20300%20198.209%20300%20196V188Z'%20fill='white'/%3e%3cpath%20d='M300%20212C300%20209.791%20301.791%20208%20304%20208H320C322.209%20208%20324%20209.791%20324%20212V220C324%20222.209%20322.209%20224%20320%20224H304C301.791%20224%20300%20222.209%20300%20220V212Z'%20fill='white'/%3e%3cpath%20d='M300%20236C300%20233.791%20301.791%20232%20304%20232H320C322.209%20232%20324%20233.791%20324%20236V244C324%20246.209%20322.209%20248%20320%20248H304C301.791%20248%20300%20246.209%20300%20244V236Z'%20fill='white'/%3e%3c/g%3e%3cdefs%3e%3cclipPath%20id='clip0_6887_52196'%3e%3crect%20width='334'%20height='264'%20fill='white'/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e"
                alt=""
                className="w-full h-full"
              />
              <img
                src="data:image/svg+xml,%3csvg%20width='230'%20height='200'%20viewBox='0%200%20230%20200'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill-rule='evenodd'%20clip-rule='evenodd'%20d='M70.3138%2049.5436C83.6498%2043.3916%2093.7713%2030.5552%20108.45%2031.0517C124.998%2031.6114%20140.698%2039.5283%20151.259%2052.2813C162.728%2066.1296%20167.801%2083.7687%20166.982%20101.73C166.023%20122.783%20162.576%20145.451%20146.4%20158.958C129.247%20173.281%20104.893%20177.005%2083.1836%20171.704C62.5669%20166.671%2048.6758%20149.466%2036.4533%20132.116C24.127%20114.618%206.47802%2094.1479%2014.5982%2074.3459C22.6165%2054.7925%2051.1239%2058.3959%2070.3138%2049.5436Z'%20fill='%23F9FAFB'%20fill-opacity='0.61'/%3e%3cpath%20d='M114.077%2068.6568C82.1541%2050.9198%2062.1688%20153.262%2066.6172%20157.693C71.0656%20162.124%20186.085%20160.953%20189.358%20157.693C192.632%20154.432%20183.382%2092.0214%20161.538%2092.0214C139.694%2092.0214%20136.443%20115.933%20136.443%20115.933C136.443%20115.933%20129.046%2076.9738%20114.077%2068.6568Z'%20fill='%23F9FAFB'/%3e%3cpath%20d='M114.077%2068.6568C82.1541%2050.9198%2062.1688%20153.262%2066.6172%20157.693C71.0656%20162.124%20186.085%20160.953%20189.358%20157.693C192.632%20154.432%20183.382%2092.0214%20161.538%2092.0214C139.694%2092.0214%20136.443%20115.933%20136.443%20115.933C136.443%20115.933%20129.046%2076.9738%20114.077%2068.6568Z'%20fill='white'/%3e%3cpath%20d='M114.077%2068.6568C82.1541%2050.9198%2062.1688%20153.262%2066.6172%20157.693C71.0656%20162.124%20186.085%20160.953%20189.358%20157.693C192.632%20154.432%20183.382%2092.0214%20161.538%2092.0214C139.694%2092.0214%20136.443%20115.933%20136.443%20115.933C136.443%20115.933%20129.046%2076.9738%20114.077%2068.6568Z'%20stroke='%23F2F4F7'%20stroke-width='4'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3cpath%20d='M148.443%20116.681C149.611%20119.43%20152.927%20123.202%20156.443%20122.458C159.959%20121.714%20160.52%20113.697%20160.52%20113.697C160.52%20113.697%20164.05%20121.623%20168.807%20120.469C173.048%20119.441%20172.515%20113.584%20172.515%20113.584'%20stroke='%23F2F4F7'%20stroke-width='4'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3cpath%20d='M91%2095.5938C91%2095.5938%2091.8998%20105.594%2097.2986%20105.594C102.697%20105.594%20105.674%20101.935%20106.574%2098.3715C106.574%2098.3715%20108.303%20105.594%20113.701%20105.594C119.1%20105.594%20119.1%20100.157%20120%2096.5937'%20stroke='%23F2F4F7'%20stroke-width='4'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3cpath%20d='M189.685%2070.8199C188.107%2076.5938%20162.856%2078.0372%20152.347%2075.1503C141.839%2072.2634%20145.642%2061.5944%20154.582%2059.3349C159.7%2046.281%20170.747%2049.168%20176.932%2059.3349C186.886%2060.4647%20191.264%2065.0461%20189.685%2070.8199Z'%20fill='white'%20stroke='%23F2F4F7'%20stroke-width='4'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3cpath%20d='M54.9462%20148.141C50.9179%20137.847%2055.2377%20122.207%2066.2925%20122.207C77.3474%20122.207%2081.6672%20137.847%2077.6388%20148.141C75.3554%20153.977%2066.2925%20159.488%2066.2925%20159.488C66.2925%20159.488%2057.2297%20153.977%2054.9462%20148.141Z'%20fill='white'%20stroke='%23F2F4F7'%20stroke-width='3'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3cpath%20d='M66.2969%20148.105V165.967'%20stroke='%23F2F4F7'%20stroke-width='3'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3cpath%20d='M33.6844%20154.111C31.1011%20147.51%2033.8712%20137.48%2040.9604%20137.48C48.0496%20137.48%2050.8198%20147.51%2048.2365%20154.111C46.7722%20157.854%2040.9604%20161.388%2040.9604%20161.388C40.9604%20161.388%2035.1487%20157.854%2033.6844%20154.111Z'%20fill='white'%20stroke='%23F2F4F7'%20stroke-width='3'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3cpath%20d='M40.9629%20155.484V165.543'%20stroke='%23F2F4F7'%20stroke-width='3'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3c/svg%3e"
                className="w-52 h-52 absolute top-0 right-0 left-0 bottom-0 m-auto"
                alt=""
              />
            </div>
          )}
          <div className="absolute top-4 left-4">
            <div className="flex items-center">
              <Tag className="text-primary shadow rounded-full bg-white/80">
                {projectItem.storyBoardTypeDesc}
              </Tag>
              <Tag className="shadow rounded-full bg-white/80 text-slate-600">
                {projectItem.pictureSize}
              </Tag>
            </div>
          </div>
        </div>
      </a>
      <div className="px-3 pt-6 flex justify-between items-center">
        <div className="flex flex-col justify-center space-y-1">
          <p className="text-xs text-primary font-semibold">
            {t("update_time")} · {projectItem.updateTime}
          </p>
          <h2 className="text-sm mb-1 truncate w-48 font-semibold">
            {projectItem.name}
          </h2>
        </div>
        <Dropdown menu={{ items }} trigger={["click"]}>
          <Button
            type="text"
            shape="circle"
            className="text-gray-500"
            icon={<img src={extendIcon} />}
          />
        </Dropdown>
        <ShareProjectModal
          projectId={projectItem.id}
          isModalOpen={isShareProjectModalOpen}
          setIsModalOpen={setIsShareProjectModalOpen}
        />
        <RenameProjectModal
          projectId={projectItem.id}
          isModalOpen={isRenameProjectModalOpen}
          setIsModalOpen={setIsRenameProjectModalOpen}
          onRenameSuccess={(newName) => {
            // 更新项目列表中的项目名称
            const updatedList = projectList.map((item) =>
              item.id === projectItem.id ? { ...item, name: newName } : item
            );
            setProjectList(updatedList);
          }}
        />
      </div>
    </div>
  );
};

export default ProjectItem;
