#!/bin/bash
# 每日定时触发 GitHub Actions 工作流
# 使用方法：添加到 crontab，如：0 8 * * * /path/to/run-daily-cron.sh

set -e

# 切换到脚本所在目录
cd "$(dirname "$0")/.."

# 日志文件
LOG_FILE="logs/cron-run-daily.log"
mkdir -p "$(dirname "$LOG_FILE")"

# 记录开始时间
echo "===== $(date '+%Y-%m-%d %H:%M:%S') 开始触发每日分析 =====" >> "$LOG_FILE"

# 触发 workflow，设置 send_notification=true 发送飞书通知
gh workflow run run-daily.yml -f send_notification=true >> "$LOG_FILE" 2>&1

if [ $? -eq 0 ]; then
    echo "✓ 工作流触发成功" >> "$LOG_FILE"
else
    echo "✗ 工作流触发失败" >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
