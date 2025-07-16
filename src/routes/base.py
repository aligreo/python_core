from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi import Form
from fastapi import APIRouter


from model_develoment.model import get_sentiment
from models.db import Text, sessionLocal

template = Jinja2Templates(directory="templates")

base_router = APIRouter()

@base_router.get("/")
def home(request:Request):
    return template.TemplateResponse(
        request=request,
        name="main.html"
    )

@base_router.get("/get_sentiment")
def upload(request:Request):
    return template.TemplateResponse(
        request=request,
        name="sentiment.html"
    )

@base_router.post("/get_sentiment")
def get_user_text(request:Request, content:str = Form(...)):
    if len(content) > 0:
        db = sessionLocal()
        new_db_row = Text(content=content)
        db.add(new_db_row)
        db.commit()
        db.refresh(new_db_row)
        db.close()
    if content:
        result = get_sentiment(text=content)
        
    return template.TemplateResponse(
        request=request,
        name="sentiment.html",
        context={"request": request,
                 "message":"texd added successfully",
                 "label": result}
        )