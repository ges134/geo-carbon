from presentation.creation.footprint import FootprintPresentation
from dal.footprintRepo import FootprintRepo

class FootprintService:
  def __init__(self, repo: FootprintRepo) -> None:
    self.repo = repo

  def add_footprint(self, presentation: FootprintPresentation) -> int:
    result = self.repo.add(presentation)
    return result
