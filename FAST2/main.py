from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# مدل داده‌ها
class Item(BaseModel):
    name: str
    description: str = None  # اختیاری
    price: float

# GET قبلی
@app.get("/")
def read_root():
    return {"message": "hi to FastAPI !"}

# POST برای ایجاد آیتم
@app.post("/items/")
def create_item(item: Item):
    return {"item_add": item}

