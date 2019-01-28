#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.getcwd())

from typing        import Text, List, TypeVar, Tuple, Optional
from Search.Engine import WebInfo

Score = Optional[List[float]]
Trivia = Tuple[Text, List[Text]]  # (Pregunta,[Opcion 1, Opcion 2, Opcion 3])
Tvar1 = TypeVar('Tvar1')
Tvar2 = TypeVar('Tvar2')

badlink = ['instagram','.pdf','.doc','youtube','facebook']

def cleanLink(linklist: WebInfo) -> List[Text]:
	if linklist is None:
		return []
	return [l for _,_,l in linklist if sum([l.count(p) for p in badlink])==0]

def zipaux(lx: List[Tvar1],ly: List[Tvar2]) -> List[Tuple[Tvar1,Tvar2]]:
	if len(lx)==0 or len(ly)==0:
		return []
	return zipaux(lx[1:],ly[1:]) + [(lx[0],ly[0])]

def zip(lx: List[Tvar1],ly: List[Tvar2]) -> List[Tuple[Tvar1,Tvar2]]:
	list = zipaux(lx,ly)
	list.reverse()
	return list

class Method:##Clase Base
	def solve(self,trivia: Trivia,data: WebInfo,negation: bool)-> Score:
		pass

#Posibles Extensiones:
#Analize(), Analisa el texto de los titulos y el resumen(no solo cuenta apariciones, busca por distancia entre las palabras y similitud)
#AnalizePage(), Descarga las paginas y analisa el texto(no solo cuenta apariciones, busca por distancia entre las palabras y similitudes)
#SmartSolver(), combina Analize y AnalizePage (Pensar en multithreading?)
#WatsonNLP(), utilizar la IA de watson para responder las preguntas
#Ambos(), cuando se necesitan encontrar dos coincidencias
#Combineoption(), busca la pregunta combinando con datos de las opciones(tardaria mucho)
