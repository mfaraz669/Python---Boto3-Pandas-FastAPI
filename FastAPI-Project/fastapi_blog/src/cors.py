from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

#Allowed origins (Front end url)
origins = [
    "http://localhost:5173/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins =origins, #allowing frontend
    allow_credentials=True,
    allow_methods=["*"], #Get PUT , DELETE, UPDATE
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "CORS ENABLE API"
    }