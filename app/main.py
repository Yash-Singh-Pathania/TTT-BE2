# app/main.py

from fastapi import FastAPI
from app.config.db import init_db, close_db
from app.routes import user

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_db()

@app.on_event("shutdown")
async def shutdown():
    await close_db()

# Include the user routes
app.include_router(user.router, prefix="/api", tags=["users"])
