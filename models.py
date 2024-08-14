from datetime import datetime
from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    name: str = Field(max_length=20)
    surname: str = Field(max_length=20)
    email: str = Field(max_length=30)
    password: str = Field(min_length=6)


class UserRead(UserCreate):
    id: int


class ProductCreate(BaseModel):
    title: str = Field(max_length=60)
    description: str = Field(max_length=500)
    price: int = Field(default=0)


class ProductRead(ProductCreate):
    id: int


class OrderCreate(BaseModel):
    user_id: int
    prod_id: int
    date: datetime = Field(default=datetime.now())
    status: str = Field(default="Оплачен")


class OrderRead(OrderCreate):
    id: int


