import * as React from 'react';
import { useTranslation } from 'react-i18next';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm'; // 支持 GFM (GitHub Flavored Markdown) 表格等

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
    points?: { [key: string]: string };
    listItems?: StringList;
    p1?: string;
}

const Content: React.FC = () => {
    const { t } = useTranslation();

    // 从 t 函数获取特定结构的数据时，使用类型断言
    const introduction = t('introduction', { returnObjects: true }) as IntroductionShape;

    const s1_definitions = t('sections.s1_definitions', { returnObjects: true }) as any;
    const s2_acceptance = t('sections.s2_acceptance', { returnObjects: true }) as any;
    const s3_serviceDescription = t('sections.s3_serviceDescription', { returnObjects: true }) as any;
    const s4_account = t('sections.s4_account', { returnObjects: true }) as any;

    const s5_userContentIP = t('sections.s5_userContentIP', { returnObjects: true }) as any;
    const s5_1_userInputContent = t('sections.s5_userContentIP.subsections.s5_1_userInputContent', { returnObjects: true }) as SubsectionShape;
    const s5_2_aiGeneratedContent = t('sections.s5_userContentIP.subsections.s5_2_aiGeneratedContent', { returnObjects: true }) as SubsectionShape;
    const s5_3_yourResponsibility = t('sections.s5_userContentIP.subsections.s5_3_yourResponsibility', { returnObjects: true }) as SubsectionShape;
    const s5_4_visionyIP = t('sections.s5_userContentIP.subsections.s5_4_visionyIP', { returnObjects: true }) as SubsectionShape;

    const s6_aup = t('sections.s6_aup', { returnObjects: true }) as any;
    const s7_aiNature = t('sections.s7_aiNature', { returnObjects: true }) as any;

    const s8_feesAndPayment = t('sections.s8_feesAndPayment', { returnObjects: true }) as any;
    const s8_1_membership = t('sections.s8_feesAndPayment.subsections.s8_1_membership', { returnObjects: true }) as SubsectionShape;
    const s8_2_credits = t('sections.s8_feesAndPayment.subsections.s8_2_credits', { returnObjects: true }) as SubsectionShape;
    const s8_3_paymentProcessing = t('sections.s8_feesAndPayment.subsections.s8_3_paymentProcessing', { returnObjects: true }) as SubsectionShape;
    const s8_4_taxes = t('sections.s8_feesAndPayment.subsections.s8_4_taxes', { returnObjects: true }) as SubsectionShape;
    const s8_5_refundPolicy = t('sections.s8_feesAndPayment.subsections.s8_5_refundPolicy', { returnObjects: true }) as SubsectionShape;

    const s9_thirdParty = t('sections.s9_thirdParty', { returnObjects: true }) as any;
    const s10_disclaimer = t('sections.s10_disclaimer', { returnObjects: true }) as any;
    const s11_liabilityLimitation = t('sections.s11_liabilityLimitation', { returnObjects: true }) as any;
    const s12_indemnification = t('sections.s12_indemnification', { returnObjects: true }) as any;
    const s13_termTermination = t('sections.s13_termTermination', { returnObjects: true }) as any;

    const s14_governingLaw = t('sections.s14_governingLaw', { returnObjects: true }) as any;
    const s14_1_governingLaw = t('sections.s14_governingLaw.subsections.s14_1_governingLaw', { returnObjects: true }) as SubsectionShape;
    const s14_2_informalResolution = t('sections.s14_governingLaw.subsections.s14_2_informalResolution', { returnObjects: true }) as SubsectionShape;
    const s14_3_arbitration = t('sections.s14_governingLaw.subsections.s14_3_arbitration', { returnObjects: true }) as SubsectionShape;
    const s14_4_classActionWaiver = t('sections.s14_governingLaw.subsections.s14_4_classActionWaiver', { returnObjects: true }) as SubsectionShape;

    const s15_internationalUsers = t('sections.s15_internationalUsers', { returnObjects: true }) as any;
    const s16_termsChanges = t('sections.s16_termsChanges', { returnObjects: true }) as any;
    const s17_generalTerms = t('sections.s17_generalTerms', { returnObjects: true }) as any;
    const s18_contactUs = t('sections.s18_contactUs', { returnObjects: true }) as any;
    const s19_finalAgreement = t('sections.s19_finalAgreement', { returnObjects: true }) as any;

    const s18_contactInfo = t('sections.s18_contactUs.contactInfo', { returnObjects: true }) as ContactInfoList;

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

            {/* Section 1: Definitions */}
            <section className="mb-8">
                <MarkdownText text={s1_definitions.title} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={s1_definitions.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownList items={s1_definitions.listItems} />
            </section>

            {/* Section 2: Acceptance */}
            <section className="mb-8">
                <MarkdownText text={s2_acceptance.title} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={s2_acceptance.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownList items={s2_acceptance.listItems} />
            </section>

            {/* Section 3: Service Description */}
            <section className="mb-8">
                <MarkdownText text={s3_serviceDescription.title} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={s3_serviceDescription.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownList items={s3_serviceDescription.listItems} />
                <MarkdownText text={s3_serviceDescription.p1} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownText text={s3_serviceDescription.p2} className="text-base text-gray-700 leading-relaxed mb-6" />
            </section>

            {/* Section 4: Account */}
            <section className="mb-8">
                <MarkdownText text={s4_account.title} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={s4_account.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownList items={s4_account.listItems} />
            </section>

            {/* Section 5: User Content IP */}
            <section className="mb-8">
                <MarkdownText text={s5_userContentIP.title} className="text-2xl font-semibold text-gray-900 mb-4" />
                <div className="ml-4 space-y-6">
                    <div>
                        <MarkdownText text={s5_1_userInputContent.title} className="text-xl font-medium text-gray-800 mb-3" />
                        <MarkdownText text={s5_1_userInputContent.points?.ownership} className="text-base text-gray-700 leading-relaxed mb-4" />
                        <MarkdownText text={s5_1_userInputContent.points?.licenseToVisionY} className="text-base text-gray-700 leading-relaxed mb-4" />
                    </div>
                    <div>
                        <MarkdownText text={s5_2_aiGeneratedContent.title} className="text-xl font-medium text-gray-800 mb-3" />
                        <MarkdownText text={s5_2_aiGeneratedContent.points?.ownership} className="text-base text-gray-700 leading-relaxed mb-4" />
                        <MarkdownText text={s5_2_aiGeneratedContent.points?.limitedLicenseToVisionY} className="text-base text-gray-700 leading-relaxed mb-4" />
                    </div>
                    <div>
                        <MarkdownText text={s5_3_yourResponsibility.title} className="text-xl font-medium text-gray-800 mb-3" />
                        <MarkdownList items={s5_3_yourResponsibility.listItems} />
                    </div>
                    <div>
                        <MarkdownText text={s5_4_visionyIP.title} className="text-xl font-medium text-gray-800 mb-3" />
                        <MarkdownText text={s5_4_visionyIP.p1} className="text-base text-gray-700 leading-relaxed mb-4" />
                    </div>
                </div>
            </section>

            {/* Section 6: AUP */}
            <section className="mb-8">
                <MarkdownText text={s6_aup.title} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={s6_aup.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownList items={s6_aup.listItems} />
                <MarkdownText text={s6_aup.p1} className="text-base text-gray-700 leading-relaxed mb-6" />
            </section>

            {/* Section 7: AI Nature */}
            <section className="mb-8">
                <MarkdownText text={s7_aiNature.title} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={s7_aiNature.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownList items={s7_aiNature.listItems} />
            </section>

            {/* Section 8: Fees and Payment */}
            <section className="mb-8">
                <MarkdownText text={s8_feesAndPayment.title} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={s8_feesAndPayment.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
                <div className="ml-4 space-y-6">
                    <div>
                        <MarkdownText text={s8_1_membership.title} className="text-xl font-medium text-gray-800 mb-3" />
                        <MarkdownText text={s8_1_membership.points?.plan} className="text-base text-gray-700 leading-relaxed mb-4" />
                        <MarkdownText text={s8_1_membership.points?.billingCycle} className="text-base text-gray-700 leading-relaxed mb-4" />
                        <MarkdownText text={s8_1_membership.points?.autoRenewal} className="text-base text-gray-700 leading-relaxed mb-4" />
                        <MarkdownText text={s8_1_membership.points?.cancellation} className="text-base text-gray-700 leading-relaxed mb-4" />
                        <MarkdownText text={s8_1_membership.points?.priceChange} className="text-base text-gray-700 leading-relaxed mb-4" />
                    </div>
                    <div>
                        <MarkdownText text={s8_2_credits.title} className="text-xl font-medium text-gray-800 mb-3" />
                        <MarkdownText text={s8_2_credits.points?.purchase} className="text-base text-gray-700 leading-relaxed mb-4" />
                        <MarkdownText text={s8_2_credits.points?.usage} className="text-base text-gray-700 leading-relaxed mb-4" />
                        <MarkdownText text={s8_2_credits.points?.noCashValue} className="text-base text-gray-700 leading-relaxed mb-4" />
                        <MarkdownText text={s8_2_credits.points?.validity} className="text-base text-gray-700 leading-relaxed mb-4" />
                        <MarkdownText text={s8_2_credits.points?.priceChange} className="text-base text-gray-700 leading-relaxed mb-4" />
                    </div>
                    <div>
                        <MarkdownText text={s8_3_paymentProcessing.title} className="text-xl font-medium text-gray-800 mb-3" />
                        <MarkdownText text={s8_3_paymentProcessing.p1} className="text-base text-gray-700 leading-relaxed mb-4" />
                    </div>
                    <div>
                        <MarkdownText text={s8_4_taxes.title} className="text-xl font-medium text-gray-800 mb-3" />
                        <MarkdownText text={s8_4_taxes.p1} className="text-base text-gray-700 leading-relaxed mb-4" />
                    </div>
                    <div>
                        <MarkdownText text={s8_5_refundPolicy.title} className="text-xl font-medium text-gray-800 mb-3" />
                        <MarkdownText text={s8_5_refundPolicy.p1} className="text-base text-gray-700 leading-relaxed mb-4" />
                    </div>
                </div>
            </section>

            {/* Section 9: Third Party */}
            <section className="mb-8">
                <MarkdownText text={s9_thirdParty.title} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={s9_thirdParty.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownText text={s9_thirdParty.p1} className="text-base text-gray-700 leading-relaxed mb-6" />
            </section>

            {/* Section 10: Disclaimer */}
            <section className="mb-8">
                <MarkdownText text={s10_disclaimer.title} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={s10_disclaimer.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownList items={s10_disclaimer.listItems} />
                <MarkdownText text={s10_disclaimer.p1} className="text-base text-gray-700 leading-relaxed mb-6" />
            </section>

            {/* Section 11: Liability Limitation */}
            <section className="mb-8">
                <MarkdownText text={s11_liabilityLimitation.title} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={s11_liabilityLimitation.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownList items={s11_liabilityLimitation.listItems} />
                <MarkdownText text={s11_liabilityLimitation.p1} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownText text={s11_liabilityLimitation.p2} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownText text={s11_liabilityLimitation.p3} className="text-base text-gray-700 leading-relaxed mb-6" />
            </section>

            {/* Section 12: Indemnification */}
            <section className="mb-8">
                <MarkdownText text={s12_indemnification.title} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={s12_indemnification.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownList items={s12_indemnification.listItems} />
            </section>

            {/* Section 13: Term Termination */}
            <section className="mb-8">
                <MarkdownText text={s13_termTermination.title} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={s13_termTermination.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownList items={s13_termTermination.listItems} />
            </section>

            {/* Section 14: Governing Law */}
            <section className="mb-8">
                <MarkdownText text={s14_governingLaw.title} className="text-2xl font-semibold text-gray-900 mb-4" />
                <div className="ml-4 space-y-6">
                    <div>
                        <MarkdownText text={s14_1_governingLaw.title} className="text-xl font-medium text-gray-800 mb-3" />
                        <MarkdownText text={s14_1_governingLaw.p1} className="text-base text-gray-700 leading-relaxed mb-4" />
                    </div>
                    <div>
                        <MarkdownText text={s14_2_informalResolution.title} className="text-xl font-medium text-gray-800 mb-3" />
                        <MarkdownText text={s14_2_informalResolution.p1} className="text-base text-gray-700 leading-relaxed mb-4" />
                    </div>
                    <div>
                        <MarkdownText text={s14_3_arbitration.title} className="text-xl font-medium text-gray-800 mb-3" />
                        <MarkdownText text={s14_3_arbitration.p1} className="text-base text-gray-700 leading-relaxed mb-4" />
                    </div>
                    <div>
                        <MarkdownText text={s14_4_classActionWaiver.title} className="text-xl font-medium text-gray-800 mb-3" />
                        <MarkdownText text={s14_4_classActionWaiver.p1} className="text-base text-gray-700 leading-relaxed mb-4" />
                    </div>
                </div>
            </section>

            {/* Section 15: International Users */}
            <section className="mb-8">
                <MarkdownText text={s15_internationalUsers.title} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={s15_internationalUsers.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownText text={s15_internationalUsers.p1} className="text-base text-gray-700 leading-relaxed mb-6" />
            </section>

            {/* Section 16: Terms Changes */}
            <section className="mb-8">
                <MarkdownText text={s16_termsChanges.title} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={s16_termsChanges.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownList items={s16_termsChanges.listItems} />
            </section>

            {/* Section 17: General Terms */}
            <section className="mb-8">
                <MarkdownText text={s17_generalTerms.title} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={s17_generalTerms.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
                <MarkdownList items={s17_generalTerms.listItems} />
            </section>

            {/* Section 18: Contact Us */}
            <section className="mb-8">
                <MarkdownText text={s18_contactUs.title} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={s18_contactUs.intro} className="text-base text-gray-700 leading-relaxed mb-4" />
                <div className="space-y-2">
                    {s18_contactInfo.map((info, index) => (
                        <div key={index} className="text-base text-gray-700 leading-relaxed">
                            <MarkdownText text={info} />
                        </div>
                    ))}
                </div>
            </section>

            {/* Section 19: Final Agreement */}
            <section className="mb-8">
                <MarkdownText text={s19_finalAgreement.title} className="text-2xl font-semibold text-gray-900 mb-4" />
                <MarkdownText text={s19_finalAgreement.p1} className="text-base text-gray-700 leading-relaxed mb-6" />
            </section>
        </div>
    );
};

export default Content;