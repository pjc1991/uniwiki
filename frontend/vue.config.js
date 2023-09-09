const {defineConfig} = require('@vue/cli-service')
const BundleTracker = require('webpack-bundle-tracker')
const path = require('path')

console.log(__dirname)

module.exports = defineConfig({
    transpileDependencies: true,
    publicPath: process.env.NODE_ENV === 'production' ? '/' : 'http://localhost:8080/',
    outputDir: './assets/webpack_bundles',
    assetsDir: 'assets',
    lintOnSave: true,
    runtimeCompiler: true,
    configureWebpack: {},
    pages: {
        index: {
            entry: './src/main.js',
        }
    },
    chainWebpack: config => {
        config
            .optimization
            .splitChunks(false)
        config
            .devServer
            .host('0.0.0.0')
            .port(8080)
            .https(false)
            .headers({'Access-Control-Allow-Origin': ['\*']})
        config.plugin('BundleTracker')
            .use(BundleTracker, [{filename: '../webpack-stats.json'}])
            .tap(args => {
                return [{
                    path: __dirname, filename: 'webpack-stats.json'
                }]
            })

    },
})

