import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

/**
 * Content Layer：直接读取仓库根的 reports/ 目录下的 JSON 数据源。
 *
 * 这是「JSON 驱动渲染」架构的核心——Astro 构建时直接消费 Python 生成的
 * 结构化报告，彻底取代旧的「md 同步到 docs + 正则解析生成索引」易碎中间层。
 *
 * zod schema 同时承担「校验」与「TypeScript 类型源」双重职责。
 * 历史报告字段不全（早期数据缺 summary_brief 等），故所有展示字段给默认值、
 * 数值字段接受 null，确保任何一份异常数据都不会阻断整体构建。
 * 路由用 entry.id（文件名 derive），不依赖 data.date。
 */

const signalSchema = z.object({
  id: z.string().catch(''),
  title: z.string().catch(''),
  type: z.string().catch(''),
  category: z.string().catch(''),
  impact_score: z.coerce.number().nullish(),
  why_it_matters: z.string().catch(''),
  sources: z.array(z.string()).default([]),
  related_repos: z.array(z.string()).default([]),
  source_signal_ids: z.array(z.string()).default([]),
});

const repoActivitySchema = z
  .object({
    repo: z.string().catch(''),
    commits: z.coerce.number().nullish(),
    top_contributors: z.array(z.string()).default([]),
  })
  .passthrough();

const dailySchema = z
  .object({
    date: z.string().catch(''),
    summary_brief: z.string().catch(''),
    engineering_signals: z.array(signalSchema).default([]),
    research_signals: z.array(signalSchema).default([]),
    commit_signals: z.array(signalSchema).default([]),
    release_signals: z.array(signalSchema).default([]),
    stats: z.record(z.string(), z.unknown()).default({}),
    activity: z
      .object({
        total_commits: z.coerce.number().nullish(),
        active_repos_count: z.coerce.number().nullish(),
        top_repos: z.array(repoActivitySchema).default([]),
      })
      .passthrough()
      .nullish(),
    releases: z.record(z.string(), z.unknown()).nullish(),
    breaking_changes: z.unknown().nullish(),
    monitored_repos: z.array(z.string()).default([]),
    issue_insights: z.record(z.string(), z.unknown()).nullish(),
    top_new_trends: z.array(z.string()).default([]),
    top_continuing_trends: z.array(z.string()).default([]),
    historical_basis_dates: z.array(z.string()).default([]),
    summary_confidence: z.coerce.number().nullish(),
    trend_status: z.string().nullish(),
  })
  .passthrough();

const coreTrendSchema = z
  .object({
    title: z.string().catch(''),
    theme: z.string().catch(''),
    description: z.string().catch(''),
    signal_ids: z.array(z.string()).default([]),
    impact_level: z.coerce.number().nullish(),
  })
  .passthrough();

const weeklySchema = z
  .object({
    week_id: z.string().catch(''),
    start_date: z.string().catch(''),
    end_date: z.string().catch(''),
    summary_brief: z.string().catch(''),
    core_trends: z.array(coreTrendSchema).default([]),
    engineering_signals: z.array(signalSchema).default([]),
    research_signals: z.array(signalSchema).default([]),
    daily_reports_count: z.coerce.number().nullish(),
    total_prs_analyzed: z.coerce.number().nullish(),
    high_impact_signals: z.coerce.number().nullish(),
    total_commits: z.coerce.number().nullish(),
    total_releases: z.coerce.number().nullish(),
    weekly_activity: z
      .object({
        total_commits: z.coerce.number().nullish(),
        active_repos_count: z.coerce.number().nullish(),
        top_repos: z.array(repoActivitySchema).default([]),
      })
      .passthrough()
      .nullish(),
  })
  .passthrough();

const discoveredProjectSchema = z
  .object({
    repo: z.string().catch(''),
    name: z.string().catch(''),
    description: z.string().catch(''),
    stars: z.coerce.number().nullish(),
    stars_growth_7d: z.coerce.number().nullish(),
    stars_growth_30d: z.coerce.number().nullish(),
    language: z.string().catch(''),
    topics: z.array(z.string()).default([]),
    license: z.string().catch(''),
    open_issues: z.coerce.number().nullish(),
    forks: z.coerce.number().nullish(),
    watchers: z.coerce.number().nullish(),
    last_commit_at: z.string().catch(''),
    quality_score: z.coerce.number().nullish(),
    activity_level: z.string().catch(''),
    community_score: z.coerce.number().nullish(),
    discovery_source: z.string().catch(''),
    discovery_reason: z.string().catch(''),
    recommended: z.boolean().nullish(),
    recommendation_priority: z.string().catch(''),
    highlight: z.record(z.string(), z.unknown()).nullish(),
  })
  .passthrough();

const discoverySchema = z
  .object({
    date: z.string().catch(''),
    total_discovered: z.coerce.number().nullish(),
    passed_quality: z.coerce.number().nullish(),
    high_priority: z.coerce.number().nullish(),
    duplicates_removed: z.coerce.number().nullish(),
    already_monitored: z.coerce.number().nullish(),
    candidates: z.array(discoveredProjectSchema).default([]),
  })
  .passthrough();

const daily = defineCollection({
  loader: glob({ pattern: 'report-*.json', base: '../reports/daily' }),
  schema: dailySchema,
});

const weekly = defineCollection({
  loader: glob({ pattern: 'weekly-*.json', base: '../reports/weekly' }),
  schema: weeklySchema,
});

// discovery 目录有 3 类 JSON：主报告 / -actionable / -bridge-result
// 只读主报告（discovery-YYYY-MM-DD.json），用精确字符通配排除衍生文件
const discovery = defineCollection({
  loader: glob({ pattern: 'discovery-????-??-??.json', base: '../reports/discovery' }),
  schema: discoverySchema,
});

export const collections = { daily, weekly, discovery };

// 导出类型别名，供组件直接 import 使用
export type Signal = z.infer<typeof signalSchema>;
export type CoreTrend = z.infer<typeof coreTrendSchema>;
export type DiscoveredProject = z.infer<typeof discoveredProjectSchema>;
export type DailyReport = z.infer<typeof dailySchema>;
export type WeeklyReport = z.infer<typeof weeklySchema>;
export type DiscoveryReport = z.infer<typeof discoverySchema>;
export type RepoActivity = z.infer<typeof repoActivitySchema>;
