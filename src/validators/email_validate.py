import httpx
from dynaconf import Dynaconf

settings = Dynaconf(settings_file="settings.toml")

API_KEY = settings.api_keys.emailable


async def fetch_email_verification(email: str) -> dict:
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
    return verification_result.get("state") == "deliverable"
