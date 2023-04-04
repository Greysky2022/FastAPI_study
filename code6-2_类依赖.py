from fastapi import FastAPI,Depends
import uvicorn
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Father():
    def __init__(self,x,y):
        self.x = x
        self.y = y
class Son(Father):
    def __init__(self,x:int ,y:int ,z:str):
        super().__init__(x,y)
        self.z = z
@app.get("/")
async def search_furniture(
        params:Son=Depends()
):
    return params

if __name__ =="__main__":
    uvicorn.run(app=app)


# class DepParam:
#     def __init__(self,q:Optional[str]=None,skip:int =0,limit:int = 1000):
#         self.q = q
#
#         self.skip = skip
#
#         self.limit = limit
#
# @app.get("/")
# async def func1(params:DepParam = Depends() ):
#     return params
#
# if __name__ =="__main__":
#     uvicorn.run(app=app)