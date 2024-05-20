

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"], 
     allow_headers=["*"],
)
class OperationData(BaseModel):
    a: int
    b: int

@app.post("/add")
def add(data: OperationData):
    return {"result": data.a + data.b}

@app.post("/subtract")
def subtract(data: OperationData):
    return {"result": data.a - data.b}

@app.post("/multiply")
def multiply(data: OperationData):
    return {"result": data.a * data.b}

@app.post("/divide")
def divide(data: OperationData):
    if data.b == 0:
        return {"error": "Cannot divide by zero"}
    return {"result": data.a / data.b}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)