from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import TypeVar, Generic, Type, List
from abc import ABC

from dal.database import getSession

class RepoBase(ABC):
  def __init__(self) -> None:
    self.session = getSession()

  def find(self, id: int):
    pass

  # TODO: see how we can make it abstract.
  # def get(self, *filterCriterions) -> List[T]:
  #   query = self.session.query(T)
  #   if len(filterCriterions) > 0:
  #     query = query.filter_by()
  #   return query.all()

  def add(self, model) -> int:
    self.session.add(model)
    self.session.flush()
    id = model.id
    self.session.commit()
    return id

  def edit(self, model):
    pass

  
  def delete(self, id: int) -> None:
    pass