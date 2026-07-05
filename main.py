from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app=FastAPI()
class tea(BaseModel):
    id: int
    name: str
    origin: str
teas: List[tea]=[]

@app.get("/")
def read_root():
    return {"message": "welcome to the tea API. Nibedita Roy, I am a very cute girl."}

@app.get("/teas")
def get_teas():
    return teas

@app.post("/teas")
def add_tea(tea: tea):
    teas.append(tea)
    return teas

@app.put("/teas/{tea_id}")
def update_tea(tea_id:int, updated_tea:tea):
    for index,tea in enumerate(teas):
        if tea.id==tea_id:
            teas[index]=updated_tea
            return updated_tea
    return{"error":"tea not found."}
