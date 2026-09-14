from fastapi import FastAPI

from app.api.sessions import router as sessions_router


app = FastAPI(
    title="CALL-E Walk Me Home",
)


app.include_router(
    sessions_router,
    prefix="/api/session",
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