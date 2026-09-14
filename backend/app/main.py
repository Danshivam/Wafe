from fastapi import FastAPI

from app.api.sessions import router as sessions_router
from app.api.webhooks import router as webhooks_router
from app.database.database import initialize_database
from app.api.incidents import router as incidents_router


initialize_database()


app = FastAPI(
    title="CALL-E Walk Me Home",
    version="0.1.0",
)


app.include_router(
    sessions_router,
    prefix="/api/session",
)

app.include_router(
    webhooks_router,
    prefix="/api/webhook",
)

app.include_router(
    incidents_router,
    prefix="/api/incidents",
)


@app.get("/")
def root():
    return {
        "name": "CALL-E Walk Me Home",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
    }

