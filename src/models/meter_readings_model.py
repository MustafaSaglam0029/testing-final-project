from pydantic import BaseModel


class MeterReadings(BaseModel):
    account_id: str | None = None
    brand: str | None = None
    connection_ean_code: str | None = None
    energy_type: str | None = None
    meter_number: str | None = None
    reading_date: str | None = None
    reading_electricity: dict | None = None
    reading_gas: dict | None = None
    rejection: dict | None = None
    validation_status: str | None = None


class IncomingMeterReadings(BaseModel):
    validation_status: str | None = None
