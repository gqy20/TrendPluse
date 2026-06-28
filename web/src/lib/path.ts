/**
 * 路径工具：站点部署在 GitHub Pages 子路径 /TrendPluse/，
 * 所有内部绝对链接必须拼上 BASE 前缀，否则跳转 404。
 */
export const BASE: string = import.meta.env.BASE_URL; // 形如 '/TrendPluse/'

/** 将根相对路径（如 '/reports/'）转为带 base 前缀的绝对路径 */
export function abs(p: string): string {
  const clean = p.replace(/^\//, '');
  // 避免重复拼接
  if (clean.startsWith(BASE.replace(/^\//, ''))) return `${BASE}${clean.slice(BASE.replace(/^\//,'').length)}`.replace(/\/$/, '') || BASE;
  return `${BASE}${clean}`;
}

/** 报告路由生成辅助 */
export const routes = {
  home: () => abs('/'),
  reports: () => abs('/reports/'),
  daily: (date: string) => abs(`/reports/daily/${date}/`),
  weekly: (week: string) => abs(`/reports/weekly/${week}/`),
  discovery: () => abs('/discovery/'),
  discoveryReport: (date: string) => abs(`/discovery/${date}/`),
  repos: () => abs('/repos/'),
};
