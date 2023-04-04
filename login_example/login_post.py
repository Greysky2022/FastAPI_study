from fastapi import FastAPI,Request,Form
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
import uvicorn
from typing import Optional
from starlette.staticfiles import StaticFiles


app = FastAPI()
templates = Jinja2Templates(directory="./templates")
app.mount('/static/js',StaticFiles(directory='./static'),name='static')

UserDB = {"admin": "123456", "grey": "123456"}

class User(BaseModel): #定义请求体参数
    username:str
    password:str

@app.get("/login")
async def login(req:Request):
    return templates.TemplateResponse("index.html",context={"request":req})


# @app.post("/login_api/")
# async def login_check(request: Request, username: str = Form(...), password: str = Form(...)):
#     flag = 'fail!'
#     if username in UserDB.keys():
#         if UserDB[username]==password:
#             flag='success!'
#     return {flag}
@app.post("/login_api/")
async def login_check(user:User):
    flag = 'fail!'
    if user.username in UserDB.keys():
        if UserDB[user.username]==user.password:
            flag='success!'
    return {flag}

if __name__ =="__main__":
    uvicorn.run(app=app)