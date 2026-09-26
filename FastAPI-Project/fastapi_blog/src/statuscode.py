from fastapi import FastAPI, status, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()
@app.post("/create_user", status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "User created"
    }

@app.get("/user")
def get_user():
    return{
        "status": "Success",
        "message": "Users found",
        "data":{
            "name": "Faraz",
            "age": 28
        }
    }

#http exception
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,)

    return {
        "id": 1,
        "name": "Faraz"
    }

@app.get("/emplid/{user_id}")
def get_users(user_id: int):
    if user_id != 2:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,)

    return {
        "id": 2,
        "name": "Smith"
    }
#customer exceptions
class UserNotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name

#global error handling
@app.exception_handler(UserNotFoundException)
def user_not_found_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
           "status": "error",
           "message": f"User {exc.name} not found"
        }
    )

@app.get("/eid/{user_name}")
def get_user(user_name: str):
    if user_name != "faraz":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,)
    return {
        "name": "Faraz"
    }

