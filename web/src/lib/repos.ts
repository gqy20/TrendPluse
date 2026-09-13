import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import process from 'node:process';

/**
 * 读取仓库根的 repos.json（监控仓库配置）。
 * Astro 7（rolldown-vite）打包后 import.meta.url 不再指向源码路径，
 * 改用 process.cwd()（dev/build 均从 web/ 目录启动）向上定位项目根。
 */
export interface RepoEntry {
  url: string;
  description?: string;
}

const REPOS_PATH = resolve(process.cwd(), '../repos.json');

export function loadRepos(): RepoEntry[] {
  try {
    const raw = readFileSync(REPOS_PATH, 'utf-8');
    const data = JSON.parse(raw);
    return Array.isArray(data) ? (data as RepoEntry[]) : [];
  } catch (err) {
    console.warn(`[repos] 读取 ${REPOS_PATH} 失败：`, err);
    return [];
  }
}

export interface ParsedRepo extends RepoEntry {
  /** owner/repo 形式，如 anthropics/claude-code */
  full: string;
  owner: string;
  repo: string;
}

export function parseRepo(r: RepoEntry): ParsedRepo {
  const m = r.url.match(/github\.com\/([^/]+\/[^/]+)/);
  const full = m?.[1] || r.url;
  const [owner, repo] = full.split('/');
  return { ...r, full, owner, repo };
}

/** 按 owner 分组并按组内数量降序 */
export function groupReposByOwner(repos: RepoEntry[]): [string, ParsedRepo[]][] {
  const groups = new Map<string, ParsedRepo[]>();
  for (const r of repos) {
    const p = parseRepo(r);
    if (!groups.has(p.owner)) groups.set(p.owner, []);
    groups.get(p.owner)!.push(p);
  }
  return [...groups.entries()].sort((a, b) => b[1].length - a[1].length);
}
