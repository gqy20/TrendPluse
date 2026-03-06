# TrendPulse 第一阶段重构任务拆分（内部文档）

> 用途：把《REFACTOR_BLUEPRINT_INTERNAL.md》拆成第一阶段可执行任务。
>
> 范围：只做低风险结构迁移，不主动改变产品行为。

---

## 1. 第一阶段目标

第一阶段只做三件事：

1. 建立新的骨架目录：`app/`、`reports/`
2. 把“报告构建”和“报告发布”从 `workflows/` 中抽出来
3. 保持旧入口兼容，确保现有命令和主流程继续可用

第一阶段明确不做：

- 不修改 `DailyReport` 字段语义
- 不删除 `pipeline.py`
- 不删除 `workflows/`
- 不统一 daily 的同步/异步实现
- 不大规模改测试结构

---

## 2. 任务清单

### 任务 A：新增新骨架

- [x] 新建 `src/trendpluse/app/`
- [x] 新建 `src/trendpluse/reports/`
- [x] 增加基础 `__init__.py`

### 任务 B：迁移报告发布

- [x] 新建 `src/trendpluse/reports/publisher.py`
- [x] 将 `ReportOutputService` 变为兼容包装
- [ ] 补充新模块的直接单测

### 任务 C：迁移报告构建

- [x] 新建 `src/trendpluse/reports/builder.py`
- [x] 将 `DailyReportFinalizer` 变为兼容包装
- [ ] 补充空报告和 stats 构建测试

### 任务 D：补 bootstrap 骨架

- [x] 新建 `src/trendpluse/app/bootstrap.py`
- [ ] 在后续阶段让 pipeline 真正使用 bootstrap

### 任务 E：验证兼容性

- [ ] 跑 `test_report_output_service.py`
- [ ] 跑部分 pipeline 相关测试
- [ ] 检查新旧导入路径同时可用

---

## 3. 当前阶段产出物

第一阶段完成后，仓库应同时存在两套层次：

### 新层次

- `trendpluse.reports.builder`
- `trendpluse.reports.publisher`
- `trendpluse.app.bootstrap`

### 兼容层

- `trendpluse.workflows.daily_report_finalizer`
- `trendpluse.workflows.report_output`

兼容层的作用不是继续承载逻辑，而是作为旧调用点的转发壳。

---

## 4. 第一阶段完成标准

满足以下条件即可视为第一阶段完成：

1. 新模块已开始承载真实逻辑，不只是空文件。
2. 旧导入路径不需要立即改动也能继续运行。
3. 旧测试基本仍可通过。
4. 后续第二阶段可以直接从新模块继续迁移。

---

## 5. 第二阶段入口

第一阶段完成后，下一步直接进入：

1. 让 `pipeline.py` 复用 `app/bootstrap.py`
2. 统一 daily 的 async 主流程
3. 开始把中间对象迁入 `models/`

这时再动 `pipeline.py` 风险会明显更低，因为报告层已经先被抽离。
