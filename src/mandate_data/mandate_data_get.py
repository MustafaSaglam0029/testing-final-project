from fastapi import APIRouter
from fastapi.responses import JSONResponse
from psycopg2.extras import DictCursor
from src.routers.mandate_router import logger
from src.utils.db_connection import conn

mandate_get_router = APIRouter()


@mandate_get_router.get("/mandate/")
async def get_mandate_data(
    business_partner_id: str | None = None, mandate_id: str | None = None
) -> JSONResponse:

    logger.info(f"Received GET request for meter_data")

    try:
        con = conn()
        cur = con.cursor(cursor_factory=DictCursor)

        if business_partner_id and mandate_id:
            cur.execute(
                f"select * from mandate where business_partner_id = '{business_partner_id}' and mandate_id = '{mandate_id}'"
            )
            rows = cur.fetchall()

        elif business_partner_id:
            cur.execute(
                f"select * from mandate where business_partner_id = '{business_partner_id}'"
            )
            rows = cur.fetchall()

        elif mandate_id:
            cur.execute(f"select * from mandate where mandate_id = '{mandate_id}'")
            rows = cur.fetchall()

        else:
            return JSONResponse(
                content={"message": f"Enter a valid business_partner_id or mandate_id"},
                status_code=200,
            )

        if rows:
            rows[0][4] = rows[0][4].isoformat()
            rows[0][5] = rows[0][5].isoformat()
            return JSONResponse(content={"message": rows}, status_code=200)

        else:
            return JSONResponse(
                content={"message": f"No record for this entry"}, status_code=200
            )

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cur:
            cur.close()

        if con:
            con.close()
