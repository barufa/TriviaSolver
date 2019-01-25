#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.getcwd() + '/Search')
sys.path.append(os.getcwd() + '/Solvers')
sys.path.append(os.getcwd() + '/Texto')
sys.path.append(os.getcwd() + '/Imagen')

from time                   import time, sleep
from Head                   import solve
from typing                 import Tuple, List, Text, Optional
from Encode                 import normalize, tokenize
from Imagen.InGame          import InGame
from Search.Combine         import Combine
from Texto.GoogleVision     import GoogleVision
from Solvers.CompleteSearch import CompleteSearch
from Solvers.WordCount      import WordCount


def saveanswer(score, respuestas, partial_time):
    nopt, pnt = getanswer(score)
    opt = chr(nopt+65)
    response = "Respuesta: " + str(opt)
    response += " con " + str(pnt)
    response += " en " + str(partial_time) + " segundos\n"
    print(response)
    respuestas += opt + '\n'
    return respuestas


def getanswer(puntos: List[float]) -> Tuple[int, float]:
    r = max(puntos)
    l_pnts = range(len(puntos))
    for i in l_pnts:
        if puntos[i] == r:
            return (i, r)  # (Opcion,Puntaje)
    return (0,0.0)


def main(args):
    print("Iniciando Programa")
    sleep(1)
    tiempo_inicial = time()
    respuestas = ''
    # Mientras ejecuto tengo en cuenta el tiempo parcial de cada pregunta y el tiempo total
    # Para que el programa funcione, no deberia demorar mas de 10 segundos por trivia
    for pregunta in args[1:]:
        print("Resolviendo " + pregunta)
        partial_time = time()
        # Resuelvo la trivia
        score = solve(Combine(), CompleteSearch(),
                      GoogleVision(), InGame(pregunta))
        respuestas = saveanswer(score, respuestas, (time()-partial_time))
    # Almaceno en un archivo las respuestas para comparar los resultados
    archivo = open("Respuestas.txt", "w")
    archivo.write(respuestas)
    tiempo_total = time() - tiempo_inicial
    print("Fin del programa con " + str(tiempo_total))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

##Posibles problemas:
# Solucionar problemas urls
# Analizar fallos en las preguntas (RA,...,RD)
# Dataset: Generar un dataset para probar el programa
# Tipos de pregunta: Clasificar las preguntas para utilizar distintos metodos y mejorar efectividad
# Aprovechar lemm. de alguna forma(tener cuidado con las entidades, aplicar solo a verbos?)
# Utilizar AI de google(actions on Google) o IBM(bluemix)
# Tiempo de ejecucion y multithreading(Es posible lanzar un timeout)
# Mejorar Main(hacerlo comfigurable desde consola y mejorar codigo)
