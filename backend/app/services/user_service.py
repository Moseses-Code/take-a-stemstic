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