from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, validator
import bcrypt

class UserCreate(BaseModel):
    name: str = Field(max_length=20)
    surname: str = Field(max_length=20)
    email: EmailStr
    password: str = Field(min_length=6)
    @validator('password')
    def hash_password(cls, password: str) -> str:
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed.decode('utf-8')


class UserRead(UserCreate):
    id: int


class ProductCreate(BaseModel):
    title: str = Field(max_length=60)
    description: str = Field(max_length=500)
    price: int = Field(gt=0)


class ProductRead(ProductCreate):
    id: int


class OrderCreate(BaseModel):
    user_id: int
    prod_id: int
    date: datetime = Field(default=datetime.now())
    status: str = Field(pattern = r"^(Оплачен|Отменен|В процессе)$")


class OrderRead(OrderCreate):
    id: int


