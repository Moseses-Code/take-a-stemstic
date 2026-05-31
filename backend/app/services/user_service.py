from app.core.database import SessionLocal
from app.models.user import User


def get_users():
    db = SessionLocal()
    get_user = db.query(User).all()
    db.close()
    return get_user

def get_user_by_id(user_id):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    return user

def create_user(user_data):
    db = SessionLocal()
    user = User(
        steam_id = user_data.steam_id,
        nickname = user_data.nickname,
        avatar_url = user_data.avatar_url
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user

def delete_user(user_id):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        db.close()
        return None
    db.delete(user)
    db.commit()
    db.close()
    return {
        "message": "Пользователь удален!"
    }

def update_user(user_id, user_data):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        db.close()
        return None
    user.steam_id = user_data.steam_id
    user.nickname = user_data.nickname
    user.avatar_url = user_data.avatar_url
    db.commit()
    db.refresh(user)
    db.close()
    return user