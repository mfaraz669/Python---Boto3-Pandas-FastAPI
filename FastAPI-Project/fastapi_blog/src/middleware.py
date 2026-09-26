from fastapi import FastAPI, Request
import time
app = FastAPI()

@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    print("Request Received")
    response = await call_next(request)
    print("Response Received")
    return response

#logging monitor time to tracker each api how much time they will take
@app.middleware("http")
async def log_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Path:{request.url.path} | Time: {process_time}")
    return response
