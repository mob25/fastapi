from fastapi import FastAPI, HTTPException
import database as db
import models
from typing import List
from random import randint
import datetime

app = FastAPI()

@app.get("/")
def root():
    return {"Message": "Hello"}


# пользователи
@app.get("/test_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = db.users.insert().values(name=f'user{i}', surname=f'surname{i}', email=f'mail{i}@mail.ru',
                                         password=f'trtgfv{i}')
        await db.database.execute(query)
    return {'message': f'Создано пользователей - {count}'}


@app.get("/users/", response_model=List[models.UserRead])
async def read_users():
    query = db.users.select()
    return await db.database.fetch_all(query)


@app.get("/users/{user_id}", response_model=models.UserRead)
async def read_user(user_id: int):
    query = db.users.select().where(db.users.c.id == user_id)
    user = await db.database.fetch_one(query)
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user


@app.put("/users/{user_id}", response_model=models.UserRead)
async def update_user(user_id: int, new_user: models.UserCreate):
    query = db.users.update().where(db.users.c.id == user_id).values(**new_user.dict())
    await db.database.execute(query)
    return {**new_user.dict(), "id": user_id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = db.users.delete().where(db.users.c.id == user_id)
    await db.database.execute(query)
    return {'message': 'Пользователь не найден'}


# товары
@app.get("/test_products/{count}")
async def create_note(count: int):
    for i in range(count):
        query = db.products.insert().values(title=f'Товар {i}', description=f'Описание {i}',
                                            price=randint(1, 1000))
        await db.database.execute(query)
    return {'message': f'Создано товаров - {count}'}


@app.get("/products/", response_model=List[models.ProductRead])
async def read_products():
    query = db.products.select()
    return await db.database.fetch_all(query)


@app.get("/products/{product_id}", response_model=models.ProductRead)
async def read_product(product_id: int):
    query = db.products.select().where(db.products.c.id == product_id)
    product = await db.database.fetch_one(query)
    if product is None:
        raise HTTPException(status_code=404, detail="Товар не найден")
    return product


@app.put("/products/{product_id}", response_model=models.ProductRead)
async def update_product(product_id: int, new_product: models.ProductCreate):
    query = db.products.update().where(db.products.c.id == product_id).values(**new_product.dict())
    await db.database.execute(query)
    return {**new_product.dict(), "id": product_id}


@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    query = db.products.delete().where(db.products.c.id == product_id)
    await db.database.execute(query)
    return {'message': 'Товар удален'}


# заказы
@app.get("/test_orders/{count}")
async def create_note(count: int):
    for i in range(count):
        query = db.orders.insert().values(user_id=randint(1, 10), prod_id=randint(1, 10), status="Оплачен",
                                          date=datetime.datetime.now())
        await db.database.execute(query)
    return {'message': f'Создано заказов - {count}'}


@app.get("/orders/", response_model=List[models.OrderRead])
async def read_orders():
    query = db.orders.select()
    return await db.database.fetch_all(query)


@app.get("/orders/{order_id}", response_model=models.OrderRead)
async def read_order(order_id: int):
    query = db.orders.select().where(db.orders.c.id == order_id)
    order = await db.database.fetch_one(query)
    if order is None:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    return order


@app.put("/orders/{order_id}", response_model=models.OrderRead)
async def update_order(order_id: int, new_order: models.OrderCreate):
    query = db.orders.update().where(db.orders.c.id == order_id).values(**new_order.dict())
    await db.database.execute(query)
    return {**new_order.dict(), "id": order_id}


@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = db.orders.delete().where(db.orders.c.id == order_id)
    await db.database.execute(query)
    return {'message': 'Заказ удален'}