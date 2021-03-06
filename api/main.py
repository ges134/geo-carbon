from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from routers.home import homeRouter
from routers.signup import signupRouter
from routers.login import loginRouter

app = FastAPI()

app.include_router(homeRouter)
app.include_router(signupRouter)
app.include_router(loginRouter)
