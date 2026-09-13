from app.calle.client import calle_client
from app.calle.tasks import (
    WALK_ME_HOME_TASK,
    WALK_ME_HOME_RESULT_SCHEMA,
)


PHONE_NUMBER = "+918527067677"

WEBHOOK_URL = (
    "https://abc123.ngrok-free.app"
    "/api/webhooks/calle"
)


def main() -> None:
    result = calle_client.calls.create(
        task=f"""
{WALK_ME_HOME_TASK}

Call the user at:
{PHONE_NUMBER}
""",
        result_schema=WALK_ME_HOME_RESULT_SCHEMA,
        webhook_url=WEBHOOK_URL,
    )

    print("\nCALL-E CALL CREATED")
    print("=" * 50)
    print(result)

    print("\nCall ID:")
    print(result["id"])

    print("\nStatus:")
    print(result["status"])


if __name__ == "__main__":
    main()