from app.core.database import Base, engine

from app.models.user import User
from app.models.user_statistics import UserStatistics

Base.metadata.create_all(bind=engine)

print("База данных обновлена")