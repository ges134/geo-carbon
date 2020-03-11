from typing import Tuple, Optional
from datetime import date
from pydantic import BaseModel

class FootprintPresentation(BaseModel):
  footprint: float
  location: Tuple[float, float]
  date: Optional[date]
