import React, { useEffect, useState } from 'react';
import { Space, Typography } from 'antd';
import { useTranslation } from 'react-i18next';

const { Text, Link } = Typography;

const NewFooter: React.FC = () => {
  const { t } = useTranslation();
  const [currentYear, setCurrentYear] = useState<number>(new Date().getFullYear());
  
  useEffect(() => {
    setCurrentYear(new Date().getFullYear());
  }, []);

  return (
    <footer className="bg-brand-dark text-slate-400 py-10">
      <div className="container max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <div className="flex justify-center items-center space-x-6 mb-6">
          <a href="https://discord.gg/CBaZPDjWEn" target="_blank" rel="noopener noreferrer" aria-label="Discord"
                className="text-slate-400 hover:text-secondary transition-colors duration-300">
            <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <title>Discord</title>
              <path
                d="M20.317 4.3698a19.7913 19.7913 0 00-4.8851-1.5152.0741.0741 0 00-.0785.0371c-.211.3753-.4404.8648-.6083 1.2495-1.8447-.2762-3.68-.2762-5.4868 0-.1679-.3847-.3973-.8742-.6083-1.2495a.0741.0741 0 00-.0785-.0371 19.7363 19.7363 0 00-4.8851 1.5152.0699.0699 0 00-.0321.0277C.5334 9.0458-.319 13.5779.0992 18.0578a.0824.0824 0 00.0312.0561c2.0528 1.5076 4.0413 2.4228 5.9929 3.0294a.0777.0777 0 00.0842-.0276c.4616-.6304.8731-1.2952 1.227-1.9942a.076.076 0 00-.0416-.1057c-.6528-.2476-1.278-.5495-1.8722-.8923a.077.077 0 01-.0076-.1277c.1258-.0941.2517-.1923.3718-.2914a.0743.0743 0 01.0776-.0106c3.9278 1.7933 8.18 1.7933 12.0614 0a.0743.0743 0 01.0776.0106c.1201.0991.246.1973.3718.2914a.077.077 0 01-.0076.1277c-.5942.3428-1.2194.6447-1.8722.8923a.076.076 0 00-.0416.1057c.3539.699.7654 1.3638 1.227 1.9942a.0777.0777 0 00.0842.0276c1.9516-.6067 3.9401-1.5219 5.9929-3.0294a.0824.0824 0 00.0312-.0561c.5004-4.3802-.3265-8.9762-2.6054-13.6602a.0699.0699 0 00-.0321-.0277zM8.0201 15.3312c-.7804 0-1.4162-.8163-1.4162-1.8229 0-1.0066.6358-1.823 1.4162-1.823.7804 0 1.4161.8163 1.4161 1.823 0 1.0066-.6357 1.8229-1.4161 1.8229zm7.9748 0c-.7804 0-1.4162-.8163-1.4162-1.8229 0-1.0066.6358-1.823 1.4162-1.823.7804 0 1.4162.8163 1.4162 1.823 0 1.0066-.6358 1.8229-1.4162 1.8229Z" />
            </svg>
          </a>
          <a href="https://www.x.com/VisionY_AI" target="_blank" rel="noopener noreferrer" aria-label="Twitter"
                className="text-slate-400 hover:text-secondary transition-colors duration-300">
            <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <title>X/Twitter</title>
              <path
                d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z" />
            </svg>
          </a>
          <a href="https://www.youtube.com/@VisionY_AI" target="_blank" rel="noopener noreferrer" aria-label="YouTube"
                className="text-slate-400 hover:text-secondary transition-colors duration-300">
            <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <title>Youtube</title>
              <path
                d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z" />
            </svg>
          </a>
          {/* <a href="https://www.tiktok.com/@visiony_ai" target="_blank" rel="noopener noreferrer" aria-label="TikTok"
                className="text-slate-400 hover:text-secondary transition-colors duration-300">
            <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg">
              <title>Tiktok</title>
              <path d="M448,209.91a210.06,210.06,0,0,1-122.77-39.25V349.38A162.55,162.55,0,1,1,185,188.31V278.2a74.62,74.62,0,1,0,52.23,71.18V0l88,0a121.18,121.18,0,0,0,1.86,22.17h0A122.18,122.18,0,0,0,381,102.39a121.43,121.43,0,0,0,67,20.14Z" />
            </svg>
          </a> */}
          <a href="https://www.instagram.com/visiony_ai" target="_blank" rel="noopener noreferrer" aria-label="Instagram"
              className="text-slate-400 hover:text-secondary transition-colors duration-300">
            <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <title>Instagram</title>
              <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/>
            </svg>
          </a>
        </div>
        <Text className="text-sm text-slate-400">
            © {currentYear} Orime. {t('all_rights_reserved')}
        </Text>
        <div className="text-xs mt-4">
          <Space split="|">
            <a href="/termsofuse" target="_blank" className="text-slate-400 hover:text-secondary transition-colors">
                {t('terms_of_use')}
            </a>
            <a href="/privacypolicy" target="_blank" className="text-slate-400 hover:text-secondary transition-colors">
                {t('privacy_policy')}
            </a>
            <a href="/aboutus" target="_blank" className="text-slate-400 hover:text-secondary transition-colors">
                {t('about_us')}
            </a>
          </Space>
        </div>
      </div>
    </footer>
  );
};

export default NewFooter;