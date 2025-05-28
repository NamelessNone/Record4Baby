import tomllib
from notion_client import Client
from datetime import datetime
from enum import Enum
import os

class event_type(Enum):
    bottle=0
    breast=1
    stool=2
    piss=3

alias_map={
    event_type.bottle:"奶瓶",
    event_type.breast:"母乳",
    event_type.stool:"大便",
    event_type.piss:"小便"
}

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
                "title": [{ "type": "text", "text": { "content": alias_map[event_name] } }]
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