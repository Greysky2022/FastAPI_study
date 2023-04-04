#先来一个经典三连
from fastapi import FastAPI
import uvicorn
app = FastAPI() # 创建FastAPI应用实例

@app.get("/items/{item_id}") # 注册路由路径，定义了一个名为item_id的路由路径参数（前端负责将参数以路由参数的形式传过来）
async def read_item(item_id):
    print(item_id)    # 后端打印一下接受到的数据
    strr = "ack-"+ item_id # 后端对数据进行加工处理
    return {"item_id":strr} # 后端以字典的形式将参数返回给前端

if __name__ =="__main__":
    uvicorn.run(app=app)
