import tomllib
from notion_client import Client
from datetime import datetime
from enum import Enum
import os

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

def load_config(filename="config.toml"):
    script_dir=os.path.dirname(os.path.abspath(__file__))
    config_path= script_dir+"/"+filename
    with open(config_path, "rb") as f:
        config = tomllib.load(f)
    return config["notion"]["token"], config["notion"]["database_id"]

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
                "date": { "start": now }
            }
    }
    if event_name is event_type.bottle:
        build_prop["Volume"]={
                "type": "number",
                "number": vol
        }

    notion.pages.create(
        parent={"database_id": db_id},
        properties= build_prop
    )