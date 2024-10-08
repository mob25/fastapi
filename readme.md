# База данных для интернет-магазина

Задание

Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
- Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
- Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
- Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.

- Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
- Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
- Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.

Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц.
Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.


## Описание

Для наполнения базы данных используются маршруты формата:

http://127.0.0.1:8000/test_users/10
http://127.0.0.1:8000/test_products/10
http://127.0.0.1:8000/test_orders/10

Просмотр данных:

http://127.0.0.1:8000/users/
http://127.0.0.1:8000/products/
http://127.0.0.1:8000/orders/

Для хеширования паролей используется библиотека bcrypt


## Зависимости

Установка зависимостей:

pip install -r requirements.txt


## Запуск проекта

uvicorn main:ap

