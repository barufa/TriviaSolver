#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.getcwd())

from lxml      import etree as tree
from Internet  import Browser
from Encode    import normalize
from Engine    import Engine, reduceXpath, zip3, WebInfo, findurl
from typing    import Text


class Ask(Engine):
	def __str__(self):
		return "%s" % "Ask Search"

	def search(self, search_term: Text) -> WebInfo:#Optional[(Titulo,Conten,Url)]
		try:
			html_text = Browser().getHTML("https://www.ask.com/web?q=" + search_term.replace(' ', '+'))
			html = tree.HTML(html_text)
			title = reduceXpath(html, "//div[@class='PartialSearchResults-body']//div[@class='PartialSearchResults-item']//a")
			title = [normalize(t.xpath("string(//a)")) for t in title]
			contents = reduceXpath(html, "//div[@class='PartialSearchResults-body']//div[@class='PartialSearchResults-item']//p[@class='PartialSearchResults-item-abstract']")
			contents = [normalize(x.xpath("string(//p)")) for x in contents]
			links = html.xpath("//div[@class='PartialSearchResults-body']//div[@class='PartialSearchResults-item']//a")
			links = [findurl(l.get('href')) for l in links]
			links = [l for l in links if not (l is None)]
			results = zip3(title, contents, links, '')
			return results
		except:
			print("Ask Fallo")
			pass
		return None
