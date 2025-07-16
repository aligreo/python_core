
from fastapi import FastAPI
from routes import base_router
from models.db import init_db
from fastapi.staticfiles import StaticFiles

init_db()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(base_router)