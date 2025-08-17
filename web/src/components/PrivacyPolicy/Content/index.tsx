import * as React from 'react';
import { useTranslation } from 'react-i18next';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm'; // 支持 GFM (GitHub Flavored Markdown) 表格等

// 类型定义
interface MarkdownTextProps {
    text: string | undefined;
    className?: string;
}

const MarkdownText: React.FC<MarkdownTextProps> = ({ text, className = "" }) => {
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

// 定义 JSON 结构中列表项的期望类型 (用于类型断言)
type StringList = string[];
type ContactInfoList = string[];

// 定义 JSON 结构中复杂对象的类型
interface IntroductionShape {
    p1: string;
    p2: string;
    p3: string;
}

interface DirectInfoShape {
    title: string;
    listItems: StringList;
}

const Content: React.FC = () => {
    const { t } = useTranslation();

    // 从 t 函数获取特定结构的数据时，使用类型断言
    const introduction = t('introduction', { returnObjects: true }) as IntroductionShape;

    const s1_collectedInfo = t('sections.s1_collectedInfo', { returnObjects: true }) as any;
    const s1_1_directInfo = t('sections.s1_collectedInfo.subsections.s1_1_directInfo', { returnObjects: true }) as DirectInfoShape;
    const s1_2_autoInfo = t('sections.s1_collectedInfo.subsections.s1_2_autoInfo', { returnObjects: true }) as { title: string; listItems: StringList };
    const s1_3_thirdPartyInfo = t('sections.s1_collectedInfo.subsections.s1_3_thirdPartyInfo', { returnObjects: true }) as { title: string; p1: string };

    const s2_listItems = t('sections.s2_howWeUseInfo.listItems', { returnObjects: true }) as StringList;
    const s3_listItems = t('sections.s3_howWeShareInfo.listItems', { returnObjects: true }) as StringList;

    const s4_aiContentRights = t('sections.s4_aiContentRights', { returnObjects: true }) as any;
    const s4_yourResponsibility_listItems = t('sections.s4_aiContentRights.points.yourResponsibility.listItems', { returnObjects: true }) as StringList;

    const s5_cookies_listItems = t('sections.s5_cookies.listItems', { returnObjects: true }) as StringList;
    const s8_yourRights_listItems = t('sections.s8_yourRights.listItems', { returnObjects: true }) as StringList;

    const s11_1_listItems = t('sections.s11_regionSpecific.subsections.s11_1_eeaUkSwitzerland.listItems', { returnObjects: true }) as StringList;
    const s11_2_listItems = t('sections.s11_regionSpecific.subsections.s11_2_california.listItems', { returnObjects: true }) as StringList;
    const s11_4_listItems = t('sections.s11_regionSpecific.subsections.s11_4_japan.listItems', { returnObjects: true }) as StringList;

    const s13_contactInfo = t('sections.s13_contactUs.contactInfo', { returnObjects: true }) as ContactInfoList;

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
                <MarkdownText text={introduction.p2} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownText text={introduction.p3} className="text-base text-gray-700 leading-relaxed mb-6" />
            </div>

            {/* Section 1: Collected Info */}
            <section className="mb-8">
                <MarkdownText text={s1_collectedInfo.title} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={s1_collectedInfo.intro} className="text-base text-gray-700 leading-relaxed mb-6" />

                <div className="ml-4">
                    <MarkdownText text={s1_1_directInfo.title} className="text-xl font-medium text-gray-800 mb-3" />
                    <MarkdownList items={s1_1_directInfo.listItems} />

                    <MarkdownText text={s1_2_autoInfo.title} className="text-xl font-medium text-gray-800 mb-3" />
                    <MarkdownList items={s1_2_autoInfo.listItems} />

                    <MarkdownText text={s1_3_thirdPartyInfo.title} className="text-xl font-medium text-gray-800 mb-3" />
                    <MarkdownText text={s1_3_thirdPartyInfo.p1} className="text-base text-gray-700 leading-relaxed mb-6" />
                </div>
            </section>

            {/* Section 2: How We Use Info */}
            <section className="mb-8">
                <MarkdownText text={t('sections.s2_howWeUseInfo.title') as string} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={t('sections.s2_howWeUseInfo.intro') as string} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownList items={s2_listItems} />
            </section>

            {/* Section 3: How We Share Info */}
            <section className="mb-8">
                <MarkdownText text={t('sections.s3_howWeShareInfo.title') as string} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={t('sections.s3_howWeShareInfo.intro') as string} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownList items={s3_listItems} />
            </section>

            {/* Section 4: AI Content Rights */}
            <section className="mb-8">
                <MarkdownText text={s4_aiContentRights.title} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={s4_aiContentRights.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownText text={s4_aiContentRights.points.attribution} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownText text={s4_aiContentRights.points.yourResponsibility.title} className="text-xl font-medium text-gray-800 mb-3" />
                <MarkdownList items={s4_yourResponsibility_listItems} />
                <MarkdownText text={s4_aiContentRights.points.visionyLicense} className="text-base text-gray-700 leading-relaxed mb-6" />
            </section>

            {/* Section 5: Cookies */}
            <section className="mb-8">
                <MarkdownText text={t('sections.s5_cookies.title') as string} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={t('sections.s5_cookies.intro') as string} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownList items={s5_cookies_listItems} />
                <MarkdownText text={t('sections.s5_cookies.p1') as string} className="text-base text-gray-700 leading-relaxed mb-6" />
            </section>

            {/* Section 6: Data Security */}
            <section className="mb-8">
                <MarkdownText text={t('sections.s6_dataSecurity.title') as string} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={t('sections.s6_dataSecurity.p1') as string} className="text-base text-gray-700 leading-relaxed mb-6" />
            </section>

            {/* Section 7: Data Retention */}
            <section className="mb-8">
                <MarkdownText text={t('sections.s7_dataRetention.title') as string} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={t('sections.s7_dataRetention.p1') as string} className="text-base text-gray-700 leading-relaxed mb-6" />
            </section>

            {/* Section 8: Your Rights */}
            <section className="mb-8">
                <MarkdownText text={t('sections.s8_yourRights.title') as string} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={t('sections.s8_yourRights.intro') as string} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownList items={s8_yourRights_listItems} />
                <MarkdownText text={t('sections.s8_yourRights.p1') as string} className="text-base text-gray-700 leading-relaxed mb-6" />
            </section>

            {/* Section 9: International Transfers */}
            <section className="mb-8">
                <MarkdownText text={t('sections.s9_internationalTransfers.title') as string} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={t('sections.s9_internationalTransfers.p1') as string} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownText text={t('sections.s9_internationalTransfers.p2') as string} className="text-base text-gray-700 leading-relaxed mb-6" />
            </section>

            {/* Section 10: Children's Privacy */}
            <section className="mb-8">
                <MarkdownText text={t('sections.s10_childrensPrivacy.title') as string} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={t('sections.s10_childrensPrivacy.p1') as string} className="text-base text-gray-700 leading-relaxed mb-6" />
            </section>

            {/* Section 11: Region Specific */}
            <section className="mb-8">
                <MarkdownText text={t('sections.s11_regionSpecific.title') as string} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={t('sections.s11_regionSpecific.intro') as string} className="text-base text-gray-700 leading-relaxed mb-6" />

                <div className="ml-4 space-y-6">
                    <div>
                        <MarkdownText text={t('sections.s11_regionSpecific.subsections.s11_1_eeaUkSwitzerland.title') as string} className="text-xl font-medium text-gray-800 mb-3" />
                        <MarkdownText text={t('sections.s11_regionSpecific.subsections.s11_1_eeaUkSwitzerland.p1') as string} className="text-base text-gray-700 leading-relaxed mb-4" />
                        <MarkdownList items={s11_1_listItems} />
                    </div>

                    <div>
                        <MarkdownText text={t('sections.s11_regionSpecific.subsections.s11_2_california.title') as string} className="text-xl font-medium text-gray-800 mb-3" />
                        <MarkdownText text={t('sections.s11_regionSpecific.subsections.s11_2_california.p1') as string} className="text-base text-gray-700 leading-relaxed mb-4" />
                        <MarkdownList items={s11_2_listItems} />
                        <MarkdownText text={t('sections.s11_regionSpecific.subsections.s11_2_california.p2') as string} className="text-base text-gray-700 leading-relaxed mb-4" />
                    </div>

                    <div>
                        <MarkdownText text={t('sections.s11_regionSpecific.subsections.s11_3_china.title') as string} className="text-xl font-medium text-gray-800 mb-3" />
                        <MarkdownText text={t('sections.s11_regionSpecific.subsections.s11_3_china.p1') as string} className="text-base text-gray-700 leading-relaxed mb-4" />
                    </div>

                    <div>
                        <MarkdownText text={t('sections.s11_regionSpecific.subsections.s11_4_japan.title') as string} className="text-xl font-medium text-gray-800 mb-3" />
                        <MarkdownText text={t('sections.s11_regionSpecific.subsections.s11_4_japan.p1') as string} className="text-base text-gray-700 leading-relaxed mb-4" />
                        <MarkdownList items={s11_4_listItems} />
                        <MarkdownText text={t('sections.s11_regionSpecific.subsections.s11_4_japan.p2') as string} className="text-base text-gray-700 leading-relaxed mb-4" />
                        <MarkdownText text={t('sections.s11_regionSpecific.subsections.s11_4_japan.p3') as string} className="text-base text-gray-700 leading-relaxed mb-4" />
                    </div>

                    <div>
                        <MarkdownText text={t('sections.s11_regionSpecific.subsections.s11_5_otherJurisdictions.title') as string} className="text-xl font-medium text-gray-800 mb-3" />
                        <MarkdownText text={t('sections.s11_regionSpecific.subsections.s11_5_otherJurisdictions.p1') as string} className="text-base text-gray-700 leading-relaxed mb-4" />
                    </div>
                </div>
            </section>

            {/* Section 12: Policy Changes */}
            <section className="mb-8">
                <MarkdownText text={t('sections.s12_policyChanges.title') as string} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={t('sections.s12_policyChanges.p1') as string} className="text-base text-gray-700 leading-relaxed mb-6" />
            </section>

            {/* Section 13: Contact Us */}
            <section className="mb-8">
                <MarkdownText text={t('sections.s13_contactUs.title') as string} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={t('sections.s13_contactUs.p1') as string} className="text-base text-gray-700 leading-relaxed mb-4" />
                <div className="space-y-2">
                    {s13_contactInfo.map((info, index) => (
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