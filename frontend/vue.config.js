const {defineConfig} = require('@vue/cli-service')
const BundleTracker = require('webpack-bundle-tracker')
const path = require('path')
module.exports = defineConfig({
    transpileDependencies: true,
    publicPath: process.env.NODE_ENV === 'production' ? '/' : '/',
    outputDir: '../static/webpack_bundles',
    assetsDir: 'assets',
    indexPath: 'index.html',
    lintOnSave: true,
    runtimeCompiler: true,
    configureWebpack: {},
    pages: {
        index: 'src/main.js'
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
