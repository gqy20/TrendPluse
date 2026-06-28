/**
 * 报告数据格式化工具
 * 信号 emoji / 影响级别 / 仓库链接等，供组件复用。
 */

/** 信号类型 → emoji（与旧站 models/signal.py 的 get_type_emoji 对齐） */
const SIGNAL_TYPE_EMOJI: Record<string, string> = {
  capability: '🚀',
  abstraction: '🎨',
  workflow: '⚙️',
  eval: '📊',
  safety: '🛡️',
  performance: '⚡',
  commit: '💾',
  release: '🎯',
};

/** 信号类型 → 中文标签 */
const SIGNAL_TYPE_LABEL: Record<string, string> = {
  capability: '新能力',
  abstraction: '抽象层',
  workflow: '工作流',
  eval: '评估',
  safety: '安全',
  performance: '性能',
  commit: '提交',
  release: '发布',
};

export function signalEmoji(type?: string): string {
  return (type && SIGNAL_TYPE_EMOJI[type]) || '📌';
}

export function signalLabel(type?: string): string {
  return (type && SIGNAL_TYPE_LABEL[type]) || type || '其他';
}

/** 影响星标字符串（1-5） */
export function impactStars(score?: number | null): string {
  if (!score || score < 1) return '';
  return '★'.repeat(Math.min(Math.round(score), 5));
}

/** 影响级别分档（用于配色/排序） */
export function impactLevel(score?: number | null): 'high' | 'medium' | 'low' {
  if (!score) return 'low';
  if (score >= 4) return 'high';
  if (score >= 3) return 'medium';
  return 'low';
}

/** GitHub 仓库 → 链接 */
export function repoUrl(repo: string): string {
  return `https://github.com/${repo}`;
}

/** 数字千分位 */
export function formatNumber(n?: number): string {
  if (n == null) return '—';
  return n.toLocaleString('en-US');
}

/** 格式化日期标题（YYYY-MM-DD → 周几补充，可选） */
export function formatDate(date?: string): string {
  if (!date) return '';
  return date;
}

/** 周标识 → 起止范围文案 */
export function weekRange(weekId?: string, start?: string, end?: string): string {
  if (start && end) return `${start} ~ ${end}`;
  return weekId || '';
}

/**
 * 信号类型 → 语义色（hex），用于 badge/图标着色
 * ⚠ Source of truth：与 styles/global.css 的 --color-signal-* 保持一致
 *    （CSS 端定义工具类 token，TS 端用于 withAlpha 拼接 inline 底色），改色请两处同改
 * 高级感色板：低饱和 + 蒙灰统一（告别 Tailwind 拾色器感），冷色为主 + 暖色点缀
 */
const SIGNAL_TYPE_COLOR: Record<string, string> = {
  capability: '#5b9bd5',
  abstraction: '#a684d6',
  workflow: '#4fb3aa',
  eval: '#e0b341',
  safety: '#5bab6e',
  performance: '#e8895a',
  commit: '#8e96a3',
  release: '#d97aa6',
};

export function signalColor(type?: string): string {
  return (type && SIGNAL_TYPE_COLOR[type]) || '#8a92a0';
}

/**
 * 状态语义色（hex）—— 与品牌色解耦，低饱和协调
 * ⚠ 与 styles/global.css 的 --color-status-* 保持一致
 * 影响级别 high/medium/low + 通用 success/warning/danger，
 * 供组件运行时选色（质量分等档、增长、痛点等）
 */
export const STATUS_COLORS = {
  high: '#e8895a',
  medium: '#6e7682',
  low: '#4a515f',
  success: '#5bab6e',
  warning: '#e0b341',
  danger: '#e0655a',
} as const;

/** 8 位 hex + alpha（如 #6366f1 + 0.1 → rgba），用于浅底色 */
export function withAlpha(hex: string, alpha: number): string {
  const a = Math.round(Math.max(0, Math.min(1, alpha)) * 255)
    .toString(16)
    .padStart(2, '0');
  return `${hex}${a}`;
}
