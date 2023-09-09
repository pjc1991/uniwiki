import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import {resolve} from 'path'
// https://vitejs.dev/config/
export default defineConfig({
    base: '/static',
    server: {
        host: 'localhost',
        port: 3000,
        open: false,
        watch: {
            usePolling: true,
            disableGlobbing: false,
        }
    },
    build: {
        outDir: resolve('./static/dist'),
        manifest: true,
        emptyOutDir: true,
        target: 'es2015',
        rollupOptions: {
            input: {
                main: resolve('./src/main.js'),
            },
            output: {
                chunkFileNames: undefined,
            }
        },
        modulePreload: {
            polyfill: true,
        },

    },
    plugins: [vue()],
})
