from fastapi import FastAPI
from app.api import stats

app = FastAPI()
app.include_router(stats.router)

@app.get("/")
def root():
    return "Working"