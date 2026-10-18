from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
items = {}

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/{item_id}")
def create(item_id: int, item: Item):
    items[item_id] = item
    return item

@app.get("/items/{item_id}")
def read(item_id: int):
    if item_id not in items:
        raise HTTPException(404, "Not found")
    return items[item_id]
