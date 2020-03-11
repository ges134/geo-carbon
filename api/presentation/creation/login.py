from pydantic import BaseModel

class LoginPresentation(BaseModel):
  email: str
  password: str

