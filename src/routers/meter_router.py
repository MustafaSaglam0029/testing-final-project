from fastapi import APIRouter
import logging

logger = logging.Logger("meter-logger")

from src.meter_data.meter_data_post import meter_post_router
from src.meter_data.meter_data_delete import meter_del_router
from src.meter_data.meter_data_get import meter_get_router
from src.meter_data.meter_data_put import meter_put_router

meter_router = APIRouter()

meter_router.include_router(meter_get_router)
meter_router.include_router(meter_put_router)
meter_router.include_router(meter_post_router)
meter_router.include_router(meter_del_router)
