from dal.repoBase import RepoBase
from presentation.creation.footprint import FootprintPresentation

class FootprintRepo(RepoBase):
  def add(self, model: FootprintPresentation) -> int:
    result = self.session.execute(
      'INSERT INTO footprints VALUES (DEFAULT, :footprint, ST_SetSRID(ST_MakePoint(:long, :lat), 4326), :date) RETURNING id',
      {
        'footprint': model.footprint,
        'long': model.location[0],
        'lat': model.location[1],
        'date': None if not model.date else model.date.c_time()
      }
    )
    self.session.commit()
    return result.fetchone()[0]

