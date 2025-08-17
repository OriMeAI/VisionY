import * as React from 'react';
import { useTranslation } from 'react-i18next';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

// 类型定义
interface MarkdownTextProps {
  text: string | undefined;
  className?: string;
}

const MarkdownText: React.FC<MarkdownTextProps> = ({ text, className = '' }) => {
  if (typeof text !== 'string' || !text) return null;
  return (
    <div className={`prose prose-gray max-w-none ${className}`}>
      <ReactMarkdown remarkPlugins={[remarkGfm]}>{text}</ReactMarkdown>
    </div>
  );
};

interface MarkdownListProps {
  items: string[] | undefined;
}

const MarkdownList: React.FC<MarkdownListProps> = ({ items }) => {
  if (!Array.isArray(items) || items.length === 0) return null;
  return (
    <ul className="list-none list-inside space-y-2 text-gray-700 leading-relaxed ml-4 mb-6">
      {items.map((item, index) => (
        <li key={index} className="pl-2">
          <MarkdownText text={item} className="inline" />
        </li>
      ))}
    </ul>
  );
};

// 定义 JSON 结构中列表项的期望类型
type StringList = string[];
type ContactInfoList = string[];

// 定义 JSON 结构中复杂对象的类型
interface IntroductionShape {
  p1: string;
  p2: string;
}

interface SubsectionShape {
  title: string;
  p1?: string;
  listItems?: StringList;
}

const Content: React.FC = () => {
  const { t } = useTranslation();

  // 从 t 函数获取特定结构的数据，使用类型断言
  const introduction = t('introduction', { returnObjects: true }) as IntroductionShape;

  const s1_ourMission = t('sections.s1_ourMission', { returnObjects: true }) as any;
  const s2_whatWeDo = t('sections.s2_whatWeDo', { returnObjects: true }) as any;

  const s3_ourTechnology = t('sections.s3_ourTechnology', { returnObjects: true }) as any;
  const s3_1_aiCore = t('sections.s3_ourTechnology.subsections.s3_1_aiCore', { returnObjects: true }) as SubsectionShape;
  const s3_2_audioGeneration = t('sections.s3_ourTechnology.subsections.s3_2_audioGeneration', { returnObjects: true }) as SubsectionShape;
  const s3_3_customization = t('sections.s3_ourTechnology.subsections.s3_3_customization', { returnObjects: true }) as SubsectionShape;
  const s3_4_cloudIntegration = t('sections.s3_ourTechnology.subsections.s3_4_cloudIntegration', { returnObjects: true }) as SubsectionShape;

  const s4_ourTeam = t('sections.s4_ourTeam', { returnObjects: true }) as any;
  const s5_ourValues = t('sections.s5_ourValues', { returnObjects: true }) as any;
  const s6_ourVision = t('sections.s6_ourVision', { returnObjects: true }) as any;
  const s7_contactUs = t('sections.s7_contactUs', { returnObjects: true }) as any;

  const s7_contactInfo = t('sections.s7_contactUs.contactInfo', { returnObjects: true }) as ContactInfoList;

  return (
    <div className="max-w-[1024px] mx-auto flex-1 p-6">
      {/* 页面标题 */}
      <div className="mb-8">
        <MarkdownText text={t('pageTitle') as string} className="text-3xl font-bold text-gray-900 mb-4" />
        <MarkdownText text={t('lastUpdated') as string} className="text-sm text-gray-500 mb-6" />
      </div>

      {/* 介绍部分 */}
      <div className="mb-8 space-y-4">
        <MarkdownText text={introduction.p1} className="text-base text-gray-700 leading-relaxed mb-4" />
        <MarkdownText text={introduction.p2} className="text-base text-gray-700 leading-relaxed mb-6" />
      </div>

      {/* Section 1: Our Mission */}
      <section className="mb-8">
        <MarkdownText text={s1_ourMission.title} className="text-2xl font-semibold text-gray-900 mb-4" />
        <MarkdownText text={s1_ourMission.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
        <MarkdownList items={s1_ourMission.listItems} />
      </section>

      {/* Section 2: What We Do */}
      <section className="mb-8">
        <MarkdownText text={s2_whatWeDo.title} className="text-2xl font-semibold text-gray-900 mb-4" />
        <MarkdownText text={s2_whatWeDo.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
        <MarkdownList items={s2_whatWeDo.listItems} />
      </section>

      {/* Section 3: Our Technology */}
      <section className="mb-8">
        <MarkdownText text={s3_ourTechnology.title} className="text-2xl font-semibold text-gray-900 mb-4" />
        <MarkdownText text={s3_ourTechnology.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
        <div className="ml-4 space-y-6">
          <div>
            <MarkdownText text={s3_1_aiCore.title} className="text-xl font-medium text-gray-800 mb-3" />
            <MarkdownText text={s3_1_aiCore.p1} className="text-base text-gray-700 leading-relaxed mb-4" />
          </div>
          <div>
            <MarkdownText text={s3_2_audioGeneration.title} className="text-xl font-medium text-gray-800 mb-3" />
            <MarkdownText text={s3_2_audioGeneration.p1} className="text-base text-gray-700 leading-relaxed mb-4" />
          </div>
          <div>
            <MarkdownText text={s3_3_customization.title} className="text-xl font-medium text-gray-800 mb-3" />
            <MarkdownText text={s3_3_customization.p1} className="text-base text-gray-700 leading-relaxed mb-4" />
          </div>
          <div>
            <MarkdownText text={s3_4_cloudIntegration.title} className="text-xl font-medium text-gray-800 mb-3" />
            <MarkdownText text={s3_4_cloudIntegration.p1} className="text-base text-gray-700 leading-relaxed mb-4" />
          </div>
        </div>
      </section>

      {/* Section 4: Our Team */}
      <section className="mb-8">
        <MarkdownText text={s4_ourTeam.title} className="text-2xl font-semibold text-gray-900 mb-4" />
        <MarkdownText text={s4_ourTeam.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
        <MarkdownList items={s4_ourTeam.listItems} />
        <MarkdownText text={s4_ourTeam.p1} className="text-base text-gray-700 leading-relaxed mb-6" />
      </section>

      {/* Section 5: Our Values */}
      <section className="mb-8">
        <MarkdownText text={s5_ourValues.title} className="text-2xl font-semibold text-gray-900 mb-4" />
        <MarkdownText text={s5_ourValues.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
        <MarkdownList items={s5_ourValues.listItems} />
      </section>

      {/* Section 6: Our Vision */}
      <section className="mb-8">
        <MarkdownText text={s6_ourVision.title} className="text-2xl font-semibold text-gray-900 mb-4" />
        <MarkdownText text={s6_ourVision.p1} className="text-base text-gray-700 leading-relaxed mb-4" />
        <MarkdownText text={s6_ourVision.p2} className="text-base text-gray-700 leading-relaxed mb-6" />
      </section>

      {/* Section 7: Contact Us */}
      <section className="mb-8">
        <MarkdownText text={s7_contactUs.title} className="text-2xl font-semibold text-gray-900 mb-4" />
        <MarkdownText text={s7_contactUs.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
        <div className="space-y-2">
          {s7_contactInfo.map((info, index) => (
            <div key={index} className="text-base text-gray-700 leading-relaxed">
              <MarkdownText text={info} />
            </div>
          ))}
        </div>
      </section>
    </div>
  );
};

export default Content;