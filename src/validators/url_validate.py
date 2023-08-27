import validators

async def is_url_valid(url: str) -> bool:
    if validators.url(url):
        return True
    else:
        return False

