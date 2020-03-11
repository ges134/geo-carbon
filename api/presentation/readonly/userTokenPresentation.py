from pydantic import BaseModel

class UserTokenPresentation(BaseModel):
  token: str
