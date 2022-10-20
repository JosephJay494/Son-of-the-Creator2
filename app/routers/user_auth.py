from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates



router = APIRouter(include_in_schema=False)

templates = Jinja2Templates(directory="templates")


@router.get("/login")
def user_login(request: Request):
    return templates.TemplateResponse("user_auth.html", {'request': request})