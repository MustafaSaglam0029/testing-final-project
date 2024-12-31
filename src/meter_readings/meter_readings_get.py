from fastapi import APIRouter
from fastapi.responses import JSONResponse
from psycopg2.extras import DictCursor
from src.routers.meter_readings_router import logger
from src.utils.db_connection import conn

readings_get_router = APIRouter()


@readings_get_router.get("/meter_readings/")
async def get_meter_readings(
    account_id: str | None = None, connection_ean_code: str | None = None
):

    logger.info(f"Received GET request for meter_readings_data")

    try:
        con = conn()
        cur = con.cursor(cursor_factory=DictCursor)

        if account_id and connection_ean_code:
            cur.execute(
                f"select * from meter_readings where account_id = '{account_id}' and connection_ean_code = '{connection_ean_code}'"
            )
            rows = cur.fetchall()

        elif account_id:
            cur.execute(
                f"select * from meter_readings where account_id = '{account_id}'"
            )
            rows = cur.fetchall()

        elif connection_ean_code:
            cur.execute(
                f"select * from meter_readings where connection_ean_code = '{connection_ean_code}'"
            )
            rows = cur.fetchall()

        else:
            return JSONResponse(
                content={"message": f"Enter a valid account_id or connection_ean_code"},
                status_code=200,
            )

        if rows:
            for row in rows:
                if row[5] is not None:
                    row[5] = row[5].isoformat()

            return JSONResponse(content={"message": rows}, status_code=200)

        else:
            return JSONResponse(
                content={"message": f"No record for this entry "}, status_code=200
            )

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cur:
            cur.close()

        if con:
            con.close()
