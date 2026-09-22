from fastapi import FastAPI, Request
from pydantic import BaseModel

#source-youtube : https://www.youtube.com/watch?v=fxRCoEUmq8s&t=1147s
app = FastAPI()

@app.get("/")
def Home():
    return {"Hello": "World"}

@app.get("/demo")
def Demo():
    return {"Hello": "World1"}

@app.get("/about")
def About():
    return {"This is the about page"}

@app.get("/users")
def Users():
    return {
        "users":["Faraz", "Arham", "Zeenath", "Inaya"]
    }
#PATH PARAMETERS --- Dynamic routing
@app.get("/emplid/{empl_id}")
def Emplid(empl_id):
    return {"empl_id": empl_id}

#take integer only as output - Data Types
@app.get("/id/{id}")
def ID(id:int):
    return {"id": id}

#Query Parameter -- eg: query_user?name=faraz
@app.get("/query_user")
def QueryUser(name):
    return {"query_user": name}

#default value in query parameters/ customize one- eg:http://127.0.0.1:8000/products?limit=23
@app.get("/products")
def Products(limit:int=10):
    return {"limit": limit}

#multiple query parameter eg:http://127.0.0.1:8000/items?price=100000&name=samsung
@app.get("/items")
def Items(name: str=None, price: int=0):
    return {
        "name": name,
        "price": price,
    }

#Request body - POST >>> This will not work in browser, you have to go in swagger api
@app.post("/create_user")
def create_user(name:str, age:int):
    return {
        "name": name,
        "age": age
    }

# POST - in dict
@app.post("/user_create")
def user_create(user: dict):
    return {
        "message": "User created successfully",
        "user": user
    }

#Pydantic is used in FastAPI to automatically validate, parse, and document API
# request and response data using standard Python type hints

class Seq(BaseModel):
    name: str
    age: int
@app.post("/seq")
def seq(seq: Seq):
    return {
        "message": "Sequence created successfully",
        "seq": seq
    }

class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/user")
def user(user: User):
    return {
        "message": "User created successfully",
        "data": user
    }

#nested model
class Address(BaseModel):
    city: str
    pincode: int

class Person(BaseModel):
    name: str
    age: int
    address: Address

@app.post("/person")
def person(person: Person):
    return Person








