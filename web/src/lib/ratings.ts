export type RatingKind = 'impact' | 'confidence';

/** 将真实评分转换为紧凑图形，缺失或越界值不推测等级。 */
export function renderRating(value: number | null | undefined, kind: RatingKind = 'impact', large = false): string {
  const max = kind === 'impact' ? 5 : 1;
  const valid = typeof value === 'number' && Number.isFinite(value) && value >= 0 && value <= max;
  const steps = kind === 'impact' ? 5 : 10;
  const filled = valid ? Math.round(value / max * steps) : 0;
  const label = valid
    ? kind === 'impact' ? `影响 ${value}/5` : `置信度 ${Math.round(value * 100)}%`
    : kind === 'impact' ? '未提供影响评分' : '未提供置信度';
  const tone = kind === 'confidence' ? 'accent' : valid && value >= 4 ? 'high' : valid && value >= 3 ? 'medium' : 'low';
  const marks = Array.from({ length:steps }, (_, i) => `<span class="rating-mark${i < filled ? ' is-filled' : ''}" style="--mark-height:${6 + i * 3}px" aria-hidden="true"></span>`).join('');
  return `<span class="rating rating-${kind}${large ? ' rating-large' : ''}" data-tone="${tone}" data-state="${valid ? 'known' : 'unknown'}" role="img" aria-label="${label}" title="${label}">${marks}</span>`;
}
