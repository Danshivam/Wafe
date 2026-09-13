import os

from dotenv import load_dotenv

load_dotenv()


CALLE_API_KEY = os.getenv("CALLE_API_KEY")

if not CALLE_API_KEY:
    raise RuntimeError(
        "CALLE_API_KEY is not set. "
        "Create a .env file in the backend directory."
    )