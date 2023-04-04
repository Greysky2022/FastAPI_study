from fastapi import FastAPI,Request,Form
import uvicorn
from fastapi.middleware.cors import CORSMiddleware  # 导入CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get('/')
async def main():
    return {"message": "Hello!"}

UserDB = {"admin": "123456", "grey": "123456"}

class User(BaseModel): #定义请求体参数
    username:str
    password:str

@app.get("/login")
async def login(req:Request):
    return template.TemplateResponse("post.html",context={"request":req})


@app.post("/login_api/")
async def login_check(user:User):
    flag = 'fail!'
    if user.username in UserDB.keys():
        if UserDB[user.username]==user.password:
            flag='success!'
    return {flag}




if __name__ =="__main__":
    uvicorn.run(app=app)

