from pydantic import BaseModel


class MeterData(BaseModel):
    business_partner_id: str | None = None
    connection_ean_code: str | None = None
    grid_company_code: str | None = None
    oda_code: str | None = None
    meter_number: str | None = None
    smart_collectable: str | None = None
    brand: str | None = None
    sjv1: str | None = None
    sjv2: str | None = None
    installation: str | None = None
    division: str | None = None
    move_out_date: str | None = None
    row_create_datetime: str | None = None
    move_in_date: str | None = None


class IncomingMeterData(BaseModel):
    smart_collectable: str | None = None
