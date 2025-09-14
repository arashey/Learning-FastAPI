from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import db, Item

app = FastAPI()

# Pydantic Schemas
class Itemmain(BaseModel):
    name: str
    price: float
    description: str | None = None

class ItemResponse(Itemmain):
    id: int
    class Config:
        from_attributes = True   # ✅ برای پشتیبانی از ORM در Pydantic v2

# مدیریت اتصال DB
@app.on_event("startup")
def startup():
    if db.is_closed():
        db.connect()

@app.on_event("shutdown")
def shutdown():
    if not db.is_closed():
        db.close()

# Create
@app.post("/items/", response_model=ItemResponse)
def create_items(item: Itemmain):
    new_item = Item.create(name=item.name, price=item.price, description=item.description)
    return ItemResponse.model_validate(new_item)  # ✅ در v2 باید از model_validate استفاده کنی

# Read all
@app.get("/items/", response_model=list[ItemResponse])
def all_items():
    items = Item.select()
    return [ItemResponse.model_validate(i) for i in items]

# Read one
@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    try:
        item = Item.get(Item.id == item_id)
        return ItemResponse.model_validate(item)
    except Item.DoesNotExist:
        raise HTTPException(status_code=404, detail="item not found!")

# Delete
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    deleted = Item.delete().where(Item.id == item_id).execute()
    if not deleted:
        raise HTTPException(status_code=404, detail="item not found!")
    return {"message": "Item deleted"}
