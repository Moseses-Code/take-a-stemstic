from fastapi import FastAPI
from app.api import stats,users,steam
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(stats.router)
app.include_router(users.router)
app.include_router(steam.router)
@app.get("/")
def root():
    return "Working"