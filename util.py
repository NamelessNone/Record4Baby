import tomllib
from notion_client import Client
from datetime import datetime
from enum import Enum
import os, time
import psutil
import win32gui, win32con, win32process

class event_type(Enum):
    null="无效事件"
    bottle="奶瓶"
    breast="母乳"
    poop="大便"
    piss="小便"
    exercises="做操"
    sleep="睡眠"
    finish="完成"
    herb="药膏"
    oil="涂油"
    walk="遛"
    diaper="纸尿裤"
    pad="隔尿垫"


def load_config(filename="config.toml"):
    script_dir=os.path.dirname(os.path.abspath(__file__))
    config_path= script_dir+"/"+filename
    with open(config_path, "rb") as f:
        config = tomllib.load(f)
    return config["notion"]["token"], config["notion"]["database_id"]

def bring_notion_front():
    target_process_name = "Notion.exe"
    notion_hwnd = None
    # 遍历所有窗口
    def enum_windows_callback(hwnd, _):
        nonlocal notion_hwnd
        try:
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            proc = psutil.Process(pid)
            if proc.name() == target_process_name:
                # 确保是可见窗口
                if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
                    notion_hwnd = hwnd
                    return False  # 停止遍历
        except Exception:
            pass
        return True
    win32gui.EnumWindows(enum_windows_callback, None)

    if notion_hwnd:
        # 恢复窗口、激活并置顶
        win32gui.ShowWindow(notion_hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(notion_hwnd)
        win32gui.SetWindowPos(notion_hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        time.sleep(0.2)
        win32gui.SetWindowPos(notion_hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        print("已将 Notion 窗口置于前台。")
    else:
        print("未找到 Notion 主窗口。")


def log_event(event_name: event_type, vol: int=0):
    token, db_id = load_config()

    notion = Client(auth=token)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    build_prop={
            "Name": {
                "type": "title",
                "title": [{ "type": "text", "text": { "content": event_name.value } }]
            },
            "Date": {
                "type": "date",
                "date": { "start": now , "time_zone": "Asia/Shanghai"}
            }
    }
    if event_name is event_type.bottle:
        build_prop["Volume"]={
                "type": "number",
                "number": vol
        }

    response= notion.pages.create(
        parent={"database_id": db_id},
        properties= build_prop
    )
    
    bring_notion_front()
    if(response['object']!= "error"): 
        return True
    else: return False