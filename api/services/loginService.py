from bcrypt import checkpw
import jwt
from pydantic import BaseModel

from services.parameterError import ParameterError
from dal.userRepo import UserRepo
from models.user import User
from presentation.creation.login import LoginPresentation

# TODO: move this out in .env or similar
JWT_SECRET = "secret"

class UserToken(BaseModel):
    id: int
    email: str

class InvalidCredentialsException(Exception):
    def __str__(self):
        return "Invalid credentials"

class LoginService:
  def __init__(self, repo: UserRepo) -> None:
    self.repo = repo

  def login(self, presentation: LoginPresentation) -> str:
    user = self.repo.getByEmail(presentation.email)

    if user is None:
      raise InvalidCredentialsException()

    if not checkpw(presentation.password.encode(), user.password.encode()):
      raise InvalidCredentialsException()

    payload = UserToken(
      id=user.id,
      email=user.email
    )

    return jwt.encode(dict(payload), JWT_SECRET)
