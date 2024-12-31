import json
from psycopg2.extras import Json
from src.models.meter_readings_model import MeterReadings
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.utils.db_connection import conn
from src.routers.meter_readings_router import logger

readings_post_router = APIRouter()

insert_sgl = """
            INSERT INTO meter_readings (account_id, brand, connection_ean_code, energy_type, meter_number,
            reading_date, reading_electricity, reading_gas, rejection,
            validation_status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """


@readings_post_router.post("/meter_readings/")
async def post_meter_readings(meter_readings_data: MeterReadings):

    logger.info(f"Received POST request for meter_readings_data")

    json_data = meter_readings_data.model_dump_json()

    try:
        if json_data:
            data = json.loads(json_data)
            data = [dict(data)]

            for record in data:
                reading_electricity = (
                    Json(record["reading_electricity"])
                    if isinstance(record["reading_electricity"], dict)
                    else record["reading_electricity"]
                )
                reading_gas = (
                    Json(record["reading_gas"])
                    if isinstance(record["reading_gas"], dict)
                    else record["reading_gas"]
                )
                rejection = (
                    Json(record["rejection"])
                    if isinstance(record["rejection"], dict)
                    else record["rejection"]
                )

                con = conn()
                cur = con.cursor()

                cur.execute(
                    insert_sgl,
                    (
                        record["account_id"],
                        record["brand"],
                        record["connection_ean_code"],
                        record["energy_type"],
                        record["meter_number"],
                        record["reading_date"],
                        reading_electricity,
                        reading_gas,
                        rejection,
                        record["validation_status"],
                    ),
                )

                con.commit()

                return JSONResponse(
                    content={
                        "message": f"Record for {meter_readings_data.account_id} is created successfully"
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
