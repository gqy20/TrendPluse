/** 用 UTC 日期构建连续的七日窗口，缺失报告不补零。 */
export function weekSeries(start: string, reports: { date: string; count?: number | null; url: string }[]) {
  const first = new Date(`${start}T00:00:00Z`);
  if (Number.isNaN(first.getTime())) return [];
  return Array.from({ length:7 }, (_, i) => {
    const date = new Date(first); date.setUTCDate(first.getUTCDate() + i);
    const key = date.toISOString().slice(0, 10);
    const report = reports.find(r => r.date === key);
    const count = report && typeof report.count === 'number' && Number.isFinite(report.count) && report.count >= 0 ? report.count : null;
    return { date:key, count, url:report?.url, status:!report ? 'missing' : count == null ? 'unknown' : 'recorded' };
  });
}

/** 验证快照计数，保留真实的零，未知值返回 null。 */
export function recordedCount(value: unknown): number | null {
  return typeof value === 'number' && Number.isFinite(value) && value >= 0 ? value : null;
}
