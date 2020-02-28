from services.signupService import SignupService
from dal.userRepo import UserRepo
from models.user import User

def getSignupService():
  return SignupService(UserRepo())