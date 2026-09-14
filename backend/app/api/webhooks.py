from fastapi import APIRouter, Request

router = APIRouter()


@router.post("/calle")
async def calle_webhook(request: Request):
    payload = await request.json()

    print()
    print("=" * 70)
    print("CALL-E WEBHOOK RECEIVED")
    print("=" * 70)
    print(payload)
    print("=" * 70)

    return {
        "received": True
    }