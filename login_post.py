from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

UserDB = {"admin": "123456", "grey": "123456"}

class User(BaseModel): #定义请求体参数
    username:str
    password:str


@app.post("/login/")
async def login_check(user:User):
    flag = 'fail!'
    if user.username in UserDB.keys():
        if UserDB[user.username]==user.password:
            flag='success!'
    return {flag}

if __name__ =="__main__":
    uvicorn.run(app=app)