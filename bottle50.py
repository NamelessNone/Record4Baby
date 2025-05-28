import os, sys
# 让 Stream Deck 脚本能访问同目录下的其他模块
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(SCRIPT_DIR)
import util

if __name__ == "__main__":
    util.log_event(util.event_type.bottle, 50)