from fastapi import FastAPI,Form
import uvicorn

app = FastAPI()

@app.post("/login/")
async def login(
        username:str = None,
        password:str
        # username:str = Form(...), # 必填参数,暂时不知道三个点是什么作用
        # password:str = Form(...)
):
    return {username,password}

if __name__ =="__main__":
    uvicorn.run(app=app)