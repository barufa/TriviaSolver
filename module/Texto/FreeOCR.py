#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io, json, requests
from OCR     import OCR
from typing  import Text, Optional

api_key = 'yourkey'

class FreeOCR(OCR):
    def getText(self, path: Text, overlay=False, language='spa') -> Optional[Text]:
		payload = {'isOverlayRequired': overlay,
	               'apikey': api_key,
	               'language': language,
	               }
	    with open(path, 'rb') as f:
	        r = requests.post('https://api.ocr.space/parse/image',
	                          files={filename: f},
	                          data=payload,
	                          )
	    try:
	        jsn = r.content.decode()
	        parsedRes = json.loads(jsn)['ParsedResults'][0]
	        return parsedRes['ParsedText']
	    except:
	        pass
	    return None
