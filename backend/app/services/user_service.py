from app.core.database import SessionLocal
from app.models.user import User
from app.services import steam_service
from app.models.user_statistics import UserStatistics


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

def create_user_from_steam(steam_id: int):
    db = SessionLocal()

    existing_user = db.query(User).filter(User.steam_id == str(steam_id)).first()

    if existing_user:
        db.close()
        return None
    steam_user = steam_service.get_player_summary(steam_id)

    user = User(
        steam_id=steam_user["steam_id"],
        nickname=steam_user["nickname"],
        avatar_url=steam_user["avatar_url"]
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()

    return user

def save_user_statistics(steam_id: int):
    db = SessionLocal()

    statistics = steam_service.get_games_statistics(steam_id)

    favorite_game = statistics["favorite_game"]

    user_statistics = UserStatistics(
        steam_id=str(steam_id),
        total_games=statistics["total_games"],
        total_hours=statistics["total_hours"],
        average_hours_per_game=statistics["average_hours_per_game"],
        played_games=statistics["played_games"],
        played_percent=statistics["played_percent"],
        never_played_count=statistics["never_played_count"],
        low_playtime_count=statistics["low_playtime_count"],
        backlog_count=statistics["backlog_count"],
        favorite_game_name=favorite_game["name"] if favorite_game else None,
        favorite_game_hours=favorite_game["hours"] if favorite_game else None
    )

    db.add(user_statistics)
    db.commit()
    db.refresh(user_statistics)
    db.close()

    return user_statistics

