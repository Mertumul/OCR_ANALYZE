from bs4 import BeautifulSoup
import httpx


async def luhn_algorithm(card_number: int) -> bool:
    """
    Implements the Luhn algorithm to validate a credit card number.

    Args:
        card_number (int): The credit card number to be validated.

    Returns:
        bool: True if the card number is valid, False otherwise.
    """
    digits = [int(digit) for digit in str(card_number)[::-1]]

    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    total = sum(digits)

    return total % 10 == 0

async def is_bin_valid(card_number: str) -> bool:
    """
    Checks if the first 6 digits of a credit card number (BIN) are valid using bin lookup.

    Args:
        card_number (str): The credit card number.

    Returns:
        bool: True if the BIN is valid, False otherwise.
    """
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
    """
    Validates a credit card number using the Luhn algorithm and BIN lookup.

    Args:
        card_number (str): The credit card number.

    Returns:
        bool: True if the credit card number is valid, False otherwise.
    """
    is_cc = await luhn_algorithm(card_number)
    if is_cc:
        is_bin = await is_bin_valid(card_number)
        if is_bin:
            return True
        return False
    return False
