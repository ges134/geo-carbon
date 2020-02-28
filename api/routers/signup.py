from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from services.signupService import SignupService
from presentation.creation.signup import SignupPresentation
from services.serviceFactories import getSignupService
from presentation.readonly.idPresentation import IdPresentation
from services.parameterError import ParameterError

signupRouter = APIRouter()
service = getSignupService()

@signupRouter.post('/signup', response_model=IdPresentation, status_code=HTTP_201_CREATED)
async def signup(presentation: SignupPresentation):
  try:
    id = service.signup(presentation)
    response = IdPresentation(id=id)
    return response
  except ParameterError as error:
    raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=error.getDetailedMessage())