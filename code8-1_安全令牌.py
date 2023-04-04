from fastapi import FastAPI,Depends
from fastapi.security import OAuth2PasswordBearer
import uvicorn

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.get('/items')
async def read_items(
        token: str = Depends(oauth2_scheme)
):
    return {"token":token}

if __name__ =="__main__":
    uvicorn.run(app=app)