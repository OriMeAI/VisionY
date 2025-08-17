// import '../src/globals.css';
import './styles.css'; 
import Choices from 'choices.js';
import 'choices.js/public/assets/styles/choices.min.css';

// 支持的语言列表及其对应的文件名。这个表格需要完善各种语言
const LANGUAGE_KEY = 'language';
const SUPPORTED_LANGUAGES = {
    'en-US': { value: 'en', label: 'English' },
    'zh-CN': { value: 'cn', label: '简体中文' },
    'zh-TW': { value: 'tw', label: '繁體中文' },
    'ja-JP': { value: 'ja', label: '日本語' },
};

const savedLanguage = localStorage.getItem(LANGUAGE_KEY);
// const currentValue = savedLanguage ? SUPPORTED_LANGUAGES[savedLanguage]?.value : 'en';

const languageOptions = Object.entries(SUPPORTED_LANGUAGES).map(
  ([key, { value, label }]) => ({
    value,
    label,
    selected: key === savedLanguage,
  })
);


document.addEventListener('DOMContentLoaded', function() {
    // 设置页脚年份
    const currentYearElement = document.getElementById('currentYear');
    if (currentYearElement) {
        // const startYear = 2023;
        const currentYear = new Date().getFullYear();
        // const yearDisplay = startYear === currentYear ? currentYear : `${startYear}-${currentYear}`;
        currentYearElement.textContent = currentYear;
    }

    // 移动端导航切换
    const mobileNavToggle = document.querySelector('.mobile-nav-toggle');
    const navLinksMobile = document.querySelector('.nav-links-mobile');

    if (mobileNavToggle && navLinksMobile) {
        mobileNavToggle.addEventListener('click', () => {
            navLinksMobile.classList.toggle('hidden');
            navLinksMobile.classList.toggle('flex'); // 使用 flex 来显示，因为它是 flex-col
            mobileNavToggle.innerHTML = navLinksMobile.classList.contains('hidden') ? '☰' : '✕';
        });
    }

    // 桌面版语言选择器
    const languageSelector = document.getElementById('language-selector');
    if (languageSelector) {
        const desktopChoices = new Choices(languageSelector, {
            choices: languageOptions,
            searchEnabled: false,
            itemSelectText: '',
            shouldSort: false,
            classNames: { // 自定义 CSS 类名
                containerOuter: 'choices',
                containerInner: 'choices__inner',
                input: 'choices__input', 
                listDropdown: 'choices__list--dropdown',
                itemSelectable: 'choices__item--selectable',
                listSingle: 'choices__list--single', // 确保这个类名被 Choices.js 使用
                item: 'choices__item' // 确保这个类名被 Choices.js 使用
            },
        });
        
        // 添加语言切换功能
        languageSelector.addEventListener('change', function(e) {
            // 获取选中的语言文件名
            const selectedValue = e.target.value;
            
            // 遍历 SUPPORTED_LANGUAGES 查找对应的语言代码
            for (const [langCode, langInfo] of Object.entries(SUPPORTED_LANGUAGES)) {
                if (langInfo.value === selectedValue) {
                    // 如果找到了对应的语言代码，则保存到 localStorage
                    localStorage.setItem(LANGUAGE_KEY, langCode);
                    // 重定向到选中的语言页面
                    window.location.href = selectedValue;
                    break;
                }
            }
        });
    }    

    // 移动版语言选择器
    const mobileLanguageSelector = document.getElementById('mobile-language-selector');
    if (mobileLanguageSelector) {
        const mobileChoices = new Choices(mobileLanguageSelector, {
            choices: languageOptions,
            searchEnabled: false,
            itemSelectText: '',
            shouldSort: false,
            classNames: { // 自定义 CSS 类名
                containerOuter: 'choices',
                containerInner: 'choices__inner',
                input: 'choices__input', 
                listDropdown: 'choices__list--dropdown',
                itemSelectable: 'choices__item--selectable',
                listSingle: 'choices__list--single', // 确保这个类名被 Choices.js 使用
                item: 'choices__item', // 确保这个类名被 Choices.js 使用
            },
        });
        
        // 添加语言切换功能
        mobileLanguageSelector.addEventListener('change', function(e) {
            // 获取选中的语言文件名
            const selectedValue = e.target.value;
            
            // 遍历 SUPPORTED_LANGUAGES 查找对应的语言代码
            for (const [langCode, langInfo] of Object.entries(SUPPORTED_LANGUAGES)) {
                if (langInfo.value === selectedValue) {
                    // 如果找到了对应的语言代码，则保存到 localStorage
                    localStorage.setItem(LANGUAGE_KEY, langCode);
                    // 重定向到选中的语言页面
                    window.location.href = selectedValue;
                    break;
                }
            }
        });
    }

    // 添加关闭动画
    function addCloseAnimation(selector) {
        const element = document.querySelector(selector);
        if (!element) return;
        
        element.addEventListener('hideDropdown', function(event) {
            const dropdown = event.target.querySelector('.choices__list--dropdown');
            if (dropdown && dropdown.classList.contains('is-active')) {
                dropdown.classList.add('choices-dropdown-closing');
                setTimeout(() => {
                    dropdown.classList.remove('choices-dropdown-closing');
                }, 200); // 动画持续时间
            }
        });
    }
    
    // 为两个选择器都添加动画
    addCloseAnimation('#language-selector');
    addCloseAnimation('#mobile-language-selector');

    // 滚动动画逻辑
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    const observerOptions = {
        root: null, // 相对于视口
        rootMargin: '0px',
        threshold: 0.1 // 元素10%可见时触发
    };

    const observer = new IntersectionObserver((entries, observerInstance) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // 添加 'is-visible' 类来触发动画
                entry.target.classList.add('is-visible');
                // 可选: 动画触发后停止观察该元素，以提高性能
                //observerInstance.unobserve(entry.target);
            } else {
                // 可选: 如果希望元素在移出视口时重置动画，则移除类
                entry.target.classList.remove('is-visible');
            }
        });
    }, observerOptions);

    animatedElements.forEach(el => {
        observer.observe(el);
    });
});