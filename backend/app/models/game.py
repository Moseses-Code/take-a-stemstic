from sqlalchemy import Column, Integer, String
from app.core.database import Base


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    steam_app_id = Column(Integer, unique=True, index=True)
    name = Column(String)