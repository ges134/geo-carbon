from bcrypt import checkpw

from services.authentication import generateToken
from dal.userRepo import UserRepo
from presentation.creation.login import LoginPresentation

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

    return generateToken(user)
