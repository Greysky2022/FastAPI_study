from fastapi import FastAPI, Request
import time
import uvicorn

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):  # callnext是回调函数
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)  # 在字典中添加键值对
    return response


@app.get('/test/{id_item}')
async def test_middleware(id_item: int):
    return id_item

if __name__ =="__main__":
    uvicorn.run(app=app)