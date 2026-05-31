from fastapi import APIRouter
from app.services import user_service
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/users")
def get_users():
    return user_service.get_users()

@router.get("/users/{user_id}")
def get_user_by_id(user_id):
    user = user_service.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(
        status_code=404,
        detail="Пользователь не найден"
        )
    return user