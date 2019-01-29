#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import json
import requests
from OCR import OCR
from typing import Text, Optional

api_key = 'ada6be3b7588957'


class FreeOCR(OCR):
    def getText(self, filename: Text, overlay=False, language='spa') -> Optional[Text]:
        payload = {'isOverlayRequired': overlay,
                   'apikey': api_key, 'language': language}
        with open(filename, 'rb') as file:
            r = requests.post('https://api.ocr.space/parse/image',
                              files={filename: file}, data=payload)
        try:
            jsn = r.content.decode()
            parsedRes = json.loads(jsn)['ParsedResults'][0]
            return parsedRes['ParsedText']
        except:
            print("Fallo FreeOCR")
            pass
        return None
