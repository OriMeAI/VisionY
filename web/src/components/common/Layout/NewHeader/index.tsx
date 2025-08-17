import React, { useState } from 'react';
import { Button } from 'antd';
import { MenuOutlined } from '@ant-design/icons';
import { useTranslation } from 'react-i18next';
import LanguageDropdown from "../../LanguageDropdown";
import LogoImage from "./../../../../../home/static/assets/visiony_logo_transparent_180.svg" 

const NewHeader: React.FC = () => {
  const { t } = useTranslation();
  const [mobileNavVisible, setMobileNavVisible] = useState(false);
  
  const toggleMobileNav = () => {
    setMobileNavVisible(!mobileNavVisible);
  };

  return (
    <header className="bg-white/95 backdrop-blur-sm shadow-md sticky top-0 z-50 w-full">
      <nav className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center h-[75px]">
        <a 
          href="/" 
          target="_blank"
          className="flex items-center hover:scale-105 border-none transition-all duration-200 px-2 py-1"
        >
          <div className="mr-2">
            <img 
              src={LogoImage}
              alt="VisionY Logo" 
              width="40"
              height="40" 
              className="logo-icon"
            />
          </div>
          <div className="logo text-2xl font-bold text-primary">VisionY</div>
        </a>

        <div className="hidden md:flex items-center space-x-8 nav-links-desktop">
          <a 
            href="https://github.com/OriMeAI/VisionY" 
            target="_blank"
            rel="noopener noreferrer"
            className="text-brand-dark text-base font-medium hover:text-primary transition-colors flex items-center"
          >
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
                stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"
                className="mr-1">
                <path
                    d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22">
                </path>
            </svg>
            GitHub
          </a>
          
          <div className="relative">
            <LanguageDropdown />
          </div>
          
          <Button 
            type="primary" 
            href="/workspace"
            target="_blank"
            style={{ height: 40 }}
            className="hover:scale-105 text-base font-medium hover:shadow-lg outline-none"
          >
            {t('workspace')}
          </Button>
        </div>
        
        <Button 
          type="text" 
          className="md:hidden text-sm text-brand-dark"
          icon={<MenuOutlined />}
          onClick={toggleMobileNav}
          aria-label="Toggle navigation"
        />
      </nav>
      
      {mobileNavVisible && (
        <div className="nav-links-mobile md:hidden absolute top-[75px] left-0 w-full bg-brand-light backdrop-blur-sm shadow-lg flex flex-col items-center py-4 space-y-4">
          <a 
            href="https://github.com/OriMeAI/VisionY" 
            target="_blank"
            rel="noopener noreferrer"
            className="text-brand-dark text-base font-medium hover:text-primary transition-colors flex items-center justify-center"
          >
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                className="mr-1">
                <path
                    d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22">
                </path>
            </svg>
            GitHub
          </a>
          
          <div className="relative">
            <LanguageDropdown />
          </div>
          
          <Button 
            type="primary" 
            href="/workspace"
            target="_blank"
            style={{ height: 40 }}
            className="hover:scale-105 text-base font-medium hover:shadow-lg outline-none"
          >
            {t('workspace')}
          </Button>
        </div>
      )}
    </header>
  );
};

export default NewHeader;