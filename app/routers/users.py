from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Fake database (list in memory)
users_db = []

# Define a user schema
class User(BaseModel):
    name: str
    email: str

# Create a user
@router.post("/")
def create_user(user: User):
    users_db.append(user)
    return {"message": "User created successfully", "user": user}

# Get all users
@router.get("/")
def get_users():
    return users_db

