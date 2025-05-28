import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(SCRIPT_DIR)
import util


# 改动下面的代码到需要的部分
if __name__ == "__main__":
    util.log_event(util.event_type.walk)