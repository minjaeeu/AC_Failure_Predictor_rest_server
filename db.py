from sqlalchemy import Column, DateTime, DECIMAL
from base import Base
from datetime import (
    datetime as DATETIME,
)  # only for type hitting and also to not confund with "datetime" variable from AC_Info class.


class AC_Info(Base):
    """Creates database called "AC-Info" and assigns its columns and data type values."""

    __tablename__ = "AC_Info"
    datetime = Column("datetime", DateTime, primary_key=True, unique=True)
    humidity = Column("humidity", DECIMAL, nullable=False)
    temperature = Column("tempature", DECIMAL, nullable=False)
    wattage = Column("wattage", DECIMAL, nullable=False)

    def __init__(
        self,
        datetime: DATETIME,
        humidity: DECIMAL,
        temperature: DECIMAL,
        wattage: DECIMAL,
    ) -> None:
        """Class constructor, assings columns from the DB to the respective parameters.

        Args:
            datetime (DATETIME): datetime pattern of YYYY-MM-DD HH:MM:SS **Needs to be a python datetime object.
            humidity (DECIMAL): decimal value for humidity percentage.
            temperature (DECIMAL): decimal value for temperature (assumed in celsius).
            wattage (DECIMAL): decimal value for wattage (power) consumption.
        """

        self.datetime = datetime
        self.humidity = humidity
        self.temperature = temperature
        self.wattage = wattage

    def __repr__(self) -> str:
        """Class repr, responsible for the formatting when querying the db.

        Returns:
            str: AC_Info table entry.
        """

        return f"datetime: {self.datetime}, humidity: {self.humidity}, temperature: {self.temperature}, wattage: {self.wattage}"
