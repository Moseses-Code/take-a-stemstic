from fastapi import FastAPI
from app.api import stats,users

app = FastAPI()
app.include_router(stats.router)
app.include_router(users.router)
@app.get("/")
def root():
    return "Working"