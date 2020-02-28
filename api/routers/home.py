from fastapi import APIRouter

homeRouter = APIRouter()

@homeRouter.get("/home")
async def home():
  return {"welcome to GeoCarbon! The gelocalized carbon footprint calculator!"}