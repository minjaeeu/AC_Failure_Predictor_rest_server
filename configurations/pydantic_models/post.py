from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime


class AC_Info_Post(BaseModel):
    datetime: datetime
    humidity: Decimal
    temperature: Decimal
    wattage: Decimal
