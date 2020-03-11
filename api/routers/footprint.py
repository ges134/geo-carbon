from fastapi import APIRouter, Depends
from starlette.status import HTTP_201_CREATED

from services.serviceFactories import getFootprintService
from services.footprintService import FootprintPresentation
from services.authentication import UserToken, authenticated
from presentation.readonly.idPresentation import IdPresentation

footprintRouter = APIRouter()
service = getFootprintService()

@footprintRouter.post('/footprint', response_model=IdPresentation, status_code=HTTP_201_CREATED)
async def add_footprint(
  presentation: FootprintPresentation,
  user: UserToken = Depends(authenticated)
):
  id = service.add_footprint(presentation)
  return IdPresentation(id=id)
