const {defineConfig} = require('@vue/cli-service')
const BundleTracker = require('webpack-bundle-tracker')
const path = require('path')
module.exports = defineConfig({
    transpileDependencies: true,
    publicPath: process.env.NODE_ENV === 'production' ? '/' : '/',
    outputDir: '../static',
    assetsDir: 'assets',
    indexPath: '../templates/wiki/app.html',
    lintOnSave: true,
    runtimeCompiler: true,
    configureWebpack: {},
    chainWebpack: config => {
        config
            .plugin('BundleTracker')
            .use(BundleTracker, [{filename: '../webpack-stats.json'}])
            .tap(args => {
                return [{
                    path: __dirname, filename: 'webpack-stats.json'
                }]
            })
    },
})
