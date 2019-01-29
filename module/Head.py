#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
sys.path.append(os.getcwd() + '/Search')
sys.path.append(os.getcwd() + '/Solvers')
sys.path.append(os.getcwd() + '/Texto')
sys.path.append(os.getcwd() + '/Imagen')

import random
from Solvers.Method     import Method, Trivia
from Solvers.OneNot     import OneNot
from Search.Engine      import Engine
from Texto.OCR          import OCR
from Imagen.ImageShape  import ImageShape
from Encode             import normalize, tokenize
from typing             import Tuple, List, Text, Optional

from P import preguntas

n_pre = 1

def getTrivia(shaper: ImageShape, ocr: OCR) -> Optional[Trivia]:
    # Nombre que no choca con nada
    file_pregunta = str(str(random.randint(1, 10001)) +
                        'runtimecreationtoremove_question_file.png')
    file_opciones = str(str(random.randint(1, 10001)) +
                        'runtimecreationtoremove_options_file.png')

    # Corto la imagen
    shaper.shapeImage(file_pregunta, file_opciones)

    # Extraigo el texto
    pre_text = ocr.getText(file_pregunta)
    opt_text = ocr.getText(file_opciones)

    # Remuevo el archivo creado por cutImage
    os.remove(file_pregunta)
    os.remove(file_opciones)

    if (pre_text is None) or (opt_text is None):
        return None

    # Limpio las listas de strings
    # Pregunta
    pre_text = normalize(pre_text)
    pre_txt = str(pre_text).split('?')
    while('' in pre_txt):
        pre_txt.remove('')
    pre_text = pre_txt[0]
    pre_text = pre_text.replace('\n', ' ') + '?'

    # Opciones
    opt_text = opt_text.replace('\n','\t')
    opt_text = normalize(opt_text)
    # En caso de que ocr halla leido 'Pregunta N'
    for nu in range(1, 13):
        prg = 'pregunta ' + str(nu)
        if pre_text.count(prg) > 0:
            pre_text = pre_text.replace(prg, '')
            break
    opt_txt = str(opt_text).split('\t')
    while('' in opt_txt):
        opt_txt.remove('')

    return (pre_text, opt_txt)


def cleanTrivia(trivia: Trivia) -> Optional[Tuple[Text, List[Text], List[List[Text]], bool]]:

    if trivia is None:
        return None

    pregunta, opciones = trivia

    # Proceso la pregunta
    words_question = normalize(pregunta).replace('?', '')
    token_question = tokenize(words_question).split(' ')

    if token_question[0] == 'pregunta' and token_question[1] in range(1, 13):
        token_question = token_question[2:]

    # Proceso las opciones
    words_option = [normalize(x) for x in opciones]
    words_option = [tokenize(l) for l in words_option]
    token_option = [l.split(' ') for l in words_option]
    # Modificar en caso de realizar analisis mas complejos
    token_option = [list(set(l)) for l in token_option]

    query = ' '.join(token_question)
    return (query, token_question, token_option, ' no ' in pregunta)


def procesar_imagen(shaper: ImageShape, ocr: OCR) -> Trivia:
    ######################################
    # Para hacer el proceso completo #####
    # trivia = getTrivia(shaper, ocr)
    ######################################
    # Evitando usar OCR ##################
    global n_pre
    trivia = preguntas[n_pre]
    n_pre+=1
    ######################################
    if trivia is None:
        return None
    pregunta, opciones = trivia
    print('Pregunta: ' + pregunta)
    print('Opciones: \n\t1: ' +
          opciones[0] + '\n\t2: ' + opciones[1] + '\n\t3: ' + opciones[2])
    return trivia

def solve(motor: Engine, metodo: Method, ocr: OCR, shaper: ImageShape):
    trivia = procesar_imagen(shaper, ocr)
    pregunta, opciones = trivia
    if (pregunta.count(' no ') > 0) and (pregunta.count('cual ') or pregunta.count('cuales ')):
        metodo = OneNot()
    cl_trivia = cleanTrivia(trivia)
    if not (cl_trivia is None):
        query, question, options, neg = cl_trivia
        webdata = motor.search(query)
        result = metodo.solve((question, options), webdata, neg)
        if not (result is None):
            return result
    #Buscar metodo probabilistico para responder
    n_opt = len(opciones)
    r = random.randint(0,n_opt-1)
    result = [0.0 for l in range(n_opt)]
    result[r] = 1.0
    return result
