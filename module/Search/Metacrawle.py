#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
sys.path.append(os.getcwd())

from lxml      import etree as tree
from Internet  import Browser
from Encode    import normalize
from Engine    import Engine, reduceXpath, zip3, WebInfo,findurl
from typing    import Text

class Metacrawle(Engine):
	def __str__(self):
		return "%s" % "Metacrawle Search"
	def search(self,search_term: Text) -> WebInfo:##[('Titulo','Resumen','URL')]
		try:
			html_text = Browser().getHTML("https://www.metacrawler.com/serp?q=" + search_term.replace(' ','+'))
			html = tree.HTML(html_text)
			titles = reduceXpath(html,"//div[@class='web-bing__result']//a[@class='web-bing__title']")
			titles = [normalize(t.xpath("string()")) for t in titles]
			contents = reduceXpath(html,"//div[@class='web-bing__result']//span[@class='web-bing__description']")
			contents = [normalize(x.xpath("string()")) for x in contents]
			links = html.xpath("//div[@class='web-bing__result']//a[@class='web-bing__title']")
			links = [findurl(l.get('href')) for l in links]
			links = [l for l in links if not (l is None)]
			results = zip3(titles,contents,links,'')
			return results
		except:
			print("Metacrawle Fallo")
			pass
		return None
