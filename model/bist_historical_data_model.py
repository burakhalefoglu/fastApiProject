from dataclasses import dataclass
from datetime import datetime


@dataclass
class InvestmentItemHistoricalData:
    date: datetime
    code: str
    value: float
    status = True

