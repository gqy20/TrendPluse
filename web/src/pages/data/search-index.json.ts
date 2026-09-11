import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { loadRepos } from '../../lib/repos';
import { BASE } from '../../lib/path';

/**
 * 构建期生成静态搜索索引(信号 / 仓库 / 项目)。
 * 只保留检索与跳转所需字段,控制体积。
 */
export const GET: APIRoute = async () => {
  const daily = (await getCollection('daily')).sort((a, b) => b.id.localeCompare(a.id));

  const signals = daily
    .slice(0, 90) // 最近 90 天
    .flatMap((e) => {
      const date = e.id.replace(/^report-/, '');
      const href = `${BASE}reports/daily/${date}/`;
      return [
        ...e.data.engineering_signals,
        ...e.data.research_signals,
        ...e.data.commit_signals,
        ...e.data.release_signals,
      ].map((s) => ({
        t: s.title,
        r: s.related_repos[0] ?? '',
        d: date,
        h: href,
        i: s.impact_score ?? 0,
      }));
    });

  const repos = loadRepos().map((r) => {
    const full = r.url.match(/github\.com\/([^/]+\/[^/]+)/)?.[1] ?? r.url;
    return { t: full, r: full, d: '', h: r.url, i: 0 };
  });

  const discovery = await getCollection('discovery');
  const projects = (discovery[discovery.length - 1]?.data.candidates ?? [])
    .slice(0, 120)
    .map((p) => ({
      t: p.name || p.repo,
      r: p.repo,
      d: '',
      h: `https://github.com/${p.repo}`,
      i: 0,
    }));

  return new Response(
    JSON.stringify({
      updated: daily[0]?.data.date ?? '',
      signals,
      repos,
      projects,
    }),
    { headers: { 'Content-Type': 'application/json' } }
  );
};
