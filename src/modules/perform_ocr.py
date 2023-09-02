import pytesseract
from PIL import Image


async def perform_ocr(image: Image.Image) -> str:
    """
    Performs Optical Character Recognition (OCR) on the given image.

    Args:
        image (Image.Image): The PIL Image object containing the image data.

    Returns:
        str: The extracted text from the image.
    """
    text = pytesseract.image_to_string(image, lang="eng")
    return text.strip()
