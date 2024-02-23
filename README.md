# TW_Plant_Illustration_Crawler
## Requirements
Crawl data from this url: https://sinica.digitalarchives.tw/collection.php?type=3799 （only 臺灣本土植物數位化典藏）

1. Save data as json files or to a database including the following parameters：
    * 中文種名(string)
    * 學名(string)
    * 標本館號(string)
    * 編目號(string)
    * 引用(string)
    * 採集日期(date string)
    * 採集者(string)
    * 緯度(float)
    * 經度(float)
    * 國家(string)
    * 行政區(string)
    * 最低海拔(float)
    * image url(string)

2. Create a simple restful application with an endpoint to query the crawled specimens.

3. Use swagger ui to document the api
    -   Create an endpoint to download the crawled data including image as a PDF.

## Authors 
- [@IsaacLee0904](https://github.com/IsaacLee0904)

## Repository structure
```
│
├── app/                    # 應用程式的主要資料夾
│   ├── api/                # 處理API路由和邏輯
│   │   ├── __init__.py
│   │   ├── dependencies.py # 依賴項
│   │   └── endpoints/      # 各個API端點
│   │       ├── __init__.py
│   │       └── specimens.py
│   │
│   ├── core/               # 核心設定檔案
│   │   ├── __init__.py
│   │   └── config.py       # 配置檔案
│   │
│   ├── models/             # 資料庫模型
│   │   ├── __init__.py
│   │   └── specimens.py
│   │
│   └── schemas/            # Pydantic模型（用於請求和響應）
│       ├── __init__.py
│       └── specimens.py
│
├── crawler/                # 爬蟲程式碼資料夾
│   ├── __init__.py
│   └── specimens_crawler.py
│
├── pdf_generator/          # PDF生成器
│   ├── __init__.py
│   └── pdf_creator.py
│
├── data                    # 資料庫檔案和遷移
│   ├── __init__.py
│   └── sqlite.db           # SQLite資料庫檔案
│
├── main.py             # FastAPI應用程式入口
├── Dockerfile              # Docker檔案，用於構建應用程式的容器
├── requirements.txt        # Python依賴檔案
└── README.md               # 專案說明文件
```