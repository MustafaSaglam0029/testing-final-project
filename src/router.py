from fastapi import APIRouter
from src.routers.mandate_router import mandate_router
from src.routers.meter_router import meter_router
from src.routers.meter_readings_router import meter_readings_router


api_router = APIRouter()

api_router.include_router(mandate_router)
api_router.include_router(meter_router)
api_router.include_router(meter_readings_router)
