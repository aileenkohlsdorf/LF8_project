import fastapi
import fastapi_swagger_dark as fsd
from router.film_router import router as film_router
from router.kunde_router import router as kunde_router
from router.ausleihe_router import router as ausleihe_router
from router.mitarbeiter_router import router as mitarbeiter_router

app = fastapi.FastAPI(docs_url=None)
router = fastapi.APIRouter()

fsd.install(router)
app.include_router(router)

app.include_router(film_router)
app.include_router(kunde_router)
app.include_router(ausleihe_router)
app.include_router(mitarbeiter_router)
