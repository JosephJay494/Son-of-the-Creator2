from fastapi import Request, APIRouter, Depends, Response
from sqlalchemy import false
from sqlalchemy.orm import Session
from ..database import get_db
from fastapi.templating import Jinja2Templates
from app import models
from ..hashing import Hasher
from jose import jwt
from ..config import settings




router = APIRouter(include_in_schema=False)

templates = Jinja2Templates(directory="templates")


@router.get("/logup")
def user_login(request: Request):
    return templates.TemplateResponse("user_auth.html", {'request': request})

@router.post("/logup")
async def user_login(request: Request, response: Response, db: Session = Depends(get_db)):
    form = await request.form()
    email = form.get("email")
    password = form.get("password")
    errors = []
    if not email:
        errors.append("Please enter an invalid email!!")
    if not password or len(password)< 6:
        errors.append("Password should be > 6 chars")

    try: 
        user = db.query(models.User).filter(models.User.email==email).first()
        if user is None:
            errors.append("Email does not exist")

            return templates.TemplateResponse("user_auth.html", {'request': request, "errors": errors} )
        else:
            if Hasher.verify_password(password,user.password):
                data = {"sub":email}
                jwt_token = jwt.encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHN)
                response.set_cookie(key="access_token", value=f"Bearer {jwt_token}", httponly=True)
                msg = "Login Successfully"
                return templates.TemplateResponse("user_auth.html", {'request': request, "msg":msg })
            else:
                errors.append("Invalid Password")
                return templates.TemplateResponse("user_auth.html", {'request': request, "errors": errors})
    except:
        errors.append("Invalid Credentials")
        return templates.TemplateResponse("user_auth.html", {'request': request, "errors": errors})

    