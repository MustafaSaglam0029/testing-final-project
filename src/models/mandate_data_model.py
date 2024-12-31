from pydantic import BaseModel


class MandateData(BaseModel):
    business_partner_id: str
    mandate_status: str | None = None
    collection_frequency: str | None = None
    brand: str | None = None
    row_update_datetime: str | None = None
    row_create_datetime: str | None = None
    changed_by: str | None = None
    mandate_id: str | None = None
    collection_type: str | None = None
    metering_consent: str | None = None


class IncomingMandateData(BaseModel):
    mandate_status: str | None = None
