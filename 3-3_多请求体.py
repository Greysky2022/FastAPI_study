from typing import Optional
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class User(BaseModel):
    username:str
    full_name: Optional[str] = None

@app.post("/item/{item_id}")
async def update_item(
        item_id: str,
        item: Item,
        user: User
):
    result = {"item_id":item_id,"item":item,"user":user}
    return result

if __name__ =="__main__":
    uvicorn.run(app=app)