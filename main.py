from fastapi import FastAPI
from apps import models
from apps.database import engine, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}
