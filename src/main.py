
from fastapi import FastAPI, Request, APIRouter
from routes.base import base_router

app = FastAPI()

app.include_router(base_router)

