from fastapi import FastAPI

app = FastAPI()

@app.get("/",{id})
def home(id:int):
    if(id==1):
        return {"patil madarchod"}
    else :
        return {"message": "Hello World"}
