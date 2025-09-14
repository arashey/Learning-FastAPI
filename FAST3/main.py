from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None, short: bool = False):
    
    result = {"item_id": item_id}
    if q:
        result["query"] = q
    if not short:
        result["description"] = "این یک توضیح کامل برای آیتم است."
    return result


