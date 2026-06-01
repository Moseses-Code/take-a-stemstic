from sqlalchemy import Column, Integer, Float, String
from app.core.database import Base


class UserStatistics(Base):
    __tablename__ = "user_statistics"

    id = Column(Integer, primary_key=True, index=True)

    steam_id = Column(String, index=True)

    total_games = Column(Integer)
    total_hours = Column(Float)
    average_hours_per_game = Column(Float)

    played_games = Column(Integer)
    played_percent = Column(Float)

    never_played_count = Column(Integer)
    low_playtime_count = Column(Integer)
    backlog_count = Column(Integer)

    favorite_game_name = Column(String)
    favorite_game_hours = Column(Float)