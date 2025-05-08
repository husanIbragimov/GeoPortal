import fastapi

from api.dependencies import (
    auth,
)
from api.dependencies import coordinates, spheres

router = fastapi.APIRouter()

router.include_router(spheres.router, prefix="/api", tags=["spheres"])
router.include_router(coordinates.router, prefix="/api", tags=["coordinates"])
router.include_router(auth.router, prefix="/api", tags=["auth"])
