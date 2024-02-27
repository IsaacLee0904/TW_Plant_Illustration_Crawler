# TW Plant Illustration Crawler
## Requirements
Crawl data from this URL: https://sinica.digitalarchives.tw/collection.php?type=3799 (only for Taiwan native plant digital collections)

1. Save data as JSON files or to a database, including the following parameters:
    * 中文種名 (string)
    * 學名 (string)
    * 標本館號 (string)
    * 編目號 (string)
    * 引用 (string)
    * 採集日期 (date string)
    * 採集者 (string)
    * 緯度 (float)
    * 經度 (float)
    * 國家 (string)
    * 行政區 (string)
    * 最低海拔 (float)
    * image url (string)

2. Create a simple RESTful application with an endpoint to query the crawled specimens.

3. Use Swagger UI to document the API.

## Authors
- [@IsaacLee0904](https://github.com/IsaacLee0904)

## Repository structure
```
├── README.md
├── data
│   ├── 20240226134932_Plant.json
│   └── specimens.db
├── dockerfile
├── main.py
├── src
│   ├── ETL
│   │   └── etl.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-38.pyc
│   │   │   └── api.cpython-38.pyc
│   │   ├── api.py
│   │   └── specimens.html
│   ├── buildup
│   │   └── create_db.py
│   └── crawler
│       └── crawler.py
└── utils
    ├── ETL_utils.py
    ├── __init__.py
    ├── __pycache__
    │   ├── ETL_utils.cpython-38.pyc
    │   ├── __init__.cpython-38.pyc
    │   └── crawler_utils.cpython-38.pyc
    └── crawler_utils.py            
```
For reproducibility, this README.md describes how to start the crawler and application.

First, ensure your Docker environment is installed and running. Then, follow the steps in the "Environment Setup" section to build your Docker image.

## Env setup
```
docker pull selenium/standalone-chrome
docker build -t tw_plant_illustration_crawler .
```
## How to Run the Code
### Starting the Crawler
Run the Docker command listed under the "Crawler" section to start crawling data from the specified URL.
```
docker run -v /Users/wen/Desktop/TW_Plant_Illustration_crawler:/app tw_plant_illustration_crawler /bin/bash -c "source activate env && python src/crawler/crawler.py"
```
### Data Extraction, Transformation, and Loading (ETL)
After crawling the data, run the Docker command listed under the "ETL" section to process and save the data.
```
docker run -v /Users/wen/Desktop/TW_Plant_Illustration_crawler:/app tw_plant_illustration_crawler /bin/bash -c "source activate env && python src/ETL/etl.py"
```
### Starting the API
Once the data is processed, run the Docker command listed under the "API" section to start the RESTful API service.
```
docker run -v /Users/wen/Desktop/TW_Plant_Illustration_crawler:/app -p 8000:8000 tw_plant_illustration_crawler /bin/bash -c "source activate env && uvicorn src.api.api:app --host 0.0.0.0 --reload"
```
Visit `http://localhost:8000` to check if the API is running properly.
```
# API port
http://localhost:8000 

# Swagger UI
http://localhost:8000/docs
```











