# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Changed
- 目录结构收敛：`services` 合并为 `workflows`，`readers` 合并到 `collectors`
- 命令入口统一收口到 `cli/`，`automation/` 退回为实现层
- `pipeline.py` 拆出 weekly / daily finalizer 等 workflow，显著缩小编排文件体积
- JSON-first 架构重构：数据模型从 dict 迁移到 Pydantic BaseModel
- 活跃度数据 (`ActivityData`) 使用结构化模型
- Release 数据 (`ReleasesData`) 使用结构化模型
- 飞书配置 `feishu_at_mobiles` 从列表类型改为逗号分隔字符串

### Fixed
- 恢复异步分析器兼容入口：`TrendAnalyzer.analyze_prs_async()` 与 `ReleaseSummarizer.summarize_releases_async()`
- GitHub Actions 配置测试改为显式隔离 GitHub Token 环境变量，避免受运行环境污染
- 修复 `feishu_at_mobiles` 空字符串导致的 JSON 解析错误
- 修复 `run` 主流程中对结构化模型的访问方式
- 修复飞书通知报告提取的多项问题

### Added
- 架构说明与测试说明文档
- Commit 信号分析功能
- Release 监控和分析功能
- Breaking Changes 检测功能
- 仓库活跃度分析（commit 数、活跃仓库、新贡献者）
- 飞书通知 @ 提醒功能
- 信号去重机制（基于 LLM）

## [0.3.0] - 2026-01-04

### Added
- **飞书通知支持**: 支持富文本卡片和 @ 提醒
- **仓库活跃度分析**: 追踪 commit 数量、活跃仓库排名
- **Commit 信号分析**: 从代码提交中提取技术趋势
- **Release 监控**: 自动追踪 GitHub Releases
- **Breaking Changes 检测**: AI 检测版本不兼容变更

### Fixed
- 修复飞书 @ 提醒手机号解析问题
- 修复 ActivityData 属性访问问题

## [0.2.0] - 2026-01-02

### Added
- **GitHub Actions 集成**: 每日自动分析和报告生成
- **GitHub Pages 部署**: 自动发布报告到网站
- **信号去重**: 基于 LLM 的智能去重机制
- **FeishuFormatter**: 飞书卡片格式化器

### Changed
- 重构通知器架构，分离 BaseNotifier 和 FeishuNotifier
- 优化报告生成流程

## [0.1.0] - 2025-12-20

### Added
- **核心功能**: GitHub 趋势分析
- **AI 驱动**: 使用 GLM-4 模型分析 PR 和 Issue
- **智能筛选**: 基于标签和事件类型的候选筛选
- **结构化报告**: Markdown 格式的每日趋势报告
- **TDD 开发**: 测试驱动开发，162+ 单元测试
- **代码质量**: Ruff 格式化和检查
- **日志系统**: Rich 彩色日志输出

### Features
- 📦 使用 uv 包管理器
- 🤖 智谱 AI GLM-4 模型集成
- 📊 自动化趋势分析报告
- ✅ 100%+ 测试覆盖率
- 🚀 GitHub Actions CI/CD
- 📝 Markdown 报告生成
