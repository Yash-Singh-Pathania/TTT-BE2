# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.db import init_db, close_db
from app.routes.v1 import router

app = FastAPI()

# CORS settings
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    # Add more origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await init_db()

@app.on_event("shutdown")
async def shutdown():
    await close_db()

# Include the user routes
app.include_router(router, prefix="/api")
