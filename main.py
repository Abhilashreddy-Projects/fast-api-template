from fastapi import FastAPI
from  pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str


@app.get("/")
async def root(name: str):
    return {"message": "Hello World "+ name}

@app.get("/item")
async def get_item():
    return Item(name="Sample Item", description="This is a sample item.")


@app.post("/item")
async def create_item(item: Item):
    return {"message": f"Item {item.name} created successfully."}
