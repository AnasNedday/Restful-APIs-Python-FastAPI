from fastapi import FastAPI 
from models import User, Gender, Role
from typing import List
from uuid import uuid4

app = FastAPI()

db: List[User] = [
    User(id=uuid4(),
    first_name="Ibtissam",
    last_name="Mekkaoui",
    middle_name="",
    gender=Gender.female,
    roles=[Role.student]
    ),
    User(id=uuid4(),
    first_name="Anas",
    last_name="Nedday",
    middle_name="",
    gender=Gender.male,
    roles=[Role.admin]
    )

]


@app.get("/")
async def root():
    return {"Hello": "Mundo"}


@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

