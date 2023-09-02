import validators

async def is_url_valid(url: str) -> bool:
    """
    Checks if a URL is valid.

    Args:
        url (str): The URL to be validated.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    if validators.url(url):
        return True
    else:
        return False

