from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse
from starlette import status

from presentation.creation.login import LoginPresentation
from services.serviceFactories import getLoginService
from presentation.readonly.userTokenPresentation import UserTokenPresentation
from services.parameterError import ParameterError
from services.loginService import InvalidCredentialsException

loginRouter = APIRouter()
service = getLoginService()

@loginRouter.post('/login', response_model=UserTokenPresentation)
async def login(presentation: LoginPresentation):
  try:
    token = service.login(presentation)
    response = UserTokenPresentation(token=token)
    return response
  except ParameterError as error:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error.getDetailedMessage())
  except InvalidCredentialsException as e:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
