#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
sys.path.append(os.getcwd())

from lxml      import etree as tree
from Internet  import Browser
from Encode    import normalize
from Engine    import Engine, reduceXpath, zip3, WebInfo,findurl
from typing    import Text

class Bing(Engine):
    def __str__(self):
        return "%s" % "Bing Search"

    def search(self, search_term: Text) -> WebInfo:  # [('Titulo','Resumen','URL')]
        try:
            html_text = Browser().getHTML("https://www.bing.com/search?q=" + search_term.replace(' ', '+'))
            html = tree.HTML(html_text)
            titles = reduceXpath(html, "//ol[@id='b_results']//li[@class='b_algo']//h2//a")
            titles = [normalize(x.xpath("string(//a)")) for x in titles]
            contents = reduceXpath(html, "//ol[@id='b_results']//li[@class='b_algo']//p")
            contents = [normalize(x.xpath("string(//p)")) for x in contents]
            links = reduceXpath(html, "//ol[@id='b_results']//li[@class='b_algo']//h2//a")
            links = [findurl(l.get('href')) for l in links]
            links = [l for l in links if not (l is None)]
            results = zip3(titles, contents, links, '')
            return results
        except:
            print("Bing Fallo")
            pass
        return None
