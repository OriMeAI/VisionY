const path = require('path');
const TerserPlugin = require('terser-webpack-plugin');
const CompressionPlugin = require('compression-webpack-plugin');
const ForkTsCheckerWebpackPlugin = require('fork-ts-checker-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin'); // 添加这一行
const dotenv = require('dotenv');
const webpack = require('webpack');

// 读取自定义环境变量文件
const env = dotenv.config({ path: path.resolve(__dirname, '.env') }).parsed;

// 转换成 Webpack 需要的 { "process.env.KEY": JSON.stringify(value) } 格式
const envKeys = Object.keys(env).reduce((prev, next) => {
  prev[`process.env.${next}`] = JSON.stringify(env[next]);
  return prev;
}, {});

module.exports = {
    // devtool: 'source-map',
    cache: false, // 禁用缓存
    output: {
      path: path.resolve(__dirname, 'dist'), // 明确指定输出路径
      filename: 'static/js/[name].[contenthash].bundle.js',
      chunkFilename: 'static/js/[name].[contenthash].bundle.js',
      clean: true,
    },
    performance: {
      hints: 'warning',
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
          use: [MiniCssExtractPlugin.loader, 'css-loader', 'postcss-loader'], // 替换 style-loader
        },
        {
          test: /\.module\.css$/,
          use: [
            // 'style-loader',
            MiniCssExtractPlugin.loader, // 替换 style-loader
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
                outputPath: 'static/assets/',
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
      // 提取 CSS 到单独的文件
      new MiniCssExtractPlugin({
        filename: 'static/css/[name].[contenthash].css',
        chunkFilename: 'static/css/[name].[contenthash].css',
      }),
      // new CompressionPlugin({
      //   algorithm: 'gzip',
      //   test: /\.(js|css|html|svg)$/,
      //   threshold: 10240,
      //   minRatio: 0.8,
      // }),
      new ForkTsCheckerWebpackPlugin({
        typescript: {
          configFile: path.resolve(__dirname, 'tsconfig.json'),
          diagnosticOptions: {
            semantic: true,
            syntactic: true,
          },
        },
      }),
    ],
    // ignoreWarnings: [/Critical dependency: the request of a dependency is an expression/],
    optimization: {
      minimize: true,
      minimizer: [
        new TerserPlugin({
          terserOptions: {
            compress: { drop_console: true, unused: true },
            mangle: true,
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
            test: /[\\/]node_modules[\\/]/,
            name: 'vendors',
            chunks: 'all',
            priority: 10,
            enforce: true,
          }
          // vendors: {
          //   test: (module) => {
          //     const moduleName = module.context || '';
          //     return (
          //       /[\\/]node_modules[\\/]/.test(moduleName) &&
          //       !/@ant-design[\\/]icons/.test(moduleName) &&
          //       !/antd/.test(moduleName) &&
          //       !/konva/.test(moduleName) &&
          //       !/lodash/.test(moduleName) &&
          //       !/(react|react-dom|react-router-dom|@react-[a-zA-Z0-9-]*[\\/])/.test(moduleName) &&
          //       !/xlsx/.test(moduleName)
          //     );
          //   },
          //   name: 'vendors',
          //   chunks: 'all',
          //   priority: 10,
          // },
        },
      },
    }
  
};