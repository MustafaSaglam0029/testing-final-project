from fastapi import APIRouter
from src.utils.db_connection import conn
from fastapi.responses import JSONResponse
from src.routers.meter_readings_router import logger

readings_del_router = APIRouter()


@readings_del_router.delete("/meter_readings/{account_id}")
async def delete_meter_readings(account_id: str):

    logger.info(f"Received DELETE request for meter_readings {account_id}")

    try:
        con = conn()
        cur = con.cursor()
        cur.execute(f"SELECT * FROM meter_readings WHERE account_id = '{account_id}' ")
        record = cur.fetchall()

        if record:

            cur.execute(
                f"DELETE FROM meter_readings WHERE account_id = '{account_id}' "
            )
            con.commit()
            return JSONResponse(
                content={"message": f"Record for {account_id} is deleted successfully"},
                status_code=200,
            )

        else:
            return JSONResponse(content={"message": f"No record for {account_id}"})

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cur:
            cur.close()

        if con:
            con.close()
