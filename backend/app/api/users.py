from fastapi import APIRouter
from app.services import user_service
from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserUpdate

router = APIRouter()

@router.get("/users")
def get_users():
    return user_service.get_users()

@router.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    user = user_service.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(
        status_code=404,
        detail="Пользователь не найден"
        )
    return user

@router.post("/users")
def create_user(new_user: UserCreate):
    user = user_service.create_user(new_user)
    return user

@router.delete("/users/{user_id}")
def delete_user_by_id(user_id: int):
    user = user_service.delete_user(user_id)
    if user is None:
        raise HTTPException(
        status_code=404,
        detail="Пользователь не найден"
        )
    return user

@router.put("/users/{user_id}")
def update_user_by_id(user_id: int, user_data: UserUpdate):
    user = user_service.update_user(user_id, user_data)
    if user is None:
        raise HTTPException(
        status_code=404,
        detail="Пользователь не найден"
        )
    return user