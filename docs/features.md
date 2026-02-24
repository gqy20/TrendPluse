# 功能概述

TrendPulse 是一个自动化趋势分析工具，专注于 Anthropic Claude 生态系统的动态追踪。

## 核心特性

### 1. 智能事件采集

- 🔍 **GitHub API 集成**: 实时获取 PR、Issue、Release
- 🎯 **智能筛选**: 过滤高价值活动
- 📅 **定时采集**: 每日自动更新数据
- 📦 **Release 监控**: 自动追踪版本发布，分析升级趋势
- 💾 **Commit 分析**: 从代码提交中提取技术信号
- 📈 **仓库活跃度**: 追踪 commit 数量、活跃仓库、新贡献者
- 🧠 **Issue 数据落盘**: 按日期和仓库输出 JSONL，支持后续 Agent 分析

### 2. AI 驱动分析

- 🤖 **GLM-4 模型**: 使用智谱 AI 进行深度分析
- 📊 **信号提取**: 自动识别技术趋势和创新点
- 🏷️ **智能分类**: 工程、研究、生态等多维度分类
- 🔄 **智能去重**: 基于 LLM 的信号去重机制
- 🔍 **Breaking Changes 检测**: AI 检测版本不兼容变更
- 🚀 **Release AI 总结**: 使用 AI 分析 Release Notes，生成结构化中文总结
- 🧠 **Issue 洞察（Agent）**: 三轮分析提取用户痛点，并输出质量分

### 3. 结构化报告

- 📝 **Markdown 格式**: 易读、易分享
- 📄 **JSON 格式**: 机器可读，支持数据分析和 API
- 🎨 **美观展示**: GitHub Pages 自动发布
- 🔍 **全文搜索**: 快速找到历史信息
- 📆 **周报聚合**: 聚合近 7 天日报输出 weekly 报告
- 🧭 **项目发现报告**: 发现候选项目并输出 discovery 报告
- 📬 **飞书通知**: 支持 @ 提醒和富文本卡片
- 📱 **折叠面板**: 飞书卡片使用折叠面板优化信息展示
- 🔄 **自动重试**: LLM 调用失败自动重试（指数退避）

### 4. 并行处理

- ⚡ **并行采集**: 使用线程池并行调用 GitHub API
- ⚡ **并行分析**: PR 和 Release 分析并行处理
- 🛡️ **容错设计**: 单个任务失败不影响整体流程

### 5. 自动化工作流

- ✅ CI：代码检查、类型检查、测试
- 📊 每日分析：生成日报并同步文档
- 📆 每周报告：聚合日报生成周报
- 🧭 项目发现：定时发现热门候选项目
- 🧠 Issue 仓库分析：在 issue/comment 中通过 `@claude` 触发
- ➕ 新增仓库请求：自动处理仓库请求流程
- 📬 飞书通知：日报/周报推送

## 支持的仓库

默认追踪以下仓库的动态：

- `anthropics/anthropic-sdk-python`
- `anthropics/claude-quickstarts`
- `anthropics/skills`
- `anthropics/claude-cookbook`

支持 50+ AI 编程工具和 Agent 框架仓库，可在配置文件中添加更多仓库。

## 报告内容

每份报告包含：

- 📊 **当日总览**: 简洁的摘要说明
- 🔧 **工程信号**: 工具链更新、API 变更（折叠面板）
- 🔬 **研究信号**: 论文、实验、探索（折叠面板）
- 💾 **Commit 信号**: 从代码提交中提取的技术信号
- 🎯 **Release 信号**: 版本发布信号分析
- 🚀 **版本发布**: 最新版本发布信息（带 AI 总结）
- ⚠️ **Breaking Changes**: 不兼容变更检测
- 📈 **仓库活跃度**: Commit 数量、活跃仓库排名
- 🧠 **Issue 洞察（Agent）**: 用户痛点 TOP 与质量指标
- 📊 **统计数据**: 分析数量、影响评分
- 🔗 **JSON 数据**: 完整的结构化数据

额外产物：

- 📆 **周报**: 按周汇总高影响趋势与活跃度
- 🧭 **项目发现报告**: 候选项目、质量评分与推荐优先级

## 技术栈

| 组件 | 技术 |
|------|------|
| 语言 | Python 3.13+ |
| 包管理 | uv |
| AI 模型 | 智谱 GLM-4 |
| 并行处理 | ThreadPoolExecutor |
| 重试机制 | tenacity |
| API | GitHub REST API |
| 部署 | GitHub Actions |
| 展示 | MkDocs + Material |
| 通知 | 飞书 Webhook |

## 关键能力说明

### Issue 洞察（Agent）

- 三轮流程：候选抽取 → 主题归一化 → 审稿与优先级判定
- 输出内容：`top_pain_points`、`quality_score`、`quality_status`
- 与日报融合：在日报中单独展示 Issue 洞察章节

### 项目发现（Discovery）

- 数据来源：Trending + 关键词搜索
- 流程：去重 → 质量评估 → 分类排序 → 发现报告
- 输出位置：`reports/discovery/` 与 `docs/discovery-reports/`

### 周报聚合

- 从过去 7 天日报聚合生成周报
- 输出位置：`reports/weekly/` 和 `docs/reports/`
