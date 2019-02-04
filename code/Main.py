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
from Imagen.ImageShape      import ImageShape
from Search.Engine          import Engine
from Texto.OCR              import OCR
from Solvers.Method         import Method
from Config                 import config_console

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
    print("Iniciando Programa...")
    tiempo_inicial = time()
    respuestas = ''

    #Configuro la ejecucion del programa con los datos del usuario
    conf = config_console()
    Engine    = conf['Engine']
    OCR       = conf['OCR']
    Method    = conf['Method']
    Game      = conf['Game']
    Preguntas = conf['Source']
    # Mientras ejecuto tengo en cuenta el tiempo parcial de cada pregunta y el tiempo total
    # Para que el programa funcione, no deberia demorar mas de 10 segundos por trivia(depende de la velocidad de internet)
    for pregunta in Preguntas:
        print("Resolviendo " + pregunta)
        partial_time = time()
        # Resuelvo la trivia
        Game.set(pregunta)
        score = solve(Engine, Method, OCR, Game)
        respuestas = saveanswer(score, respuestas, (time()-partial_time))
    # Almaceno en un archivo las respuestas para comparar los resultados
    archivo = open("Respuestas.txt", "w")
    archivo.write(respuestas)
    archivo.close()
    Engine.clear()
    tiempo_total = time() - tiempo_inicial
    print("Fin del programa con " + str(tiempo_total))

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

##Posibles problemas y extensiones:
# Analizar fallos en las preguntas (RA,...,RD)
# Tipos de pregunta: Clasificar las preguntas para utilizar distintos metodos y mejorar efectividad
# Utilizar AI de google(actions on Google) o IBM(bluemix)
# Tiempo de ejecucion y multithreading(Es posible lanzar un timeout)
# Agregar idiomas
# Incluir TriviaDB(opentdb.com) para mejorar efectividad
# Agregar opcion -test
# Argegar deteccion de bordes a ImageShape
# Investigar interfaz Android
