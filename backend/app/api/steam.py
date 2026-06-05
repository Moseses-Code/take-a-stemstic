from fastapi import APIRouter
from app.services import steam_service
from app.services import user_service
from fastapi import HTTPException

router = APIRouter()


@router.get("/steam/profile/{steam_id}")
def get_steam_profile(steam_id: int):
    return steam_service.get_player_summary(steam_id)

@router.get("/steam/games/{steam_id}")
def get_steam_games(steam_id: int):
    return steam_service.get_owned_games(steam_id)

@router.get("/steam/statistics/{steam_id}")
def get_steam_statistics(steam_id: int):
    return steam_service.get_games_statistics(steam_id)

@router.post("/steam/statistics/save/{steam_id}")
def save_steam_statistics(steam_id: int):
    return user_service.save_user_statistics(steam_id)

@router.post("/steam/games/save/{steam_id}")
def save_steam_games(steam_id: int):
    return user_service.save_user_games(steam_id)

@router.get("/statistics/{steam_id}")
def get_statistics(steam_id: int):
    statistics = user_service.get_user_statistics(steam_id)

    if statistics is None:
        raise HTTPException(
            status_code=404,
            detail="Статистика не найдена"
        )

    return statistics

@router.get("/games/{steam_id}")
def get_user_games(steam_id: int):
    games = user_service.get_user_games(steam_id)

    if not games:
        raise HTTPException(
            status_code=404,
            detail="Игры пользователя не найдены"
        )

    return games

@router.post("/sync/{steam_id}")
def sync_user_data(steam_id: int):
    return user_service.sync_user_data(steam_id)