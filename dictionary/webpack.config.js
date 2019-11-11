path = require ('path') 
module.exports = {
  mode: "development",
  entry: './src/dictionary/index.tsx',
  output: {
    filename: './bundle.js',
    path: path.resolve (__dirname, 'static', 'dictionary'),
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        exclude: /node_modules/,
        use: [ { loader: "ts-loader" } ]
      },
      {
        test: /\.tsx?/,
        enforce: "pre",
        exclude: /node_modules/,
        loader: "eslint-loader",
        options: {
          "cache": true,
        },
      },
      {
        test: /\.css/,
        loader:["style-loader", "css-loader" ]
      },
      // all output '.js' files will have any sourcemaps re-processed by 'source-map-loader'.
      {
        test: /\.js$/,
        enforce: "pre",
        loader: "source-map-loader"
      },
    ]
  },
  resolve: {
    extensions: [".ts", ".tsx", '.js']
  },
  devtool: "inline-source-map",
  devServer: {
    contentBase: path.resolve (__dirname, 'static','dictionary'),
    port: 9000,
    hot: true,
    writeToDisk: true
  },
};
