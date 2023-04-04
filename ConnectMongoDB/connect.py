from typing import Optional,List
from pydantic import BaseModel
import uvicorn
from fastapi import Depends,FastAPI
from pymongo import MongoClient
from bson.json_util import dumps
import json
app = FastAPI()

MONGO_DATABASE_URL = 'mongodb://localhost:27017/'

def get_db():
    client = MongoClient(MONGO_DATABASE_URL)
    db = client['test']
    try:
        yield db
    finally:
        client.close()

class Item(BaseModel):
    title:str
    description:Optional[str]=None

@app.post('/item/',response_model=Item)
async def create_item(item:Item,db:MongoClient = Depends(get_db)):
    mycol = db['items']
    obj = mycol.insert_one(item.dict())
    return item
@app.get('/item/',response_model=List[Item])
async def get_item(db:MongoClient = Depends(get_db)):
    mycol = db['items']
    return json.loads(dumps(mycol.find()))

if __name__ == '__main__':
    uvicorn.run(app=app)