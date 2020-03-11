from services.signupService import SignupService
from services.loginService import LoginService
from services.footprintService import FootprintService
from dal.footprintRepo import FootprintRepo
from dal.userRepo import UserRepo
from models.user import User

def getSignupService():
  return SignupService(UserRepo())

def getLoginService():
  return LoginService(UserRepo())

def getFootprintService():
  return FootprintService(FootprintRepo())
