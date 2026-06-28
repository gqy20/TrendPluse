// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

// TrendPulse 前端配置
// 部署在 GitHub Pages 项目子路径 https://gqy20.github.io/TrendPluse/
// 因此必须显式声明 site + base，否则资源/链接 404
export default defineConfig({
  site: 'https://gqy20.github.io',
  base: '/TrendPluse/',
  vite: {
    plugins: [tailwindcss()],
  },
});
