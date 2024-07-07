from PIL import Image
import pytesseract
from pathlib import Path


def get_text_from_image(image_path: Path) -> str:
    img = Image.open(image_path)

    text = pytesseract.image_to_string(img)

    return text
