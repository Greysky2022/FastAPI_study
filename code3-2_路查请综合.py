from typing import Optional
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price:float
    tax: Optional[float] = None

app = FastAPI()

@app.post("/item/{item_id}")
async def create_item(
        item_id:int, # 路径参数 无默认值
        item:Item, #
        q: Optional[str]=None

):
    result = {"item_id":item_id,**item.dict()}
    if q:
        result.update({"q":q})
    return result

if __name__ =="__main__":
    uvicorn.run(app=app)