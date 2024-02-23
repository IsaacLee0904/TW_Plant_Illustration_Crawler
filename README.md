# TW_Plant_Illustration_Crawler
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