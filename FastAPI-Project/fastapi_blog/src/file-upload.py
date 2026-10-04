from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
import os, shutil

app = FastAPI()

#Step-1 - Ensure upload folder exists
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

#Step-2 Setting up statis file
#URL  - HTTP://127.0.0.1:8080/files/<filename>
app.mount("/files", StaticFiles(directory=UPLOAD_FOLDER), name="files")

#Step - 3 - Upload file API
@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    if not filename:
        raise HTTPException(status_code=404, detail="File not found")
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

        return {
            "message": "File successfully uploaded",
            "filename": filename,
            "file_url": f"http://127.0.0.1:8000/files/{filename}"
        }
#Step - 4 Get file url API
@app.get("/files/{filename}")
def get_file(filename: str):
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return {
        "file_url": f"http://127.0.0.1:8000/files/{filename}"
    }

@app.get("/")
def home():
    return {"message": "Upload file API"}

