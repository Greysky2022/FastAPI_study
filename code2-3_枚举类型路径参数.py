from fastapi import FastAPI
import uvicorn
from enum import Enum

app = FastAPI()


class ModelName(str, Enum): # 创建一个枚举类
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName): # 在这一步中，str参数被“改造”成ModelName类型
    print(model_name) #ModelName.lenet
    if model_name == ModelName.alexnet:
        return {"model_name": model_name}
    if model_name.value == "lenet":
        return {"model_name": model_name}
if __name__ =="__main__":
    uvicorn.run(app=app)