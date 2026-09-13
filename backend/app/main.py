from fastapi import FastAPI

app = FastAPI(
    title="CALL-E Walk Me Home",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "name": "CALL-E Walk Me Home",
        "status": "running",
    }


@app.get("/health")
async def health():
    return {
        "status": "ok",
    }