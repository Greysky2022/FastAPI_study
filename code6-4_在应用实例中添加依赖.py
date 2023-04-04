from fastapi import FastAPI,Depends,Header,Cookie,HTTPException
import uvicorn

async def verify_token(x_token: str = Header(...)):
    if x_token != "my_token":
        raise HTTPException(status_code=400,detail="token已经失效")

async def check_userid(userid: str = Cookie(...)): # 官方文档失效，无法判断出Cookie
    if userid != "9527":
        raise HTTPException(status_code=400,detail='无效的用户')

app = FastAPI(dependencies=[Depends(verify_token),Depends(check_userid)])

@app.get("/")
async def get_id():
    return "sdsdsd"

if __name__ =="__main__":
    uvicorn.run(app=app)