from fastapi import APIRouter
from app.services import stats_services

router = APIRouter()

@router.get("/stats")
def get_stats():
    return stats_services.get_stats()
   