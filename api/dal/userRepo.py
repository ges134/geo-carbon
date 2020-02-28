from dal.repoBase import RepoBase
from models.user import User

class UserRepo(RepoBase):
  def find(self, id: int) -> User:
    return self.session.query(User).filter_by(id=id).first()
  
  def add(self, model: User) -> int:
    return super().add(model)
  
  def getByEmail(self, email: str) -> User:
    return self.session.query(User).filter_by(email=email).first()
  
  def edit(self, model: User) -> User:
    toUpdate = self.find(model.id)
    toUpdate.email = model.email
    toUpdate.password = model.password
    self.session.commit()
    return toUpdate
  
  def delete(self, id:int) -> None:
    toDelete = self.find(id)
    self.session.delete(toDelete)