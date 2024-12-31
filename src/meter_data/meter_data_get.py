from src.routers.meter_router import logger
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from psycopg2.extras import DictCursor
from src.utils.db_connection import conn

meter_get_router = APIRouter()


@meter_get_router.get("/meter/")
async def get_meter_data(
    business_partner_id: str | None = None, connection_ean_code: str | None = None
):

    logger.info(f"Received GET request for meter_data")

    try:
        con = conn()
        cur = con.cursor(cursor_factory=DictCursor)

        if business_partner_id and connection_ean_code:
            cur.execute(
                f"select * from meter where business_partner_id = '{business_partner_id}' and connection_ean_code = '{connection_ean_code}'"
            )
            rows = cur.fetchall()

        elif business_partner_id:
            cur.execute(
                f"select * from meter where business_partner_id = '{business_partner_id}'"
            )
            rows = cur.fetchall()

        elif connection_ean_code:
            cur.execute(
                f"select * from meter where connection_ean_code = '{connection_ean_code}'"
            )
            rows = cur.fetchall()

        else:
            return JSONResponse(
                content={
                    "message": f"Enter a valid business_partner_id or connection_ean_code"
                },
                status_code=200,
            )

        if rows:
            rows[0][11] = rows[0][11].isoformat()
            rows[0][12] = rows[0][12].isoformat()
            rows[0][13] = rows[0][13].isoformat()
            rows[1][11] = rows[1][11].isoformat()
            rows[1][12] = rows[1][12].isoformat()
            rows[1][13] = rows[1][13].isoformat()
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
