import io
import pytesseract
import cv2
from OCR import OCR
from typing import Text, Optional

class Tesseract(OCR):
    def getText(self, path: Text, language='spa') -> Optional[Text]:
        try:
            txt = pytesseract.image_to_string(path, lang=language)
            return txt
        except:
            pass
        return None

print(Tesseract().getText('/home/bruno/Escritorio/TriviaBot/questions/A/qweq.png'),'\n')
print(Tesseract().getText('/home/bruno/Escritorio/TriviaBot/questions/A/qwep.png'))
