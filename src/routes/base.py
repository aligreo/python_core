#fastapi imports
from fastapi import FastAPI, Request, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Form
from fastapi.staticfiles import StaticFiles

# project imports
from models.db import Text, init_db, sessionLocal
from model_development.model import classifier


template = Jinja2Templates(directory="templates")

base_router = APIRouter()
base_router.mount("/static", StaticFiles(directory="static"), name="static")

init_db()

@base_router.get("/")
def home(request:Request):
    return template.TemplateResponse(
        request=request,
        name="main.html"
    )

@base_router.get("/classify")
def classify_text(request:Request):
    return template.TemplateResponse(
        request=request,
        name="upload.html"
    )

@base_router.post("/classify")
def get_user_text(request:Request, content:str = Form(...)):
    success = False
    if len(content) > 0:
        db = sessionLocal()
        new_db_row = Text(content=content)
        db.add(new_db_row)
        db.commit()
        db.refresh(new_db_row)
        db.close()
        success = True
    if content:
        result = classifier(content)[0]
        print(result)
    return template.TemplateResponse(
        request=request,
        name="main.html",
        context={
            "request": request,
            "message":"texd added successfully",
            "label": result['label'],
            "score": result['score'],
            "success": success}
    )
