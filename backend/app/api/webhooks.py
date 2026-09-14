from fastapi import APIRouter, Request

from app.safety.engine import safety_engine
from app.incidents.service import create_incident


router = APIRouter()


@router.post("/calle")
async def calle_webhook(request: Request):

    payload = await request.json()

    data = payload.get("data", payload)

    safety_result = safety_engine.process_call_result(
        data
    )

    decision = safety_result["decision"]

    session_id = (
        safety_result
        .get("metadata", {})
        .get("session_id")
    )

    call_id = safety_result.get("call_id")

    print()
    print("=" * 70)
    print("CALL-E WEBHOOK")
    print("=" * 70)

    print("Call:", call_id)
    print("Session:", session_id)
    print("Status:", data.get("status"))

    print()
    print("Safety:", decision)

    # Create incident only when danger is detected
    if decision["status"] == "danger":

        incident_id = create_incident(
            session_id=session_id,
            call_id=call_id,
            decision=decision,
        )

        print()
        print("🚨 INCIDENT CREATED")
        print("Incident ID:", incident_id)

    return {
        "received": True,
        "safety_status": decision["status"],
    }