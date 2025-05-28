from notion_client import Client
from datetime import datetime
import tomllib
import sys


# ==== 配置 ====
NOTION_TOKEN = "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"  # 你的 Notion Token
DATABASE_ID = "201ea51e249c80f98f54f4dffe4c2c1e"  # 你的数据库 ID

event = "奶瓶"
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

notion = Client(auth=NOTION_TOKEN)

# ==== 写入数据库 ====
notion.pages.create(
    parent={"database_id": DATABASE_ID},
    properties={
        "Name": {
            "type": "title",
            "title": [{ "type": "text", "text": { "content": "奶瓶" } }]
        },
        "Volume": {
            "type": "number",
            "number": 60
        },
        "Date": {
            "type": "date",
            "date": { "start": now }
        }
    }
)
