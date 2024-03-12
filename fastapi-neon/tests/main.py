# fastapi_neon/main.py

from typing import Union

from fastapi import FastAPI



app = FastAPI()



@app.get("/")

def read_root():

    return {"Hello": "jigar"}



@app.get("/items/{item_id}")

def read_item(item_id: str, q: Union[str, None] = None):

    return {"item_id": item_id, "q": q}