from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi import Form
from models.db import Text, init_db, sessionLocal
from model_development.model import classifier

template = Jinja2Templates(directory="templates")

app = FastAPI()

init_db()

@app.get("/")
def home(request:Request):
    return template.TemplateResponse(
        request=request,
        name="main.html"
    )

@app.get("/classify")
def classify_text(request:Request):
    return template.TemplateResponse(
        request=request,
        name="upload.html"
    )

@app.post("/classify")
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


