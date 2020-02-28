from bcrypt import hashpw, gensalt

from services.parameterError import ParameterError
from dal.userRepo import UserRepo
from models.user import User
from presentation.creation.signup import SignupPresentation

class SignupService:
  def __init__(self, repo: UserRepo) -> None:
    self.repo = repo

  def signup(self, presentation: SignupPresentation) -> int:
    if presentation.password != presentation.passwordConfirm:
      raise ParameterError('passwordConfirm', 'The passwords does not match')

    user = self.repo.getByEmail(presentation.email)

    if user is not None:
      raise ParameterError('email', 'Email is already taken.')

    passwordAsBytes = bytes(presentation.password, 'utf-8')
    hashed = str(hashpw(passwordAsBytes, gensalt()))

    newUser = User(email=presentation.email, password=hashed)

    newUserId = self.repo.add(newUser)

    return newUserId
