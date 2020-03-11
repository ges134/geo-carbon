from presentation.creation.footprint import FootprintPresentation
from dal.footprintRepo import FootprintRepo
from models.footprint import Footprint

class FootprintService:
  def __init__(self, repo: FootprintRepo) -> None:
    self.repo = repo

  def add_footprint(self, presentation: FootprintPresentation, user_id: int) -> int:
    footprint = Footprint(
      id=None,
      user_id=user_id,
      footprint=presentation.footprint,
      location=presentation.location,
      date=presentation.date
    )
    return self.repo.add(footprint)
