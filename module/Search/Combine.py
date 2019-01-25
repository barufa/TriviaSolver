#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
sys.path.append(os.getcwd())

from Engine    import Engine, WebInfo
from typing    import Text, List, Tuple
from Bing      import Bing
from Google    import Google

class Combine(Engine):
	def __str__(self):
		return "%s" % "Google&Bing Search"
	def search(self,search_term: Text) -> WebInfo:##[('Titulo','Resumen','URL')]
		resG = Google().search(search_term)
		resB = Bing().search(search_term)
		results:List[Tuple[Text, Text, Text]] = []
		if resG is None and resB is None:
			print("Combine.py: No se obtuvo informacion de los motores Google ni Bing")
			return None
		else:
			if resG is None:
				resG = []
				print("Combine.py: No se obtuvo informacion de Google")
			if resB is None:
				resB = []
				print("Combine.py: No se obtuvo informacion de Bing")
			results = resG+resB
		return results
