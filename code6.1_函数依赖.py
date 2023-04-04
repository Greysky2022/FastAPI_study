from fastapi import FastAPI,Depends,Cookie
import uvicorn
from typing import Optional
app = FastAPI()

# async def dep_parms(item_id:int,q:Optional[str]=None):
#     return {"item_id":item_id,"q":q}
#
# @app.get('/')
# async def item_get(
#         commons:dict = Depends(dep_parms)
# ):
#     return commons
#
#
# if __name__ =="__main__":
#     uvicorn.run(app=app)


