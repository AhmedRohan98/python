from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum
app = FastAPI()
class Item(BaseModel):
    name: str
    description: str = None
@app.post("/items/")
def create_item(item: Item):
    return {"name": item.name, "description": item.description}
handler = Mangum(app)