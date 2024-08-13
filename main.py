from fastapi import FastAPI
import database as db
import models
from typing import List

app = FastAPI()

@app.get("/")
def root():
    return {"Message": "Hello"}

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