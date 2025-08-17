const HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path');
const TerserPlugin = require('terser-webpack-plugin');
const CompressionPlugin = require('compression-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');
const ForkTsCheckerWebpackPlugin = require('fork-ts-checker-webpack-plugin');
const dotenv = require('dotenv');
const webpack = require('webpack');

module.exports = () => {
  const isProduction = false;

  // 读取自定义环境变量文件
  const env = dotenv.config({ path: path.resolve(__dirname, '.env') }).parsed;

  // 转换成 Webpack 需要的 { "process.env.KEY": JSON.stringify(value) } 格式
  const envKeys = Object.keys(env).reduce((prev, next) => {
    prev[`process.env.${next}`] = JSON.stringify(env[next]);
    return prev;
  }, {});

  return {
    mode: 'development',
    entry: {
      home: './home/main.js', // 新首页入口
      // index: './src/index.tsx',
      workspace: './src/workspace.tsx',
      aboutus: './src/aboutus.tsx',
      termsofuse: './src/termsofuse.tsx',
      privacypolicy: './src/privacypolicy.tsx',
      usercenter: './src/usercenter.tsx',
      project: './src/project.tsx',
      share: './src/share.tsx',
      login: './src/login.tsx',
      error: './src/error.tsx',
    },
    output: {
      path: path.resolve(__dirname, 'dist/'),
      filename: '[name]/index.[contenthash].bundle.js',
      publicPath: '/',
      chunkFilename: '[name]/chunk.[contenthash].bundle.js',
      clean: true,
    },
    performance: {
      hints: isProduction ? 'error' : false,
      maxEntrypointSize: 2 * 512000,
      maxAssetSize: 512000,
    },
    resolve: {
      alias: {
        '@src': path.resolve(__dirname, 'src/'),
        '@components': path.resolve(__dirname, 'src/components/'),
        '@assets': path.resolve(__dirname, 'assets/'),
        'lodash-es': 'lodash',
      },
      extensions: ['.js', '.jsx', '.ts', '.tsx'],
    },
    module: {
      rules: [
        {
          test: /\.(js|jsx|ts|tsx)$/,
          exclude: /node_modules/,
          use: {
            loader: 'babel-loader',
            options: {
              configFile: path.resolve(__dirname, 'babel.config.json'),
            },
          },
        },
        {
          test: /\.css$/,
          exclude: /\.module\.css$/,
          // use: ['style-loader', 'css-loader', 'postcss-loader'],
          use: [isProduction ? MiniCssExtractPlugin.loader : 'style-loader', 'css-loader', 'postcss-loader'], // 替换 style-loader
        },
        {
          test: /\.module\.css$/,
          use: [
            // 'style-loader',
            isProduction ? MiniCssExtractPlugin.loader : 'style-loader', // 替换 style-loader
            {
              loader: 'css-loader',
              options: {
                importLoaders: 1,
                modules: {
                  namedExport: false,
                  localIdentName: '[name]__[local]___[hash:base64:5]',
                },
              },
            },
            'postcss-loader',
          ],
        },
        {
          test: /\.(png|svg|jpg|jpeg|gif)$/i,
          use: [
            {
              loader: 'file-loader',
              options: {
                name: '[name].[ext]',
                outputPath: 'images/',
              },
            },
          ],
        },
        {
          test: /\.md$/,
          use: ['raw-loader'],
        },
        {
          test: /\.(mp4)$/,
          use: [
            {
              loader: 'url-loader',
              options: { limit: 8192 },
            },
            {
              loader: 'file-loader',
              options: {
                name: '[name].[ext]',
                outputPath: 'videos/',
              },
            },
          ],
        },
        {
          test: /\.docx$/,
          use: [
            {
              loader: 'file-loader',
              options: {
                name: '[name].[ext]',
                outputPath: 'documents/',
              },
            },
          ],
        },
      ],
    },
    plugins: [
      //环境变量
      new webpack.DefinePlugin(envKeys),
      //多语言页面开始
      // 多语言 HTML 文件，输出到 home/{lang}.html
      new HtmlWebpackPlugin({
        template: './home/cn.html',
        filename: 'home/cn.html',
        chunks: ['home'],
      }),
      new HtmlWebpackPlugin({
          template: './home/en.html',
          filename: 'home/en.html',
          chunks: ['home'],
      }),
      new HtmlWebpackPlugin({
          template: './home/ja.html',
          filename: 'home/ja.html',
          chunks: ['home'],
      }),
      new HtmlWebpackPlugin({
          template: './home/tw.html',
          filename: 'home/tw.html',
          chunks: ['home'],
      }),
      //多语言页面结束

      // new HtmlWebpackPlugin({
      //   template: './src/index.html',
      //   filename: 'index/index.html',
      //   chunks: ['index'],
      // }),
      new HtmlWebpackPlugin({
        template: './src/workspace.html',
        filename: 'workspace/index.html',
        chunks: ['workspace'],
      }),
      new HtmlWebpackPlugin({
        template: './src/aboutus.html',
        filename: 'aboutus/index.html',
        chunks: ['aboutus'],
      }),
      new HtmlWebpackPlugin({
        template: './src/termsofuse.html',
        filename: 'termsofuse/index.html',
        chunks: ['termsofuse'],
      }),
      new HtmlWebpackPlugin({
        template: './src/privacypolicy.html',
        filename: 'privacypolicy/index.html',
        chunks: ['privacypolicy'],
      }),
      new HtmlWebpackPlugin({
        template: './src/usercenter.html',
        filename: 'usercenter/index.html',
        chunks: ['usercenter'],
      }),
      new HtmlWebpackPlugin({
        template: './src/error.html',
        filename: 'error/index.html',
        chunks: ['error'],
      }),
      new HtmlWebpackPlugin({
        template: './src/project.html',
        filename: 'project/index.html',
        chunks: ['project'],
      }),
      new HtmlWebpackPlugin({
        template: './src/share.html',
        filename: 'share/index.html',
        chunks: ['share'],
      }),
      new HtmlWebpackPlugin({
        template: './src/login.html',
        filename: 'login/index.html',
        chunks: ['login'],
      }),
      // 复制静态资源到 home/static/
      new CopyWebpackPlugin({
        patterns: [
            { from: './favicon.ico', to: 'favicon.ico' },
            {
              from: path.resolve(__dirname, 'home/static'),
              to: path.resolve(__dirname, 'dist/home/static'),
            },
        ],
      }),
      new MiniCssExtractPlugin({
        filename: '[name]/[name].[contenthash].css',
        chunkFilename: '[name]/[name].[contenthash].css'
      }),
      new ForkTsCheckerWebpackPlugin({
        typescript: {
          configFile: path.resolve(__dirname, 'tsconfig.json'),
          diagnosticOptions: {
            semantic: true,
            syntactic: true,
          },
        },
      }),
      // 只在生产环境中启用压缩插件
      ...(isProduction ? [
        new CompressionPlugin({
          algorithm: 'gzip',
          test: /\.(js|css|html|svg)$/,
          threshold: 10240,
          minRatio: 0.8,
        }),
      ] : []),
      // new BundleAnalyzerPlugin({ analyzerMode: 'static', reportFilename: 'bundle-report.html', openAnalyzer: true }),
    ],
    devServer: {
      static: {
        directory: path.join(__dirname, 'dist'),
        publicPath: '/',
      },
      devMiddleware: {
        writeToDisk: false,
      },
      compress: true,
      port: 8080,
      hot: 'only',
      liveReload: false,
      historyApiFallback: {
        verbose: true, // 开启日志，查看重定向详情
        rewrites: [
          {
            // from: /^\/home\/(cn|en|tw|ja)(\/.*)?$/,
            from: /^\/(cn|en|tw|ja)(\/.*)?$/,
            to: function (context) {
              const lang = context.match[1]; // 捕获组 $1，即 cn、en、tw 或 ja
              return `/home/${lang}.html`;
            },
          },
          { from: /^\/$/, to: '/home/en.html' },
          { from: /^\/workspace(\/.*)?(\?.*)?$/, to: '/workspace/index.html' },
          { from: /^\/project\/.*/, to: '/project/index.html' },
          { from: /^\/share(\/.*)?(\?.*)?$/, to: '/share/index.html' },
          { from: /^\/aboutus/, to: '/aboutus/index.html' },
          { from: /^\/termsofuse/, to: '/termsofuse/index.html' },
          { from: /^\/privacypolicy/, to: '/privacypolicy/index.html' },
          { from: /^\/usercenter/, to: '/usercenter/index.html' },
          { from: /^\/login/, to: '/login/index.html' },
          { from: /./, to: '/error/index.html' },
        ],
      },
    },
    ignoreWarnings: [/Critical dependency: the request of a dependency is an expression/],
    optimization: {
      minimize: isProduction,
      minimizer: [
        new TerserPlugin({
          terserOptions: {
            compress: { drop_console: isProduction, unused: true },
            mangle: isProduction,
          },
        }),
      ],
      splitChunks: {
        chunks: 'all',
        cacheGroups: {
          antd: { test: /[\\/]node_modules[\\/]antd[\\/]/, name: 'antd', priority: 20, enforce: true },
          antDesignIcons: {
            test: /[\\/]node_modules[\\/]@ant-design[\\/]icons[\\/]/,
            name: 'ant-design-icons',
            priority: 25,
            enforce: true,
          },
          konva: { test: /[\\/]node_modules[\\/]konva[\\/]/, name: 'konva', priority: 20, enforce: true },
          lodash: { test: /[\\/]node_modules[\\/]lodash[\\/]/, name: 'lodash', priority: 20, enforce: true },
          react: {
            test: /[\\/]node_modules[\\/](react|react-dom|react-router-dom|@react-[a-zA-Z0-9-]*[\\/])/,
            name: 'react-vendors',
            priority: 25,
            enforce: true,
          },
          xlsx: { test: /[\\/]node_modules[\\/]xlsx[\\/]/, name: 'xlsx', priority: 20, enforce: true },
          vendors: {
            test: (module) => {
              const moduleName = module.context || '';
              return (
                /[\\/]node_modules[\\/]/.test(moduleName) &&
                !/@ant-design[\\/]icons/.test(moduleName) &&
                !/antd/.test(moduleName) &&
                !/konva/.test(moduleName) &&
                !/lodash/.test(moduleName) &&
                !/(react|react-dom|react-router-dom|@react-[a-zA-Z0-9-]*[\\/])/.test(moduleName) &&
                !/xlsx/.test(moduleName)
              );
            },
            name: 'vendors',
            chunks: 'all',
            priority: 10,
          },
        },
      },
    },
  }
};