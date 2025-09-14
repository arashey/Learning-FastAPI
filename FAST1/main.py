from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name = str
    discription = str=None
    price = float
    

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "hi to FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q} 
