#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.getcwd())

from Encode    import cleanText
from Method    import Method, cleanLink, zip, Score, Trivia, WebInfo
from Internet  import Browser
from typing    import List

class PageScrap(Method):
    def solve(self, trivia: Trivia, data: WebInfo, negation: bool, num_pages=5) -> Score:
        if data is None:
            print('PageScrap.py: var "data" is None')
            return None
        words_question, words_option = trivia
        l_opt = range(len(words_option))
        score = [0.0 for _ in l_opt]
        link_list = cleanLink(data)
        current_links = link_list[0:num_pages]

        # Cuento las apariciones dentro de las primeras paginas
        for link in link_list[0:num_pages]:
            text = Browser().getText(link)
            if not(text is None):
                txt = cleanText(text)
                for i in l_opt:
                    for opt in words_option[i]:
                        score[i] += txt.count(opt)
            else:
                try:
                    lnk = link_list[num_pages]
                    num_pages +=1
                    current_links.append(lnk)
                except:
                    pass
        # Emparejo los resultados(distinta cantidad de palabras en cada opcion)
        for i in l_opt:
            score[i] = score[i] / float(len(words_option[i]))
        # Promedio los resultados
        total = float(sum(score))
        if total == 0:
            print("PageScrap.py: No se obtuvieron resultados")
            return None
        score = [float("%0.3f" % (x / float(total))) for x in score]
        # En caso de que la pregunta este negada
        if negation:
            score = [1.0 - x for x in score]
        return score
