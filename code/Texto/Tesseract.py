import io
import pytesseract
from OCR import OCR
from typing import Text, Optional

class Tesseract(OCR):
    def getText(self, path: Text, language='spa') -> Optional[Text]:
        try:
            txt = pytesseract.image_to_string(path, lang=language)
            return txt
        except:
            print("Tesseract fails")
        return None
