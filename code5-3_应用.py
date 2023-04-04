from fastapi import FastAPI,Query
from typing import Optional
import uvicorn
from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from pydantic import BaseModel

app = FastAPI()
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request,exc): # 覆盖异常处理器（http_exception_handler）
    return PlainTextResponse(str(exc.detail),status_code=exc.status_code) # 从效果上看就是把http_exception_handler 处理函数的异常改为了StarletteHTTPException异常类，并且调用了该类的方法

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request,exc):
    return PlainTextResponse(str(exc),status_code=400)

class One(BaseModel):
    name:str
    rank:str
    edition:float
    belongTo:str

roles_table={
    '雷电将军':['5星',3.3,'稻妻城'], #人物星级，抽取版本 人物所属
    '胡桃':['5星',3.4,'往生堂'],
    '夜兰':['5星',3.4,'岩上荼室'],
    '行秋':['4星',3.3,'飞云商会']
}

@app.post('/roles/',response_model=One)
async def find_role(one:One,name:str=Query(...,max_length=10,min_length=1)):
    if name in roles_table.keys():
        values = roles_table[name]
        one.name = name
        one.rank = values[0]
        one.edition = values[1]
        one.belongTo = values[2]
        return one
    else:
        raise HTTPException(status_code=418,detail="角色"+name+"未抽取！")

if __name__ =="__main__":
    uvicorn.run(app=app)

