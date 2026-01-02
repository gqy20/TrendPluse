# TrendPluse - Claude Code 指令

## 项目概述

- **Python 版本**: 3.13+
- **包管理**: uv（极速包管理器）
- **项目结构**: src layout
- **代码规范**: ruff（检查 + 格式化）
- **测试框架**: pytest
- **日志系统**: rich

## 常用命令

```bash
# 创建虚拟环境并安装依赖
make install

# 代码检查
make check

# 格式化
make format

# 测试
make test
make test-cov

# 运行所有检查
make all
```

## 代码规范

1. **语言**: 所有注释、文档字符串使用中文
2. **命名**: 函数和类使用英文（遵循 PEP 8）
3. **类型注解**: 必需
4. **文档字符串**: Google 风格中文文档
5. **提交规范**: feat/fix/docs/refactor/test/chore



## 项目结构

```
src/trendpluse/
├── __init__.py    # 包初始化，导出公共 API
├── core.py        # 核心功能
├── logger.py      # 日志系统

└── main.py        # 主程序入口
```
