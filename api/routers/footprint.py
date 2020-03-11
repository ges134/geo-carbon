from fastapi import APIRouter, Depends

from services.serviceFactories import getFootprintService
from services.footprintService import FootprintPresentation
from services.authentication import UserToken, authenticated

footprintRouter = APIRouter()
service = getFootprintService()

@footprintRouter.post('/footprint')
async def add_footprint(
  presentation: FootprintPresentation,
  user: UserToken = Depends(authenticated)
):
  print(presentation)
  print(user)
  service.add_footprint(presentation)
  return { 'ok': 'lol' }
