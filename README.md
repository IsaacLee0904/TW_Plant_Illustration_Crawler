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
├── src
│   ├── api                    
│   │       
│   └── crawler
│ 
├── data                    
│   └── sqlite.db           
├── docs
├── setup.py
├── main.py                 
├── Dockerfile              
└── README.md               
```