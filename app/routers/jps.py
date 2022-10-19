from fastapi import Request, APIRouter,  Response, status, HTTPException, Depends, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app import models , oauth2
from sqlalchemy import func
from typing import  Optional
from sqlalchemy.orm import Session
from  ..database import get_db

 
router = APIRouter(
    include_in_schema=False
)

templates = Jinja2Templates(directory="templates")


@router.get("/")
def page(request: Request, db: Session = Depends(get_db)):
    books =db.query(models.Books).all() 
    return templates.TemplateResponse("index.html", {'request': request, 'books': books} )

@router.get("/book/{id}")
def get_posts(request: Request, id: int, db: Session = Depends(get_db)):
    book = db.query(models.Books).filter(models.Books.id == id).first()
    user = db.query(models.User).filter(models.User.id == book.owner_id).first()
    return templates.TemplateResponse("get_posts.html", {'request': request, 'book': book, "user": user} )