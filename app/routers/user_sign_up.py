from urllib import response
from fastapi import Request, APIRouter, status, HTTPException, Depends, APIRouter, responses
from fastapi.templating import Jinja2Templates
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.database import get_db

from app.models import User
from ..hashing import Hasher


router = APIRouter(include_in_schema=False)

templates = Jinja2Templates(directory="templates")

@router.get("/register")
def Sign_up(request: Request):
    return templates.TemplateResponse("user_sign_up.html", {'request': request} )

@router.post("/register")
async def Sign_up(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    email = form.get("email")
    password = form.get("password")
    errors = []
    if len (password) < 6:
        errors.append("Password should be > 6 characters")
        return templates.TemplateResponse("user_sign_up.html", {'request': request, "errors": errors} )

    user = User(email=email, password=Hasher.get_hash_password(password))
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return responses.RedirectResponse("/?msg=Successfully Registered", status_code = status.HTTP_302_FOUND)
    except IntegrityError:
        errors.append("Email already exist")
        return templates.TemplateResponse("user_sign_up.html", {'request': request, "errors": errors} )