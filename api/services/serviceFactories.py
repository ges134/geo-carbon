from services.signupService import SignupService
from services.loginService import LoginService
from dal.userRepo import UserRepo
from models.user import User

def getSignupService():
  return SignupService(UserRepo())

def getLoginService():
  return LoginService(UserRepo())
