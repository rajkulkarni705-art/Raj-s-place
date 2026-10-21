
from fastapi import FastAPI

app = FastAPI(
    docs_url="/",
    redoc_url=None
)

@app.get("/home")
def home(id: int = 1):
    if id == 1:
        return {"message": "Patil"}
    else:
        return {"message": "Hello World"}
