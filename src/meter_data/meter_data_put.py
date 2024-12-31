from src.utils.get_meter_status import get_meter_collectable
from src.models.meter_data_model import IncomingMeterData
from src.routers.meter_router import logger
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from src.utils.db_connection import conn

meter_put_router = APIRouter()


@meter_put_router.put("/meter/{business_partner_id}")
async def put_meter_data(business_partner_id: str, incoming_data: IncomingMeterData):

    logger.info(f"Received PUT request for meter {business_partner_id}")

    json_data = incoming_data.model_dump_json()
    status = get_meter_collectable(json_data)

    try:

        if json_data:
            con = conn()
            cur = con.cursor()
            cur.execute(
                f"UPDATE meter SET smart_collectable = '{status}' WHERE business_partner_id = '{business_partner_id}' "
            )
            con.commit()
            return JSONResponse(
                content={
                    "message": f"Record for {business_partner_id} is changed successfully"
                },
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
