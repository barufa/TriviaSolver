#!/usr/bin/env python
# -*- coding: utf-8 -*-

###VERSION VIEJA, OBSOLETA

import sys,os
sys.path.append(os.getcwd())

import urllib.parse
import selenium.webdriver as webdriver
from time    import time
from Encode  import normalize
from time    import time
from Engine  import Engine

# Un buscador en comun para todos
driver = webdriver.PhantomJS()

def zipeer(lx, ly):
    if len(lx) == 0:
        return ly
    if len(ly) == 0:
        return lx
    return [lx[0]] + [ly[0]] + zipper(lx[1:], ly[1:])


class Google(Engine):
    def __str__(self):
        return "%s" % "Google Search"

    def search(self, search_term):
        driver.get("https://www.google.com/search?q=" +
                   search_term.replace(' ', '+'))
        response = driver.find_elements_by_css_selector('div.g')
        result = []
        for res in response:
            if len(res.find_elements_by_css_selector('.r')) == 0:
                continue
            head = res.find_elements_by_css_selector('.r')[0]
            try:
                title = head.text
                title = normalize(title)
            except:
                title = ''
            try:
                text = res.find_element_by_css_selector("span.st").text
                text = normalize(text)
                text = text.replace('\n', ' ')
            except:
                text = ''
            try:
                link = head.find_element_by_tag_name("a").get_attribute("href")
                link = urllib.parse.parse_qs(
                    urllib.parse.urllib.parse(link).query)["q"][0]
            except:
                link = ''
            result.append((title, text, link))
        return result

class Bing(Engine):
    def __str__(self):
        return "%s" % "Bing Search"

    def search(self, search_term):  # [('Titulo','Resumen','URL')]
        driver.get("https://www.bing.com/search?q=" +
                   search_term.replace(' ', '+'))
        response = driver.find_elements_by_css_selector('li.b_algo')
        result = []
        for res in response:
            try:
                title = res.find_element_by_tag_name("a").text
                title = normalize(title)
            except:
                title = ''
            try:
                text = res.find_element_by_tag_name("p").text
                text = normalize(text)
                text = text.replace('\n', ' ')
            except:
                text = ''
            try:
                link = res.find_element_by_tag_name("a").get_attribute("href")
            except:
                link = ''
            result.append((title, text, link))
        return result


class Ask(Engine):
    def __str__(self):
        return "%s" % "Ask Search"

    def search(self, search_term):  # [('Titulo','Resumen','URL')]
        driver.get("https://www.ask.com/web?q=" +
                   search_term.replace(' ', '+'))
        response = driver.find_elements_by_css_selector(
            'div.PartialSearchResults-item')
        result = []
        for res in response:
            try:
                title = res.find_elements_by_css_selector(
                    'a.PartialSearchResults-item-title-link')[0].text
                title = normalize(title)
            except:
                title = ''
            try:
                text = res.find_elements_by_css_selector(
                    'p.PartialSearchResults-item-abstract')[0].text
                text = normalize(text)
                text = text.replace('\n', ' ')
            except:
                text = ''
            try:
                link = res.find_elements_by_css_selector(
                    'a.PartialSearchResults-item-title-link')[0]
                link = link.get_attribute("href")
            except:
                link = ''
            result.append((title, text, link))
        return result


class Metacrawle(Engine):
    def __str__(self):
        return "%s" % "Metacrawle Search"

    def search(self, search_term):  # [('Titulo','Resumen','URL')]
        driver.get("https://www.metacrawler.com/serp?q=" +
                   search_term.replace(' ', '+'))
        response = driver.find_elements_by_css_selector('div.web-bing__result')
        result = []
        for res in response:
            try:
                title = res.find_elements_by_css_selector(
                    '.web-bing__title')[0].text
                title = normalize(title)
            except:
                title = ''
            try:
                text = res.find_elements_by_css_selector(
                    '.web-bing__description')[0].text
                text = normalize(text)
                text = text.replace('\n', ' ')
            except:
                text = ''
            try:
                link = res.find_elements_by_css_selector(
                    '.web-bing__title')[0].get_attribute("href")
            except:
                link = ''
            result.append((title, text, link))
        return result


class Combine(Engine):
    def __str__(self):
        return "%s" % "Google&Bing Search"

    def search(self, query):  # [('Titulo','Resumen','URL')]
        rG = Google().search(query)
        rB = Bing().search(query)
        result = zipeer(rG, rB)
        return result
