from xmlrpc.client import Boolean

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy import create_engine, Column, Integer, String
app = FastAPI()

# Database URL
DATABASE_URL = "sqlite:///./test.db"

# Engine create (DB connection)
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
# Session (DB operations ke liye)
SessionLocal = sessionmaker(bind=engine)

# Base (model ke liye)
Base = declarative_base()

# Table (Model)
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    completed = Column(String)


# Table create
Base.metadata.create_all(bind=engine)


# Dependency (DB session provide karega)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todos")
def create_todo(title: str, author: str, db:Session = Depends(get_db)):
    todo = Todo(title=title, author=author, completed= "False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "message": "Todo created successfully",
        "data": todo
    }

#Read ALL Data
@app.get("/todos")
def read_todos(db:Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return {
        "Total": len(todos),
        "data": todos,
        "message": "All todos data fetched successfully"
    }

#fetched data as per particular id
@app.get("/todos/{todo_id}")
def read_todo(todo_id:int, db:Session = Depends(get_db)):
    todo = db.query(Todo).filter_by(id=todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

#updated data
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, title: str, author: str, completed: str, db:Session = Depends(get_db)):
    todo = db.query(Todo).filter_by(id=todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail= "Todo not found")

    todo.title = title
    todo.author = author
    todo.completed = completed
    db.commit()
    db.refresh(todo)
    return {
        "message": "todo updated successfully",
        "data": todo
    }

#delete operation
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db:Session = Depends(get_db)):
    todo = db.query(Todo).filter_by(id=todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()

    return {
        "message": "todo deleted successfully",
    }
