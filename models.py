from datetime import datetime
from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    name: str = Field(max_length=20)
    surname: str = Field(max_length=20)
    email: str = Field(max_length=30)
    password: str = Field(min_length=6)


class UserRead(UserCreate):
    id: int
