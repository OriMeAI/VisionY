/**
 * 创建新作品按钮文字
 */

import React from 'react';
import { useTranslation } from 'react-i18next';
const CreateNewText: React.FC = () => {
  const {t} = useTranslation();
  return <span className="font-semibold">{t('create_new_work')}</span>;
};

export default CreateNewText;
