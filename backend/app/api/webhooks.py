from fastapi import APIRouter, Request


router = APIRouter()


@router.post("/calle")
async def calle_webhook(request: Request):
    payload = await request.json()

    print("\n" + "=" * 60)
    print("CALL-E WEBHOOK RECEIVED")
    print("=" * 60)
    print(payload)

    return {
        "received": True
    }