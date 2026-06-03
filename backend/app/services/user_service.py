from app.core.database import SessionLocal
from app.models.user import User
from app.services import steam_service
from app.models.user_statistics import UserStatistics
from app.models.game import Game
from app.models.user_game import UserGame


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

def save_user_games(steam_id: int):
    db = SessionLocal()

    games = steam_service.get_owned_games(steam_id)

    saved_games = []

    for game_data in games:
        steam_app_id = game_data["appid"]
        name = game_data["name"]
        hours = round(game_data["playtime_forever"] / 60, 1)

        game = db.query(Game).filter(Game.steam_app_id == steam_app_id).first()

        if game is None:
            game = Game(
                steam_app_id=steam_app_id,
                name=name
            )

            db.add(game)

        existing_user_game = db.query(UserGame).filter(
            UserGame.steam_id == str(steam_id),
            UserGame.steam_app_id == steam_app_id
        ).first()

        if existing_user_game:
            existing_user_game.hours = hours
        else:
            user_game = UserGame(
                steam_id=str(steam_id),
                steam_app_id=steam_app_id,
                hours=hours
            )

            db.add(user_game)

        saved_games.append({
            "name": name,
            "hours": hours
        })

    db.commit()
    db.close()

    return {
        "steam_id": steam_id,
        "saved_games_count": len(saved_games),
        "saved_games": saved_games
    }


def get_user_statistics(steam_id: int):
    db = SessionLocal()
    statistics = db.query(UserStatistics).filter(UserStatistics.steam_id == str(steam_id)).first()
    db.close()
    return statistics

def get_user_games(steam_id: int):
    db = SessionLocal()

    user_games = db.query(UserGame).filter(
        UserGame.steam_id == str(steam_id)
    ).all()

    result = []

    for user_game in user_games:
        game = db.query(Game).filter(
            Game.steam_app_id == user_game.steam_app_id
        ).first()

        result.append({
            "steam_app_id": user_game.steam_app_id,
            "name": game.name if game else "Unknown game",
            "hours": user_game.hours
        })

    db.close()

    return result

def sync_user_data(steam_id: int):
    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.steam_id == str(steam_id)
    ).first()

    db.close()

    if existing_user is None:
        user = create_user_from_steam(steam_id)
    else:
        user = existing_user

    statistics = save_user_statistics(steam_id)
    games = save_user_games(steam_id)

    return {
        "message": "Синхронизация завершена",
        "user": user,
        "statistics": statistics,
        "games_saved": games["saved_games_count"]
    }