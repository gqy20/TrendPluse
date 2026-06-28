import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

/**
 * 读取仓库根的 repos.json（监控仓库配置）。
 * 用 fileURLToPath + import.meta.url 解析项目外路径，规避 Vite import 限制。
 */
export interface RepoEntry {
  url: string;
  description?: string;
}

const REPOS_PATH = fileURLToPath(new URL('../../../repos.json', import.meta.url));

export function loadRepos(): RepoEntry[] {
  try {
    const raw = readFileSync(REPOS_PATH, 'utf-8');
    const data = JSON.parse(raw);
    return Array.isArray(data) ? (data as RepoEntry[]) : [];
  } catch {
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
