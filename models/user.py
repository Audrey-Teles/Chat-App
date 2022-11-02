from pydantic import BaseModel


class RegisterValidator(BaseModel):
    username: str

    class Config:
        orm_mode = True
