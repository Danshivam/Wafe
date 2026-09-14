from fastapi import FastAPI

from app.api.sessions import router as sessions_router
from app.api.webhooks import router as webhooks_router


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