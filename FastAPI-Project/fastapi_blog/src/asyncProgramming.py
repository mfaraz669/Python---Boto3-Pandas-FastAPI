from fastapi import FastAPI
import time, asyncio

app = FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(3)
    return {
        "message": "Async API"
    }
