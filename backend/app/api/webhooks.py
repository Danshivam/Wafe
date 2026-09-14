from fastapi import APIRouter, Request

from app.safety.engine import safety_engine


router = APIRouter()


@router.post("/calle")
async def calle_webhook(request: Request):

    payload = await request.json()

    print()
    print("=" * 70)
    print("CALL-E WEBHOOK RECEIVED")
    print("=" * 70)

    print("Call ID:", payload.get("data", {}).get("id"))

    data = payload.get("data", payload)

    print("Status:", data.get("status"))

    safety_result = safety_engine.process_call_result(
        data
    )

    print()
    print("SAFETY DECISION")
    print("=" * 70)
    print(safety_result)

    return {
        "received": True,
        "safety_status": (
            safety_result["decision"]["status"]
        ),
    }