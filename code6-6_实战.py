from fastapi import FastAPI,Depends
import uvicorn
from pydantic import BaseModel

class Goods(BaseModel):
    name:str
    num:float
    unit:str
    price:float

async def conculate(good:Goods):
    return good.num*good.price

app = FastAPI()
@app.put('/goods/')
async def jisuan(
        stat:float = Depends(conculate)
):
    return stat


if __name__ =="__main__":
    uvicorn.run(app=app)