
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js,ts,jsx,tsx}",
    './home/**/*.{html,js}', // 新首页文件
  ],
  theme: {
    extend: {
      screens: {
        'custom': '1050px',
        '3xl': '1920px',
        '4xl': '2560px',
        '5xl': '3440px',
        '6xl': '3840px',
      },
      colors: {
        primary: "#7E2FFF",//"#7f56d9",
        background: "var(--background)",
        foreground: "var(--foreground)",
        'custom-purple': '#7E2FFF',
        //这些事首页需要的配色
        'primary-darker': '#6a48b8',
        secondary: '#50E3C2',
        accent: '#FFC107',
        'brand-dark': '#2c3e50',
        'brand-light': '#f8f9fa',
        'brand-text': '#34495e',
      },
      borderColor: {
        primary: "#7E2FFF",
      },
      animation: {
        marquee: 'marquee 25s linear infinite',
        marquee2: 'marquee2 25s linear infinite',
      },
      keyframes: {
        marquee: {
          '0%': { transform: 'translateX(0%)' },
          '100%': { transform: 'translateX(-100%)' },
        },
        marquee2: {
          '0%': { transform: 'translateX(100%)' },
          '100%': { transform: 'translateX(0%)' },
        },
      },
    },
  },
  plugins: [],
};
