const path = require("path");

const resolvePath = relPath => path.resolve(__dirname, relPath);

const list_react_file = resolvePath("./src/List.jsx");
const outputDir = resolvePath("../static/");

const bundleName = "js/[name].js";
const imgName = "img/[name].[ext]";

module.exports = {
  entry: {
    list: list_react_file,
  },
  output: {
    path: outputDir,
    filename: bundleName,
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-react"],
          },
        },
      },
      {
        test: /\.(png|jpe?g|gif)$/,
        use: [
          {
            loader: "file-loader",
            options: {
              name: imgName,
              publicPath: "/static",
            },
          },
        ],
      },
    ],
  },
};
