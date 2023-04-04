from fastapi import FastAPI
import uvicorn

# 建立一个字典
items = {"商品A":{"单价": 10,"单位": "箱","库存": 5},
         "商品B":{"单价":20 ,"单位":"盒" ,"库存": 10},
         "商品B":{"单价":20 ,"单位":"盒" ,"库存": 10},
         }

app = FastAPI()

@app.get("/shop/")
async def goods_table(name):
    return items[name] # 还可以再优化，比如把商品名加进去

if __name__ =="__main__":
    uvicorn.run(app=app)