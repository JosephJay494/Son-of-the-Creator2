from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter(
    include_in_schema=False
)

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def page(request: Request):
    context= {'request': request}
    return templates.TemplateResponse("index.html", context)