from pydantic import BaseModel

class UserCreate(BaseModel):
    steam_id: int
    nickname: str
    avatar_url: str

class UserUpdate(BaseModel):
    steam_id: int
    nickname: str
    avatar_url: str
