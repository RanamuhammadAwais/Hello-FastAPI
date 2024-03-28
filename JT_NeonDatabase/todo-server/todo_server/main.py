from fastapi import FastAPI


todo_server: FastAPI = FastAPI()

from todo_server import settings



@todo_server.get("/")
def helo():
    return {"message": "Hello bahi"}


@todo_server.get("/db")
def db():
    return {"DB": settings.DATABASE_URL}