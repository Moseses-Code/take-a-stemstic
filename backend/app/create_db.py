from app.core.database import Base, engine

from app.models.user import User
from app.models.user_statistics import UserStatistics
from app.models.game import Game
from app.models.user_game import UserGame

Base.metadata.create_all(bind=engine)

print("База данных обновлена")