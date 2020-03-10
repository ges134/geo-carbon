from pydantic import BaseModel

# TODO: move this in another folder?
class LoginPresentation(BaseModel):
  email: str
  password: str
