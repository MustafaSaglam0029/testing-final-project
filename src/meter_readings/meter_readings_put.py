from src.utils.get_meter_readings_status import get_validation_status
from src.models.meter_readings_model import IncomingMeterReadings
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.utils.db_connection import conn
from src.routers.meter_readings_router import logger

readings_put_router = APIRouter()


@readings_put_router.put("/meter_readings/{account_id}")
async def put_meter_readings(account_id: str, incoming_data: IncomingMeterReadings):

    logger.info(f"Received PUT request for meter_readings {account_id}")

    json_data = incoming_data.model_dump_json()
    status = get_validation_status(json_data)

    try:

        if json_data:
            con = conn()
            cur = con.cursor()
            cur.execute(
                f"UPDATE meter_readings SET validation_status = '{status}' WHERE account_id = '{account_id}' "
            )
            con.commit()

            return JSONResponse(
                content={"message": f"Record for {account_id} is changed successfully"},
                status_code=200,
            )

        else:
            return JSONResponse(
                content={"message": "Send a valid update"}, status_code=200
            )

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cur:
            cur.close()

        if con:
            con.close()
