from bs4 import BeautifulSoup
import httpx


async def luhn_algorithm(card_number: int):
    digits = [int(digit) for digit in str(card_number)[::-1]]

    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    total = sum(digits)

    return total % 10 == 0

async def is_bin_valid(card_number: str) -> bool:
    bin_number = card_number[:6]
    url = f"https://quickbinlookup.com/?binquery={bin_number}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    bin_result_div = soup.find("div", {"id": "binresult"})
    if bin_result_div and "No results" in bin_result_div.get_text():
        return False
    else:
        return True

async def is_cc_valid(card_number: str) -> bool:
    is_cc = await luhn_algorithm(card_number)
    if is_cc:
        is_bin = await is_bin_valid(card_number)
        if is_bin:
            return True
        return False
    return False
