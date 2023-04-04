from fastapi import FastAPI,Depends
import uvicorn

app = FastAPI()

class PetQueryChecker:
    def __init__(self,pet_name:str):
        self.pet_name = pet_name
    def __call__(self, q:str = ''):
        if q:
            return self.pet_name in q #
        else:
            return False

checkcat = PetQueryChecker("cat")
checkdog = PetQueryChecker("dog")

@app.get("/pet")
async def read_query_check(
    has_dog:bool = Depends(checkdog),
    has_cat:bool = Depends(checkcat)
):
    return {"has dog":has_dog,"has cat":has_cat}

if __name__ =="__main__":
    uvicorn.run(app=app)