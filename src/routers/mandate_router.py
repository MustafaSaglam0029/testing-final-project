from fastapi import APIRouter
import logging

logger = logging.Logger("mandate-logger")


from src.mandate_data.mandate_data_post import mandate_post_router
from src.mandate_data.mandate_data_delete import mandate_del_router
from src.mandate_data.mandate_data_get import mandate_get_router
from src.mandate_data.mandate_data_put import mandate_put_router

mandate_router = APIRouter()

mandate_router.include_router(mandate_get_router)
mandate_router.include_router(mandate_put_router)
mandate_router.include_router(mandate_post_router)
mandate_router.include_router(mandate_del_router)
