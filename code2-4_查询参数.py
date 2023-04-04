from fastapi import FastAPI
import uvicorn
from typing  import Optional
app = FastAPI()

items = [{"a":"aa"},{"b":"bb"},{"c":"cc"}]

# 查询参数
@app.get("/items/")
async def read_item(skip:int = 0,limit:int=10):
    return items[skip:skip+limit] # 切片含左不含右


# 查询 http://127.0.0.1:8000/items/?limit=1 结果只有{"a":"aa"}
# 展示了查询参数的输入方法及其使用前提（要在路径操作函数中声明）
# 默认值是必须的吗？ 是的呢

#可选查询参数
@app.get("/items2/{item_id}")
async def read_item2(
<<<<<<< HEAD
        item_id:str="sds", # 路径参数不能为空,就算写了默认值也是无用，请求时必须带上该参数
        q:Optional[str] = None, # 可选查询参数必须设置默认值为None
        short:bool=False
):
    item = {"item_id":item_id,"short":short}
=======
        item_id:str, # 路径参数不能为空，无默认值
        q:Optional[str] = None, # 可选查询参数必须设置默认值为None
        short:bool = False # 查询参数必须有默认值
):
    item = {"item_id":item_id}
>>>>>>> 213ae4ea7ebae962393706483851c69a81e4ad60
    if q:
        item.update({"q":q})
    if short:
        item.update({"description":"short为True"})
    return item

if __name__ =="__main__":
    uvicorn.run(app=app)