import pytesseract
from PIL import Image

async def perform_ocr(image: Image.Image) -> str:
    text = pytesseract.image_to_string(image, lang='eng', config='--psm 6')
    return text.strip()
