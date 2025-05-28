# Record4Baby
为了简便的记录新生儿各种活动而开发的脚本，使用stream deck一键记录到数据库，方便日后查询

## 功能概述
这个中间件让我能按Stream Deck上的实体按键，就可以直接把一件事记录到数据库（暂时是Notion Db）
主要功能存在于util.py中，其他内容较少的python脚本主要是调用util中的函数，并直接配置到stream deck的按钮上

*需要注意python脚本的默认打开方式需要为Python.exe而不是某个编辑器
在stream deck中的按钮上配置Run Script，将脚本指向我们那些简单的脚本（如bottle50.py）
按键即可进行记录

## 使用到的软件与硬件
+ Stream Deck（Elgato）
    + 它的官方配套软件，当然
    + Python Scipt Deck，用来运行脚本
+ Python，3.12
    + notion_client，用来访问notion数据库
    + tomllib，用来访问toml配置文件

## 配置文件，Config.toml
放在项目根目录下

> [notion]
> token = "我的notion token"
> database_id = "notion的data base id"

其中notion token可以从
https://www.notion.so/profile/integrations
创建

data base id看这里
https://developers.notion.com/docs/working-with-databases#adding-pages-to-a-database

> Open the database as a full page in Notion. Use the Share menu to Copy link. Now paste the link in your text editor so you can take a closer look. The URL uses the following format:
>> https://www.notion.so/{workspace_name}/{database_id}?v={view_id}

## Juicy
icon下面的图标可以配置到按钮上，Stream Deck好用！

## 待开发的功能

### 更多的按钮
根据老婆的需求
+ 做操
+ 睡眠
+ 结束，不管是睡眠还是什么
+ 药膏
+ 涂油
+ 遛