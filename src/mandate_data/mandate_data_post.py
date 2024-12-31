import json
from src.models.mandate_data_model import MandateData
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.routers.mandate_router import logger
from src.utils.db_connection import conn

mandate_post_router = APIRouter()


@mandate_post_router.post("/mandate/")
async def post_mandate_data(mandate_data: MandateData) -> JSONResponse:

    logger.info(f"Received POST request for mandate_data")

    json_data = mandate_data.model_dump_json()

    try:

        if json_data:
            data = json.loads(json_data)
            data = tuple(data.values())
            con = conn()
            cur = con.cursor()
            cur.execute(f"INSERT INTO mandate VALUES{data}")
            con.commit()
            return JSONResponse(
                content={
                    "message": f"Record for {mandate_data.business_partner_id} is created successfully"
                },
                status_code=200,
            )

        else:
            return JSONResponse(
                content={"message": "Send a valid post"}, status_code=200
            )

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cur:
            cur.close()

        if con:
            con.close()
