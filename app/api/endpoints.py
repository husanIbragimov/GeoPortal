import fastapi

from app.api.dependencies import (
    auth,
    spheres,
    coordinates,
)

router = fastapi.APIRouter()

router.include_router(spheres.router, prefix="/v1/api", tags=["spheres"])
router.include_router(coordinates.router, prefix="/v1/api", tags=["coordinates"])
router.include_router(auth.router, prefix="/v1/api", tags=["auth"])
