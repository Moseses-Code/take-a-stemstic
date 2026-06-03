from fastapi import APIRouter
from app.services import steam_service
from app.services import user_service

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