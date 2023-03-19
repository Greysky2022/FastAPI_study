#经典三连
from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/items/{item_id}") # 注册路由路径，定义了一个名为item_id的路由路径参数（前端负责将参数以路由参数的形式传过来）
async def read_item(item_id:int):
    print(item_id)    # 后端打印一下接受到的数据
    return {"item_id":item_id}

if __name__ =="__main__":
    uvicorn.run(app=app)