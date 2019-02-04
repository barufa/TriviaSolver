#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
sys.path.append(os.getcwd())

from lxml      import etree as tree
from Internet  import Browser
from Encode    import normalize
from Engine    import Engine, reduceXpath, zip3, WebInfo,findurl
from typing    import Text

class Google(Engine):
	def __str__(self):
		return "%s" % "Google Search"
	def search(self,search_term: Text) -> WebInfo:
		try:
			html_text = Browser().getHTML("https://www.google.com.ar/search?q=" + search_term.replace(' ','+'))
			html = tree.HTML(html_text)
			titles = html.xpath("//div[@class='g']//h3[@class='r']//a")
			titles = [normalize(t.xpath('string()')) for t in titles]
			contents = reduceXpath(html,"//div[@class='g']//div[@class='s']//span[@class='st']")
			contents = [normalize(x.xpath("string()").replace('\n','')) for x in contents]
			links = html.xpath("//div[@class='g']//h3[@class='r']//a")
			links = [findurl(l.get('href')) for l in links]
			links = [l for l in links if not (l is None)]
			results = zip3(titles,contents,links,'')
			return results
		except:
			print("Google Fallo")
			pass
		return None

#
# browser = Google()
# res = browser.search('bandas retiraron grammy')
# print('Resultados de "bandas+retiraron+grammy"\n\n\n')
# if not(res is None):
# 	for t,c,l in res:
# 		line = str(t)+': '+str(l)+'\n'+str(c)
# 		print(str(line+'\n'))
