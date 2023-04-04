from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

UserDB = {"admin": "123456", "grey": "123456"}


@app.get("/login/")
async def login_check(username:str,password:str):
    flag = 'fail!'
    if username in UserDB.keys():
        if UserDB[username]==password:
            flag='success!'
    return {flag}




if __name__ =="__main__":
    uvicorn.run(app=app)