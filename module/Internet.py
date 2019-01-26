#!/usr/bin/env python
# -*- coding: utf-8 -*-

from html2text       import HTML2Text
from urllib.request  import urlopen,Request
from Encode          import normalize
from time            import time
from typing          import Text, Optional

html_to_text = HTML2Text()
html_to_text.ignore_links = True
header = {'User-Agent': 'Mozilla/64.0 (X11; Linux x86_64) Chrome/71.0.3578',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
          'Accept-Encoding': 'none',
          'Accept-Language': 'en-US,en,es,es-AR;q=0.8',
          'Connection': 'keep-alive'}

class Browser:
    def getHTML(self, url: Text) -> Optional[Text]:
        if url.count('.pdf') >= 1 or url.count('.doc') >= 1:
            print("Internet.py: El link recibio pertenece a un documento")
            return None
        try:
            request = Request(url, headers = header)
            response = urlopen(request)
            html = response.read()
            r = html.decode("utf8")
            return r
        except:
            print("Internet.py: Hubo un error al descargar el html " + str(url))
            pass
        return None

    def getText(self, url: Text) -> Optional[Text]:
        r = self.getHTML(url)
        if r is None:
            print("Internet.py: No es posible extraer el texto del link " + str(url))
            return None
        else:
            rs = html_to_text.handle(r)
            return rs

# print(Browser().getText('https://es.wikipedia.org/wiki/Cris_Morena'))
