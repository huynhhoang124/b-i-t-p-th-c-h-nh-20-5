from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"], 
     allow_headers=["*"],
)

students = [
    {"id": 1, "name": "F", "age": 20, "address": "T1", "phone": "555-555-5555", "email": "skt1_faker@gmail.com", "class": "Tliet"},
    {"id": 2, "name": "a", "age": 18, "address": "T1", "phone": "555-555-5556", "email": "skt1_zeus@gmail.com", "class": "Tliet"},
    {"id": 3, "name": "b", "age": 19, "address": "T1", "phone": "555-555-5557", "email": "skt1_onner@gmail.com", "class": "Tliet"},
    {"id": 4, "name": "c", "age": 19, "address": "T1", "phone": "555-555-5558", "email": "skt1_killer@gmail.com", "class": "Tliet"},
    {"id": 5, "name": "d", "age": 18, "address": "T1", "phone": "555-555-5559", "email": "skt1_killer@gmail.com", "class": "Tliet"},
]



@app.get("/students")
def get_students():
    return students