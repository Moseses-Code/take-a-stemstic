from sqlalchemy import Column, Integer, Float, String
from app.core.database import Base


class UserGame(Base):
    __tablename__ = "user_games"

    id = Column(Integer, primary_key=True, index=True)
    steam_id = Column(String)
    steam_app_id = Column(Integer)
    hours = Column(Float)