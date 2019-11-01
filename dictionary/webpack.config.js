const path = require('path'); 

module.exports = { 
  mode: "development",
  entry: './src/dictionary/index.tsx',
  output: { 
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'static/dictionary/'),
  },
  module:{
    rules: [ 
      {
        test: /\.tsx$/,
        loader: 'babel-loader',
      },
      {
        test: /\.js$/,
        loader: 'source-map-loader',
      },
    ],
  },
  devtool: 'inline-source-map',
  resolve: {
    extensions: ['.tsx', '.ts', '.js']
  },
  watch: true,
};
