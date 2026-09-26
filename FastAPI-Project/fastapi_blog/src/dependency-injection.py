from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

def common_logic():
    return {
        "message": "common logic executed successfully"
    }
@app.get("/home")
def home(data = Depends(common_logic)):
    return data

#reusable logic
def user_profile():
    return {
        "username": "Guest"
    }
@app.get("/profile")
def user_profile(data = Depends(user_profile)):
    return data

@app.get("/Dashboard")
def dashboard(data = Depends(user_profile)):
    return data

@app.get("/loginpage")
def login_page(data = Depends(user_profile)):
    return data

def verify_token(token: str = Header(None)):
    if token != "mytoken":
        raise HTTPException(status_code=401, detail="Invalid Token")
    return {
        "user": "Authorized Successfully"
    }
@app.get("/secure")
def secure(data = Depends(verify_token)):
    return data

