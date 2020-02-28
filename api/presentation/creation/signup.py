from pydantic import BaseModel

class SignupPresentation(BaseModel):
  email:str
  password:str
  passwordConfirm:str