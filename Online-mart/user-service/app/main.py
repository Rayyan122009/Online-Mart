# main.py
from contextlib import asynccontextmanager
from typing import Union, Optional, Annotated
from app import settings
from sqlmodel import Field, Session, SQLModel, create_engine, select, Sequence
from fastapi import FastAPI, Depends
from typing import AsyncGenerator

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create an instance of FastAPI
app = FastAPI()

# Temporary storage for user data (replace with database integration)
users_db = []

# Model for User data
class User(BaseModel):
    username: str
    email: str
    password: str

# Endpoint for user registration
@app.post("/register/")
def register_user(user: User):
    users_db.append(user)
    return {"message": "User registered successfully"}

# Endpoint for user authentication
@app.post("/login/")
def login_user(username: str, password: str):
    for user in users_db:
        if user.username == username and user.password == password:
            return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

# Endpoint for user profile
@app.get("/profile/{username}")
def get_user_profile(username: str):
    for user in users_db:
        if user.username == username:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Endpoint to delete a user
@app.delete("/delete/{username}")
def delete_user(username: str):
    for idx, user in enumerate(users_db):
        if user.username == username:
            del users_db[idx]
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")


