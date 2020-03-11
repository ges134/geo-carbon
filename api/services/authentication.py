from fastapi import HTTPException
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST
from pydantic import BaseModel, ValidationError
import jwt

from presentation.readonly.userTokenPresentation import UserTokenPresentation
from models.user import User

# TODO: move this out in .env or similar
JWT_SECRET = "secret"

class UserToken(BaseModel):
  id: int
  email: str

async def authenticated(request: Request) -> UserToken:
  auth = request.headers.get("Authorization")
  if not auth or not auth.lower().startswith("bearer "):
    unauthorized()
  try:
    user = jwt.decode(auth[7:], JWT_SECRET)
    return UserToken(**user)
  except jwt.exceptions.DecodeError:
    unauthorized()
  except ValidationError:
    raise HTTPException(status_code=HTTP_400_BAD_REQUEST)

def generateToken(user: User) -> str:
  payload = UserToken(id=user.id, email=user.email)
  return jwt.encode(dict(payload), JWT_SECRET)

def unauthorized():
  raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Not authenticated")
