from fastapi import FastAPI
from app.api.endpoints import (
    auth,
    spheres,
    coordinates,
)
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

app = FastAPI(
    title="Geographic Information System (G.I.S) API",
    version="0.1.1",
    docs_url="/docs",
    debug=True,
    description="This is a Geographic Information System (G.I.S) API. It provides information about regions and districts in Uzbekistan. The API is built using FastAPI and MongoDB. API is powered by Statistics Agency of the Republic of Uzbekistan.",
)

ORIGINS = (
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:3001",
    "*"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(spheres.router, prefix="/v1/api", tags=["spheres"])
app.include_router(coordinates.router, prefix="/v1/api", tags=["coordinates"])
app.include_router(auth.router, prefix="/v1/api", tags=["auth"])
