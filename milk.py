import sys
from datetime import datetime

# 读取传入参数作为事件名
event = sys.argv[1] if len(sys.argv) > 1 else "未命名事件"

# 构造日志内容
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_line = f"{now} - {event}\n"

# 写入本地日志文件
log_file = "F:/Projects/python/record4baby/db/event_log.txt"
with open(log_file, "a", encoding="utf-8") as f:
    f.write(log_line)
