from fastapi import APIRouter
from fastapi import Request
from fastapi import Response

from models.user import RegisterValidator

router = APIRouter(
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/api/current_user")
def get_user(request: Request):
    return request.cookies.get("X-Authorization")


@router.post("/api/register")
def register_user(user: RegisterValidator, response: Response):
    response.set_cookie(key="X-Authorization", value=user.username, httponly=True)

