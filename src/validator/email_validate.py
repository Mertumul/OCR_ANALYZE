import httpx
from dynaconf import Dynaconf

settings = Dynaconf(settings_file="settings.toml")

API_KEY = settings.api_keys.emailable


async def fetch_email_verification(email: str) -> dict:
    """
    Fetches email verification details using the Emailable API.

    Args:
        email (str): The email address to be verified.

    Returns:
        dict: Verification details returned by the Emailable API.
    """
    api_url = "https://api.emailable.com/v1/verify"
    params = {"email": email, "api_key": API_KEY}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(api_url, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            print("Error:", e)
            return None


async def is_email_deliverable(verification_result: dict) -> bool:
    """
    Checks if an email address is deliverable based on the verification result.

    Args:
        verification_result (dict): The verification result returned by the Emailable API.

    Returns:
        bool: True if the email address is deliverable, False otherwise.
    """
    return verification_result.get("state") == "deliverable"
