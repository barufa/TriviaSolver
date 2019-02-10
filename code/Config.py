import sys
import os
sys.path.append(os.getcwd() + '/Search')
sys.path.append(os.getcwd() + '/Solvers')
sys.path.append(os.getcwd() + '/Texto')
sys.path.append(os.getcwd() + '/Imagen')

import argparse
import Encode
from typing import Tuple, List, Text, Optional


def set_game(config, args):
    game = args.Game.lower()
    if(game == 'ingame'):
        from Imagen.InGame import InGame
        config['Game'] = InGame()
    elif(game == 'hqtrivia'):
        from Imagen.HQTrivia import HQTrivia
        config['Game'] = HQTrivia()
    elif(game == 'cashshow'):
        from Imagen.CashShow import CashShow
        config['Game'] = CashShow()
    elif(game == 'trivialive'):
        from Imagen.TriviaLive import TriviaLive
        config['Game'] = TriviaLive()
    else:
        print('ERROR: La interfaz de juego seleccionado no se corresponde con ninguna de las disponibles')
        exit(1)
    pass


def set_engine(config, args):
    engine = args.Search.lower()
    if(engine == 'ask'):
        from Search.Ask import Ask
        config['Engine'] = Ask()
    elif(engine == 'bing'):
        from Search.Bing import Bing
        config['Engine'] = Bing()
    elif(engine == 'combine'):
        from Search.Combine import Combine
        config['Engine'] = Combine()
    elif(engine == 'google'):
        from Search.Google import Google
        config['Engine'] = Google()
    elif(engine == 'metacrawle'):
        from Search.Metacrawle import Metacrawle
        config['Engine'] = Metacrawle()
    else:
        print('ERROR: El motor de busqueda seleccionado no se corresponde con ninguno de los motores disponibles')
        exit(2)
    pass


def set_solver(config, args):
    method = args.Method.lower()
    if(method == 'completesearch'):
        from Solvers.CompleteSearch import CompleteSearch
        config['Method'] = CompleteSearch()
    elif(method == 'pagescrape'):
        from Solvers.PageScrape import PageScrape
        config['Method'] = PageScrape()
    elif(method == ''):
        from Solvers.SimpleSearch import SimpleSearch
        config['Method'] = SimpleSearch()
    elif(method == ''):
        from Solvers.WikipediaSearch import WikipediaSearch
        config['Method'] = WikipediaSearch()
    else:
        print('ERROR: El metodo de resolucion seleccionado no se corresponde con ninguno de los disponibles')
        exit(3)
    pass


def set_ocr(config, args):
    ocr = args.OCR.lower()
    if(ocr == 'freeocr'):
        from Texto.FreeOCR import FreeOCR
        config['OCR'] = FreeOCR()
        pass
    elif(ocr == 'tesseract'):
        from Texto.Tesseract import Tesseract
        config['OCR'] = Tesseract()
        pass
    elif(ocr == 'googlevision'):
        from Texto.GoogleVision import GoogleVision
        config['OCR'] = GoogleVision()
        pass
    else:
        print('ERROR: El motor de reconocimiento de caracteres seleccionado no se corresponde con ninguno de los disponibles')
        exit(4)
    pass


def set_src(config, args):
    # Actualmente la parte de src no esta definida ni implementada
    try:
        src = args.Source
        config['Source'] = src.split('+')
    except:
        print('ERROR: Se debe especificar una fuente')
        exit(5)
    pass


def set_lang(config, args):
    lang = args.Language.lower()
    if(lang == 'spa' or lang == 'eng'):
        Encode.idioma(lang)
    else:
        print('ERROR: Se debe especificar un idioma')
        exit(6)
    pass


def config_console():
    conf = {}
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--Game',  type=str,
                        help='Interfaz del juego a analizar. Los valores posibles son:\n* InGame\n* HQTrivia\n* CashShow', default='Ingame')
    parser.add_argument('-s', '--Search', type=str,
                        help='Motor de busqueda que utilizara el programa. Los valores posibles son:\n* Google\n* Ask\n* Bing\n* Combine\n* Metacrawle', default='Google')
    parser.add_argument('-m', '--Method', type=str,
                        help='Metodo principal utilizado para resolver las trivias. Los metodos disponibles son:\n* SimpleSearch\n* PageScrape\n* WikipediaSearch\n* CompleteSearch', default='CompleteSearch')
    parser.add_argument('-o', '--OCR', type=str,
                        help='Motor de reconocimiento de caracteres a utilizar. Los valores posibles son:\n* FreeOCR\n* Tesseract\n* GoogleVision', default='GoogleVision')
    parser.add_argument('-src', '--Source', type=str,
                        help='Funte desde la cual se obtendran las trivias')
    parser.add_argument('-lang', '--Language', type=str,
                        help='Idioma en el cual desea correr el programa. Los valores posibles son:\n* Spa\tEspañol\n* Eng\tIngles',default='spa')
    args = parser.parse_args()

    set_game(conf, args)
    set_engine(conf, args)
    set_ocr(conf, args)
    set_solver(conf, args)
    set_src(conf, args)
    set_lang(conf, args)

    return conf
