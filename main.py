from fastapi import FastAPI
from database import engine
import models
from routers import auth_router, heroes_router

# initialisation de l'application 
app=FastAPI()
models.Base.metadata.create_all(bind=engine)  # create the database tables

app.include_router(heroes_router.router, tags=["Heroes"])  # include the heroes router with a prefix
app.include_router(auth_router.router, tags=["Authentication"])  # include the auth router with a prefix
