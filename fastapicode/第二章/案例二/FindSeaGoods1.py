# FindSeaGoods1.py
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel  # 导入基础模型类


class Goods(BaseModel):  # 定义数据模型类，继承自BaseModel类
    name: str  # 定义字段name，类型 str
    num: float  # 定义字段num，类型float
    unit: str  # 定义字段unit，类型 str
    price: float  # 定义字段price，类型float


app = FastAPI()


@app.put("/goods/")  # 注册路由路径
async def findGoods(name, good: Goods):  # 定义路径操作函数

    return good


if __name__ == '__main__':
    uvicorn.run(app=app)
