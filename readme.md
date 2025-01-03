# Nguyễn Đình Thái
# A simple backend system using DJANGO and DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.
## Server url: http://43.203.217.22:8000/
## Swagger API documentation for the CRM system: http://43.203.217.22:8000/api-doc/api/schema/swagger-ui/
## Deployments & tools
- AWS
- docker
## Requirements
- Python 3.11
- Django 5.1.4
- Django REST Framework

## Installation and Set up Project
1. Running the project on a local environment
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command
```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
2. Running the project using Docker
Docker provides a modern approach, allowing you to run the project inside an isolated container environment
```
docker compose up -d --build
```
## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.
Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`/authentication/signin/` | POST | - | Status, Accesstoken and refreshtoken
`/authentication/signup/` | POST | - | Status
-- | -- |-- |--
`/crm/customers/` | GET | READ | Get all customers
`/crm/customers/:id/` | GET | READ | Get a single customer
`/crm/customers/`| POST | CREATE | Create a new customer
`/crm/ustomers/:id/` | PUT | UPDATE | Update a customer
`/crm/customers/:id/` | DELETE | DELETE | Delete a customer
-- | -- |-- |--
`/crm/products/` | GET | READ | Get all products
`/crm/products/:id/` | GET | READ | Get a single product
`/crm/products/`| POST | CREATE | Create a new product
`/crm/products/:id/` | PUT | UPDATE | Update a product
`/crm/products/:id/` | DELETE | DELETE | Delete a product
-- | -- |-- |--
`/crm/employees/` | GET | READ | Get all employees
`/crm/employees/:id/` | GET | READ | Get a single employee
`/crm/employees/`| POST | CREATE | Create a new employee
`/crm/employees/:id/` | PUT | UPDATE | Update a employee
`/crm/employees/:id/` | DELETE | DELETE | Delete a employee
-- | -- |-- |--
`/crm/task-board/` | GET | READ | Get all tasks
`/crm/task-board/:id/` | GET | READ | Get a single task
`/crm/task-board/`| POST | CREATE | Create a new task
`/crm/task-board/:id/` | PUT | UPDATE | Update a task
`/crm/task-board/:id/` | DELETE | DELETE | Delete a task

## Use
We can test the API using [Postman](https://www.postman.com/) or click to swagger doc link: http://43.203.217.22:8000/api-doc/api/schema/swagger-ui

First, we have to start up Django's development server.
```
python manage.py runserver
```
Only authenticated users can use the API services, for that reason if we try this:
```
http  http://127.0.0.1:8000/crm/customers/
```
we get:
```
{
    "detail": "Authentication credentials were not provided."
}
```
Instead, if we try to access with credentials:
```
http http://127.0.0.1:8000/crm/customers/1/ "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQxMDcyNDE0LCJpYXQiOjE3MzU4ODg0MTQsImp0aSI6ImU2YTQ3MDI4ZDk2MzRmYmQ5MGEzZjY3ZmRjZDkwYjBmIiwidXNlcl9pZCI6MX0.a6MQjjgJxfpIfY_UzUhJkuiWewfpro60EXziUDRQi9M"
```
we get the movie with id = 1
```
{
  "id": 1,
  "name": "testuser",
  "email": "test@gmail.com",
  "phone": "9999999999999",
  "address": "test",
  "notes": "test"
}
```

## Create users and Tokens

First we need to create a user, so we can log in
```
http POST http://43.203.217.22:8000/authentication/signup/
params:
{
  "username": "testuser",
  "email": "user@gmail.com",
  "password1": "testpassword",
  "password2": "testpassword"
}
```

After we create an account we can login to get a token

To get a token first we need to request
```
http POST http://43.203.217.22:8000/authentication/signin/
params:
{
  "username_login": "admin",
  "password_login": "admin",
  "next": "/dashboard/"
}
```
after that, we get the token
```
{
  "success": true,
  "next_page": "/dashboard/",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczNTk3NDgxNCwiaWF0IjoxNzM1ODg4NDE0LCJqdGkiOiIwNGVmODBmMzMxMGE0YmJmYjZjZWNhNjBjOTc3ZWQ5MiIsInVzZXJfaWQiOjF9.KzIQVq9UX7DVxemoQK4gv2NVJHVe6OirlJ9NuXTmr9w",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQxMDcyNDE0LCJpYXQiOjE3MzU4ODg0MTQsImp0aSI6ImU2YTQ3MDI4ZDk2MzRmYmQ5MGEzZjY3ZmRjZDkwYjBmIiwidXNlcl9pZCI6MX0.a6MQjjgJxfpIfY_UzUhJkuiWewfpro60EXziUDRQi9M"
}
```
We got two tokens, the access token will be used to authenticated all the requests we need to make, this access token will expire after some time.

The API has some restrictions:
-   Only authenticated users may use these CRUD api

### Request using postman
#### Authentication
#### Signin
```
url:POST http://127.0.0.1:8000/authentication/signin/
params:
{
  "username_login": "testuser",
  "password_login": "testpassword",
  "next": "/dashboard/"
}
response:
{
  "success": true,
  "next_page": "/dashboard/",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczNTk4MjMyNCwiaWF0IjoxNzM1ODk1OTI0LCJqdGkiOiIyMTU5ZWZmY2ZlZTc0NWIyYmQ1ODkzY2Q0NDgxMDUyNCIsInVzZXJfaWQiOjF9.MMpjtJkal2nvp5zgeNn8UZHM7drc6-wlvqiuo-kyD_s",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQxMDc5OTI0LCJpYXQiOjE3MzU4OTU5MjQsImp0aSI6ImE2ZjE0NmQ3MGVlYTQ5ODBiZTlmMzZhZjg1NWFmOWRhIiwidXNlcl9pZCI6MX0.BzAiRsCmKpjxaiDlTD8byHHzqaZ6cGJI_W-rKr4zGkQ"
}
```
#### Signup
```
url:POST http://127.0.0.1:8000/authentication/signup/
params:
{
  "username": "testuser",
  "email": "user@gmail.com",
  "password1": "testpassword",
  "password2": "testpassword"
}
response:
{
  "success": true,
  "message": "Sign up successful!"
}
```
#### All these api must have Authorization: Bearer {YOUR_TOKEN}
#### Get all customers
```
url:GET http://127.0.0.1:8000/crm/customers/
response:
[
  {
    "id": 1,
    "name": "testuser",
    "email": "test@gmail.com",
    "phone": "9999999999999",
    "address": "test",
    "notes": "test"
  }
]
```
#### Get a single customer
```
url:GET http://127.0.0.1:8000/crm/customers/[id]/
response:
{
  "id": 1,
  "name": "testuser",
  "email": "test@gmail.com",
  "phone": "9999999999999",
  "address": "test",
  "notes": "test"
}
```
#### Create a new customer
```
url:POST http://127.0.0.1:8000/crm/customers/
params:
{
  "name": "string",
  "email": "user@example.com",
  "phone": "string",
  "address": "string",
  "notes": "string"
}
response:
{
  "id": 0,
  "name": "string",
  "email": "user@example.com",
  "phone": "string",
  "address": "string",
  "notes": "string"
}
```
#### Full update a customer
```
url:PUT http://127.0.0.1:8000/crm/customers/[id]/
params:
{
  "name": "testuser2",
  "email": "test@gmail.com",
  "phone": "9999999999999",
  "address": "test",
  "notes": "test"
}
response:
{
  "id": 1,
  "name": "testuser2",
  "email": "test@gmail.com",
  "phone": "9999999999999",
  "address": "test",
  "notes": "test"
}
```
#### Delete a customer
```
http:DELETE \http://127.0.0.1:8000/crm/customers/[id]/
----------------------------------------------------------------------------------------------------------------------------------------------------
```
#### Get all products
```
url:GET http://127.0.0.1:8000/crm/products/
response:
[
  {
    "id": 1,
    "name": "testproduct",
    "description": "test",
    "price": "1.00",
    "stock": 1
  }
]
```
#### Get a single product
```
url:GET http://127.0.0.1:8000/crm/products/[id]/
response:
{
  "id": 1,
  "name": "testproduct",
  "description": "test",
  "price": "1.00",
  "stock": 1
}
```
#### Create a new product
```
url:POST http://127.0.0.1:8000/crm/products/
params:
{
  "name": "string",
  "description": "string",
  "price": "246",
  "stock": 4294967295
}
response:
{
  "id": 2,
  "name": "string",
  "description": "string",
  "price": "246.00",
  "stock": 4294967295
}
```
#### Full update a product
```
url:PUT http://127.0.0.1:8000/crm/products/[id]/
params:
{
  "name": "testproduct2",
  "description": "test",
  "price": "1.00",
  "stock": 1
}
response:
{
  "id": 1,
  "name": "testproduct2",
  "description": "test",
  "price": "1.00",
  "stock": 1
}
```
#### Delete a product
```
http:DELETE \http://127.0.0.1:8000/crm/products/[id]/
----------------------------------------------------------------------------------------------------------------------------------------------------
```
#### Get all employees
```
url:GET http://127.0.0.1:8000/crm/employees/
response:
[
  {
    "id": 1,
    "name": "testemployee",
    "email": "test2@gmail.com",
    "phone": "11111111111111",
    "position": "test"
  }
]
```
#### Get a single employees
```
url:GET http://127.0.0.1:8000/crm/employees/[id]/
response:
{
  "id": 1,
  "name": "testemployee",
  "email": "test2@gmail.com",
  "phone": "11111111111111",
  "position": "test"
}
```
#### Create a new employees
```
url:POST http://127.0.0.1:8000/crm/employees/
params:
{
  "name": "strieng",
  "email": "user@exampele.com",
  "phone": "string",
  "position": "string"
}
response:
{
  "id": 3,
  "name": "strieng",
  "email": "user@exampele.com",
  "phone": "string",
  "position": "string"
}
```
#### Full update a employees
```
url:PUT http://127.0.0.1:8000/crm/employees/[id]/
params:
{
  "name": "strieng3",
  "email": "user@exampele.com",
  "phone": "string",
  "position": "string"
}
response:
{
  "id": 3,
  "name": "strieng3",
  "email": "user@exampele.com",
  "phone": "string",
  "position": "string"
}
```
#### Delete a employees
```
http:DELETE \http://127.0.0.1:8000/crm/employees/[id]/
----------------------------------------------------------------------------------------------------------------------------------------------------
```
#### Get all tasks-board
```
url:GET http://127.0.0.1:8000/crm/task-board/
response:
[
  {
    "id": 1,
    "name": "testtask",
    "description": "test",
    "position": 0,
    "due_date": "2025-01-03",
    "status": "Open",
    "column": 1,
    "assigned_to": 1
  }
]
```
#### Get a single task-board
```
url:GET http://127.0.0.1:8000/crm/task-board/[id]/
response:
{
  "id": 1,
  "name": "testtask",
  "description": "test",
  "position": 0,
  "due_date": "2025-01-03",
  "status": "Open",
  "column": 1,
  "assigned_to": 1
}
```
#### Create a new task-board
```
url:POST http://127.0.0.1:8000/crm/task-board/
params:
{
  "name": "string",
  "description": "string",
  "position": 4294967295,
  "due_date": "2025-01-03",
  "status": "Open",
  "column": 1,
  "assigned_to": 1
}
response:
{
  "id": 2,
  "name": "string",
  "description": "string",
  "position": 4294967295,
  "due_date": "2025-01-03",
  "status": "Open",
  "column": 1,
  "assigned_to": 1
}
```
#### Full update a task-board
```
url:PUT http://127.0.0.1:8000/crm/task-board/[id]/
params:
{
  "name": "string2",
  "description": "string",
  "position": 4294967295,
  "due_date": "2025-01-03",
  "status": "Open",
  "column": 1,
  "assigned_to": 1
}
response:
{
  "id": 2,
  "name": "string2",
  "description": "string",
  "position": 4294967295,
  "due_date": "2025-01-03",
  "status": "Open",
  "column": 1,
  "assigned_to": 1
}
```
#### Delete a task-board
```
http:DELETE \http://127.0.0.1:8000/crm/task-board/[id]/
----------------------------------------------------------------------------------------------------------------------------------------------------
```
### Filters
#### The API task-board filtering, you can filter by the attributes of a task-board like this
Filter base on assigned_to field and status field
```
url:GET http://127.0.0.1:8000/crm/task-board/?assigned_to=[user_id]&?status=open
response:
[
  {
    "id": 1,
    "name": "testtask",
    "description": "test",
    "position": 0,
    "due_date": "2025-01-03",
    "status": "Open",
    "column": 1,
    "assigned_to": 1
  },...
]
```
```

