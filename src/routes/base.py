from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi import Form
from fastapi import APIRouter
from models.db import Text, init_db, sessionLocal

template = Jinja2Templates(directory="templates")

base_router = APIRouter()

@base_router.get("/")
def home(request:Request):
    return template.TemplateResponse(
        request=request,
        name="main.html"
    )

@base_router.get("/upload")
def upload(request:Request):
    return template.TemplateResponse(
        request=request,
        name="upload.html"
    )

@base_router.post("/upload")
def get_user_text(request:Request, content:str = Form(...)):
    if len(content) > 0:
        db = sessionLocal()
        new_db_row = Text(content=content)
        db.add(new_db_row)
        db.commit()
        db.refresh(new_db_row)
        db.close()
        
    return template.TemplateResponse(
        request=request,
        name="upload.html",
        context={"request": request, "message":"texd added successfully"}
    )