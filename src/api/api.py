import sqlite3
from typing import List, Optional
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, HttpUrl

# define the model
class Specimen(BaseModel):
    chinese_name: Optional[str]
    scientific_name: Optional[str]  
    museum_number: Optional[str]
    image_url: Optional[HttpUrl]

# load data from the database
def get_specimens() -> List[Specimen]:
    try:
        conn = sqlite3.connect('data/specimens.db')
        cursor = conn.cursor()
        cursor.execute("SELECT chinese_name, scientific_name, museum_number, image_url FROM specimens")
        specimens_data = cursor.fetchall()
    except sqlite3.Error as error:
        print(f"databaseerror: {error}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        if conn:
            conn.close()

    # return the query result as a table named Specimen 
    return [Specimen(chinese_name=row[0], scientific_name=row[1], museum_number=row[2], image_url=row[3]) for row in specimens_data]

app = FastAPI()

templates = Jinja2Templates(directory="src/api")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    specimens = get_specimens()  
    return templates.TemplateResponse("specimens.html", {"request": request, "specimens": specimens})
