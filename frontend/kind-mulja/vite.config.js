import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { VitePWA } from 'vite-plugin-pwa'

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    port: 5173,
    host: '0.0.0.0'
  },
  proxy: {
    // socket.io 프락시 설정
    '/socket': {
      target: 'http://j10c109.p.ssafy.io:12002', // HTTP로 통신
      changeOrigin: true, // 원본 헤더를 변경하여 대상 호스트를 목적지로 사용하도록 설정
      ws: true // WebSocket 프록시 활성화
    }
  },
  plugins: [
    vue(),
    VitePWA({
      registerType: 'autoUpdate',
      devOptions: {
        enabled: true
      },
      injectRegister: 'auto',
      manifest: {
        name: '친절한 물자씨',
        short_name: 'Mr.Mulja',
        theme_color: '#111111',
        display: 'standalone',
        icons: [
          {
            src: '/icons/icon-192.png',
            type: 'image/png',
            sizes: '192x192'
          },
          {
            src: '/icons/icon-192-maskable.png',
            type: 'image/png',
            sizes: '192x192',
            purpose: 'maskable'
          },
          {
            src: '/icons/icon-512.png',
            type: 'image/png',
            sizes: '512x512'
          },
          {
            src: '/icons/icon-512-maskable.png',
            type: 'image/png',
            sizes: '512x512',
            purpose: 'maskable'
          }
        ]
      }
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
