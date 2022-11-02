from fastapi import Request
from fastapi import APIRouter
from starlette.templating import Jinja2Templates

router = APIRouter(
    tags=["chat"],
    responses={404: {"description": "Not found"}},
)
# locate templates
templates = Jinja2Templates(directory="templates")


@router.get("/")
def get_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@router.get("/chat")
def get_chat(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})
