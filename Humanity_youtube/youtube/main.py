from fastapi import FastAPI
from typing import Optional
from sqlmodel import SQLModel, create_engine,Field , Session
from pydantic import BaseModel
from fastapi import HTTPException


class Todos(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    content : str
    is_complete : bool = Field(default=False)

class User_Data():
    content : str
    is_complete : bool = False




db_url='postgresql://neondb_owner:tq7ZJOIDn9kC@ep-shrill-mode-a5fftd37.us-east-2.aws.neon.tech/ToDo_Next?sslmode=require'

engine = create_engine(db_url , echo = True)

def create_table():
    SQLModel.metadata.create_all(engine)

def inser_data_into_table(content : str):
    with Session(engine) as session:
        data : Todos  = Todos(content = "coding")
        session.add(data)
        session.commit()

     


app = FastAPI(
    title= "Practic ToDo App"
)
@app.get("/")
def read_root():
    return {"message" : "To Do App"}

@app.post("/todos")
def add_todos(user_todos : User_Data):
    if user_todos:
        return{"message" : "Todos Add successfully"}
    else:
        raise HTTPException(status_code=404, detail="Todos not found")

