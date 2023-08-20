import asyncio
from datetime import datetime


async def is_cc_valid(card_number):
    # İşlemi tersine çevirerek sayıları alıyoruz
    digits = [int(digit) for digit in card_number[::-1]]

    # Çift indisli basamakları iki katına çıkarıyoruz ve gerekirse iki basamaklı hale getiriyoruz
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    total = sum(digits)

    return total % 10 == 0
