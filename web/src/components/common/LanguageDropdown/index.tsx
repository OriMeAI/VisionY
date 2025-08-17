// src/components/LanguageDropdown.tsx
import { Select } from 'antd';
import * as React from 'react';
import { useTranslation } from 'react-i18next';

// 定义 SUPPORTED_LANGUAGES 的类型
const LANGUAGE_KEY = 'language';

const SUPPORTED_LANGUAGES = {
  'en-US': { value: 'en', label: 'English' },
  'zh-CN': { value: 'cn', label: '简体中文' },
  'zh-TW': { value: 'tw', label: '繁體中文' },
  'ja-JP': { value: 'ja', label: '日本語' },
} as const; // 使用 as const 确保键和值是只读的

type LanguageCode = keyof typeof SUPPORTED_LANGUAGES;

const LanguageDropdown: React.FC = () => {
  const { i18n } = useTranslation();

  const getBrowserLanguage = (): LanguageCode => {
    const savedLanguage = localStorage.getItem(LANGUAGE_KEY) as LanguageCode | null;
    if (savedLanguage && SUPPORTED_LANGUAGES[savedLanguage]) {
      return savedLanguage;
    }
    const browserLang = navigator.language || (navigator as any).userLanguage;
    if (SUPPORTED_LANGUAGES[browserLang as LanguageCode]) {
      return browserLang as LanguageCode;
    }
    return 'en-US';
  };

  const handleChange = async (value: string) => {
    const langCode = (Object.keys(SUPPORTED_LANGUAGES) as LanguageCode[]).find(
      (key) => SUPPORTED_LANGUAGES[key].value === value
    );
    if (langCode) {
      localStorage.setItem(LANGUAGE_KEY, langCode);
      await i18n.changeLanguage(langCode);
      location.reload();
    }
  };

  React.useEffect(() => {
    const language = getBrowserLanguage();
    i18n.changeLanguage(language);
    localStorage.setItem(LANGUAGE_KEY, language);
  }, []);

  // 获取当前语言，如果不存在则使用默认语言
  const getCurrentLanguage = (): LanguageCode => {
    const currentLang = i18n.language as LanguageCode;
    return SUPPORTED_LANGUAGES[currentLang] ? currentLang : 'en-US';
  };

  const currentLanguage = getCurrentLanguage();

  return (
    <Select
      value={SUPPORTED_LANGUAGES[currentLanguage].value}
      style={{ width: 120 }}
      onChange={handleChange}
      options={Object.entries(SUPPORTED_LANGUAGES).map(([key, { value,label }]) => ({
        value,
        label,
      }))}
    />
  );
};

export default LanguageDropdown;