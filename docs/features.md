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

### 2. AI 驱动分析

- 🤖 **GLM-4 模型**: 使用智谱 AI 进行深度分析
- 📊 **信号提取**: 自动识别技术趋势和创新点
- 🏷️ **智能分类**: 工程、研究、生态等多维度分类
- 🔄 **智能去重**: 基于 LLM 的信号去重机制
- 🔍 **Breaking Changes 检测**: AI 检测版本不兼容变更

### 3. 结构化报告

- 📝 **Markdown 格式**: 易读、易分享
- 🎨 **美观展示**: GitHub Pages 自动发布
- 🔍 **全文搜索**: 快速找到历史信息
- 📬 **飞书通知**: 支持 @ 提醒和富文本卡片

## 数据流程

```mermaid
sequenceDiagram
    participant GH as GitHub
    participant Collector as 采集器
    participant Filter as 筛选器
    participant AI as AI 分析
    participant Reporter as 报告器
    participant Pages as GitHub Pages

    GH->>Collector: 获取事件
    Collector->>Filter: 传递原始数据
    Filter->>Filter: 筛选候选
    Filter->>AI: 发送 PR 详情
    AI->>AI: 提取信号
    AI->>Reporter: 生成报告
    Reporter->>Pages: 发布到网站
```

## 支持的仓库

默认追踪以下仓库的动态：

- `anthropics/anthropic-sdk-python`
- `anthropics/claude-quickstarts`
- `anthropics/skills`
- `anthropics/claude-cookbook`

可在配置文件中添加更多仓库。

## 报告内容

每份报告包含：

- 📊 **当日总览**: 简洁的摘要说明
- 🔧 **工程信号**: 工具链更新、API 变更
- 🔬 **研究信号**: 论文、实验、探索
- 💾 **Commit 信号**: 从代码提交中提取的技术信号
- 🎯 **版本发布**: 最新版本发布信息
- 📈 **仓库活跃度**: Commit 数量、活跃仓库排名
- ⚠️ **Breaking Changes**: 不兼容变更检测
- 📈 **统计数据**: 分析数量、影响评分

## 技术栈

| 组件 | 技术 |
|------|------|
| 语言 | Python 3.13+ |
| 包管理 | uv |
| AI 模型 | 智谱 GLM-4 |
| API | GitHub REST API |
| 部署 | GitHub Actions |
| 展示 | MkDocs + Material |
