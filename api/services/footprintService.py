from typing import Tuple, Optional
from datetime import date
from pydantic import BaseModel

from dal.userRepo import UserRepo

class FootprintPresentation(BaseModel):
  footprint: float
  location: Tuple[float, float]
  date: Optional[date]

class FootprintService:
  def __init__(self, repo: UserRepo) -> None:
    self.repo = repo

  def add_footprint(self, presentation: FootprintPresentation) -> str:
    return ""
