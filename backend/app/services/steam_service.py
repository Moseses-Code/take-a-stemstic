import os
import requests
from dotenv import load_dotenv

load_dotenv()

STEAM_API_KEY = os.getenv("STEAM_API_KEY")

def get_player_summary(steam_id: int):
    url = "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"

    params = {
        "key": STEAM_API_KEY,
        "steamids": steam_id
    }

    response = requests.get(url, params=params)
    data = response.json()

    player = data["response"]["players"][0]

    return {
        "steam_id": player["steamid"],
        "nickname": player["personaname"],
        "avatar_url": player["avatarfull"]
    }

def get_owned_games(steam_id: int):
    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"

    params = {
        "key": STEAM_API_KEY,
        "steamid": steam_id,
        "include_appinfo": True,
        "include_played_free_games": True,
        "format": "json"
    }

    response = requests.get(url, params=params)
    data = response.json()

    games = data["response"].get("games", [])

    return games

def get_games_statistics(steam_id: int):
    games = get_owned_games(steam_id)

    total_games = len(games)
    total_minutes = sum(game["playtime_forever"] for game in games)
    total_hours = round(total_minutes / 60, 1)
    average_hours_per_game = 0

    if total_games > 0:
        average_hours_per_game = round(
        total_hours / total_games,
        1
    )

    top_games_raw = sorted(
    games,
    key=lambda game: game["playtime_forever"],
    reverse=True
)   [:10]

    top_games = [
    {
        "name": game["name"],
        "hours": round(game["playtime_forever"] / 60, 1)
    }
    for game in top_games_raw
]
    favorite_game = None

    if top_games:
        favorite_game = top_games[0]
    never_played_games = [
    {
        "name": game["name"]
    }
    for game in games
    if game["playtime_forever"] == 0
]
    low_playtime_games = [
    {
        "name": game["name"],
        "hours": round(game["playtime_forever"] / 60, 1)
    }
    for game in games
        if 0 < game["playtime_forever"] < 60
]

    low_playtime_count = len(low_playtime_games)

    never_played_count = len(never_played_games)
    backlog_count = never_played_count + low_playtime_count
    played_games = total_games - never_played_count

    played_percent = 0

    if total_games > 0:
        played_percent = round((played_games / total_games) * 100, 1)

    return {
    "total_games": total_games,
    "total_hours": total_hours,
    "average_hours_per_game": average_hours_per_game,
    "top_games": top_games,
    "favorite_game": favorite_game,
    "never_played_count": never_played_count,
    "low_playtime_count": low_playtime_count,
    "backlog_count": backlog_count,
    "low_playtime_games": low_playtime_games,
    "played_games": played_games,
    "played_percent": played_percent,
    "never_played_games": never_played_games
}