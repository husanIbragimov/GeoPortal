import fastapi

from src.api.dependencies import (
    auth,
    spheres,
    coordinates,
)

router = fastapi.APIRouter()

router.include_router(spheres.router, prefix="/api", tags=["spheres"])
router.include_router(coordinates.router, prefix="/api", tags=["coordinates"])
router.include_router(auth.router, prefix="/api", tags=["auth"])
