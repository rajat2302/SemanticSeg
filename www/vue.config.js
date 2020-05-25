const path = require('path');

module.exports = {
    assetsDir: '../static',
    publicPath: '',
    outputDir: path.resolve(__dirname, '../templates'),
    runtimeCompiler: undefined,
    productionSourceMap: undefined,
    parallel: undefined,
    css: undefined,
    transpileDependencies: [ 'vuetify' ],
};
