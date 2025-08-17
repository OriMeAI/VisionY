/**
 * 首页
 */
import React, {useEffect} from "react";
import Footer from "../common/Layout/Footer";
import Header from "../common/Layout/Header";
import Content from "./Content";
import style from "./style.module.css";
import homeBg from "./../../../assets/images/pages/home/NosiyBackground.png";
import authService from "../../libs/auth-service";
import { IUserContexts, UserContexts } from "./../../contexts/user-contexts";

const Home: React.FC = () => {
  const [isScrolled, setIsScrolled] = React.useState(false);
  const userContexts: IUserContexts = React.useContext<IUserContexts>(UserContexts);

  useEffect(() => {
    authService.registerLogoutCallback(() => {
      userContexts.setIsAuthenticated(false);
      userContexts.setUserInfo(undefined);
    });
  }, [userContexts]);  

  useEffect(() => {
    // 设置 body 的 overflow 为 hidden
    document.body.style.overflow = 'hidden';
    
    const handleScroll = () => {
      // 直接获取 home-scrollbar 元素
      const scrollContainer = document.getElementById('home-scrollbar');
      if (scrollContainer && scrollContainer.scrollTop > 0) {
        setIsScrolled(true);
      } else {
        setIsScrolled(false);
      }
    };
  
    const scrollContainer = document.getElementById('home-scrollbar');
    if (scrollContainer) {
      scrollContainer.addEventListener("scroll", handleScroll);
    }
    
    return () => {
      // 组件卸载时恢复 body 样式
      document.body.style.overflow = '';
      const scrollContainer = document.getElementById('home-scrollbar');
      if (scrollContainer) {
        scrollContainer.removeEventListener("scroll", handleScroll);
      }
    };
  }, []);
  
  return (
    <div style={{ maxHeight: '100vh',overflowY: 'auto' }} className={style.simpleBarCustom} id="home-scrollbar">
      <div
        style={{ backgroundImage: `url(${homeBg})` }}
        className={`relative flex flex-col min-h-screen justify-center overlay overflow-x-hidden ${style.homeWrapper}`}
      >
        <div className="relative z-10 w-full">
          <div
            className={`fixed top-0 z-20 w-screen ${
              isScrolled
                ? "backdrop-blur-lg bg-black bg-opacity-40"
                : "transparent"
            }`}
          >
            <Header />
          </div>
          <Content />
          <footer className="bg-[#1D1C1C]">
            <Footer />
          </footer>
        </div>
      </div>
    </div>
  );
};

export default Home;
