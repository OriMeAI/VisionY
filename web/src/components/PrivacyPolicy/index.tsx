/**
 * 隐私政策页面
 */
import * as React from "react";

// import Footer from "../common/Layout/Footer";
// import Header from "../common/Layout/Header";
import NewFooter from "../common/Layout/NewFooter";
import NewHeader from "../common/Layout/NewHeader";

import Content from "./Content";

const PrivacyPolicy: React.FC = () => {
  return (
    <div className="min-h-screen flex flex-col">
      {/* 固定在顶部的 Header */}
      <NewHeader/>
      
      {/* 内容区域，带有顶部和底部的 padding 以避免被 header 和 footer 遮挡 */}
      <div className="flex-1 flex flex-col">
        <Content />
      </div>
      
      {/* 固定在底部的 Footer */}
      <NewFooter/>
    </div>
  );
};

export default PrivacyPolicy;
