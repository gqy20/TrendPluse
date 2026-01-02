# 趋势报告归档

!!! note "说明"
    所有报告按时间倒序排列，最新的报告在最前面。

## 最新报告

{% if reports %}
{% for report in reports %}
### [{{ report.date }}](report-{{ report.date }}.md)

{{ report.summary }}

*发布时间: {{ report.published }}*

{% endfor %}
{% else %}
!!! warning "暂无报告"
    报告生成中，请稍后查看...

    报告将在每天 UTC 0:00（北京时间 8:00）自动更新。
{% endif %}

## 按月份浏览

- [2026年1月](#2026-01)
- [2025年12月](#2025-12)

### 2026年1月

{% for report in reports_2026_01 %}
- [{{ report.date }}](report-{{ report.date }}.md) - {{ report.title }}
{% endfor %}

## 统计信息

| 指标 | 数值 |
|------|------|
| 总报告数 | {{ total_reports }} |
| 总信号数 | {{ total_signals }} |
| 本月报告 | {{ monthly_reports }} |
