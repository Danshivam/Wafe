from fastapi import APIRouter
from pydantic import BaseModel

from app.calle.client import client
from app.calle.tasks import (
    WALK_ME_HOME_TASK,
    WALK_ME_HOME_RESULT_SCHEMA,
)


router = APIRouter()


class StartSessionRequest(BaseModel):
    phone_number: str


@router.post("/start")
def start_session(request: StartSessionRequest):

    call = client.calls.create(
        task=f"""
{WALK_ME_HOME_TASK}

Call this phone number:

{request.phone_number}
""",
        result_schema=WALK_ME_HOME_RESULT_SCHEMA,
    )

    return {
        "session_status": "starting",
        "call_id": call["id"],
        "calle_status": call["status"],
    }