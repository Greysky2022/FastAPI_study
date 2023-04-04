from fastapi import FastAPI,File,UploadFile
import uvicorn
app = FastAPI()

@app.post("/files")
async def create_file(
        file:bytes = File(...)
):
    return {"file_size":len(file)}

if __name__ =="__main__":
    uvicorn.run(app=app)