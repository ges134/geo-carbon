from dal.repoBase import RepoBase
from models.footprint import Footprint

class FootprintRepo(RepoBase):
  def add(self, model: Footprint) -> int:
    result = self.session.execute(
        'INSERT INTO footprints VALUES (DEFAULT, :user_id, :footprint, ST_SetSRID(ST_MakePoint(:long, :lat), 4326), :date) RETURNING id',
      {
        'footprint': model.footprint,
        'user_id': model.user_id,
        'long': model.location[0],
        'lat': model.location[1],
        'date': None if not model.date else model.date.c_time()
      }
    )
    self.session.commit()
    return result.fetchone()[0]

