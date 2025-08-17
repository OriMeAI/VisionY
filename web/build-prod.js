const common = require("./webpack.config.prod");
const path = require("path");
const { merge } = require("webpack-merge");
const webpack = require("webpack");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const fs = require("fs");

function getConfigs(pages) {
  const configs = [];

  // Handle regular pages
  pages.forEach((page) => {
    if (page !== "home") {
      configs.push({
        entry: {
          index: path.resolve(__dirname, `./src/${page}.tsx`),
        },
        output: {
          path: path.resolve(__dirname, `./dist/${page}/`),
          publicPath: `/${page}/`,
        },
        plugins: [
          new HtmlWebpackPlugin({
            template: path.resolve(__dirname, `./src/${page}.html`),
            filename: "index.html",
            chunks: ["index"],
          }),
        ],
      });
    }
  });

  // Handle home page with multi-language support
  configs.push({
    entry: {
      index: path.resolve(__dirname, "./home/main.js"),
    },
    output: {
      path: path.resolve(__dirname, "./dist/home/"),
      publicPath: "/home/",
    },
    plugins: [
      // Multi-language HTML files
      ...["cn", "en", "tw", "ja"].map((lang) => 
        new HtmlWebpackPlugin({
          template: path.resolve(__dirname, `./home/${lang}.html`),
          filename: `${lang}.html`,
          chunks: ["index"],
        })
      ),
      // Copy static assets for home
      {
        apply: (compiler) => {
          compiler.hooks.afterEmit.tap("CopyHomeStaticPlugin", () => {
            const sourceDir = path.resolve(__dirname, "home/static");
            const destDir = path.resolve(__dirname, "dist/home/static");
            try {
              if (fs.existsSync(sourceDir)) {
                fs.mkdirSync(destDir, { recursive: true });
                fs.cpSync(sourceDir, destDir, { recursive: true });
                console.log(`Copied home/static to dist/home/static`);
              } else {
                console.warn(`Warning: home/static directory does not exist: ${sourceDir}`);
              }
            } catch (err) {
              console.error(`Failed to copy home/static: ${err}`);
            }
          });
        },
      },
    ],
  });

  return configs.map((config) => merge(common, config));
}

async function main() {
  function runCompiler(config) {
    return new Promise((resolve, reject) => {
      const compiler = webpack(config);

      console.log(`Starting build: ${config.output.path}`);

      compiler.run((err, stats) => {
        if (err) {
          console.error(`Build failed: ${config.output.path}`, err);
          reject(err);
          return;
        }

        if (stats.hasErrors()) {
          console.error(
            `Build errors: ${config.output.path}`,
            stats.toString({ colors: true })
          );
          reject(stats.toString());
          return;
        }

        console.log(`Build completed: ${config.output.path}`);

        compiler.close((closeErr) => {});
        resolve();
      });
    });
  }

  async function build(pages) {
    const batchSize = 1;
    const configs = getConfigs(pages);
    for (let i = 0; i < configs.length; i += batchSize) {
      const batch = configs.slice(i, i + batchSize);
      console.log(`Starting batch ${Math.floor(i / batchSize) + 1}`);
      for (const config of batch) {
        await runCompiler(config);
      }
      console.log(`Batch ${Math.floor(i / batchSize) + 1} completed`);
    }
  }

  await build([
    "home", // Add home to the pages list
    // "index",
    "login",
    "workspace",
    "aboutus",
    "project",
    "termsofuse",
    "privacypolicy",
    "usercenter",
    "share",
    "error",
  ]);

  // Copy favicon.ico to root directory
  const outputPath = path.resolve(__dirname, "./dist");
  const faviconSource = path.resolve(__dirname, "./favicon.ico");
  const faviconDest = path.resolve(outputPath, "favicon.ico");

  try {
    if (fs.existsSync(faviconSource)) {
      fs.copyFileSync(faviconSource, faviconDest);
      console.log(`Copied favicon.ico to: ${outputPath}`);
    } else {
      console.warn(`Warning: favicon.ico source file does not exist: ${faviconSource}`);
    }
  } catch (copyErr) {
    console.error(`Failed to copy favicon.ico: ${copyErr}`);
  }
}

main();