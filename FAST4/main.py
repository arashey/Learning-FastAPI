from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# مدل داده
class Item(BaseModel):
    name: str
    price: float
    description: str = None

# دیتابیس موقت (لیست در حافظه)
items_db = []

# -------------------- Create --------------------
@app.post("/items/")
def create_item(item: Item):
    item_dict = item.dict()
    item_dict["id"] = len(items_db) + 1  # یه id خودکار میدیم
    items_db.append(item_dict)
    return item_dict

# -------------------- Read (all) --------------------
@app.get("/items/")
def read_items():
    return items_db

# -------------------- Read (one) --------------------
@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in items_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="آیتم پیدا نشد")

# -------------------- Update --------------------
@app.put("/items/{item_id}")
def update_item(item_id: int, new_item: Item):
    for item in items_db:
        if item["id"] == item_id:
            item["name"] = new_item.name
            item["price"] = new_item.price
            item["description"] = new_item.description
            return item
    raise HTTPException(status_code=404, detail="آیتم برای بروزرسانی پیدا نشد")

# -------------------- Delete --------------------
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for item in items_db:
        if item["id"] == item_id:
            items_db.remove(item)
            return {"message": "آیتم حذف شد"}
    raise HTTPException(status_code=404, detail="آیتم برای حذف پیدا نشد")
