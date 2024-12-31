from fastapi import APIRouter
import logging

logger = logging.Logger("meter_readings-logger")

from src.meter_readings.meter_readings_post import readings_post_router
from src.meter_readings.meter_readings_delete import readings_del_router
from src.meter_readings.meter_readings_get import readings_get_router
from src.meter_readings.meter_readings_put import readings_put_router

meter_readings_router = APIRouter()


meter_readings_router.include_router(readings_get_router)
meter_readings_router.include_router(readings_put_router)
meter_readings_router.include_router(readings_post_router)
meter_readings_router.include_router(readings_del_router)
