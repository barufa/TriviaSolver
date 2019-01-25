#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
sys.path.append(os.getcwd())

from Encode    import cleanText
from Internet  import Browser
from Method    import Method, cleanLink, Score, Trivia, WebInfo


def determinate(opt) -> Score:
    # Veo si algun par de opciones aparacion una gran cantidad de veces en comparacion a la opcion restante
    total = float(sum(opt))
    if total == 0.0:
        return None
    opt = [float(t)/total for t in opt]
    if opt[0] >= 0.45 and opt[1] >= 0.45:
        return [0.0, 0.0, 1.0]
    if opt[0] >= 0.45 and opt[2] >= 0.45:
        return [0.0, 1.0, 0.0]
    if opt[1] >= 0.45 and opt[2] >= 0.45:
        return [1.0, 0.0, 0.0]
    return None


class OneNot(Method):
    def solve(self, trivia: Trivia, data: WebInfo, negation: bool, num_pages=3) -> Score:
        if data is None:
            print('OneNot.py: var "data" is None')
            return None
        words_question, words_option = trivia
        l_opt = range(len(words_option))
        score = [0.0 for _ in l_opt]
        nulo  = [0.0 for _ in l_opt]
        aux   = [0.0 for _ in l_opt]
        link_list = cleanLink(data)
        current_links = link_list[0:num_pages]
        # Cuento las apariciones dentro de las primeras paginas
        for link in current_links:
            # Extraigo el texto y lo limpio
            text = Browser().getText(link)
            if text is None:
                try:
                    lnk = link_list[num_pages]
                    num_pages +=1
                    current_links.append(lnk)
                except:
                    pass
                continue
            txt = cleanText(text)
            # Para cada opcion busca su puntaje(cuantas veces aparece)
            for i in l_opt:
                aux[i] = 0.0
                for opt in words_option[i]:
                    aux[i] += txt.count(opt)
                # Luego actualizo score
                aux[i] = aux[i] / float(len(words_option[i]))
                score[i] += aux[i]
            # Determino si existe una respuesta obvia
            res = determinate(aux)
            if not (res is None):
                return res
        # Calculo el resultado final
        total = sum(score)
        if total == 0.0:
            print('OneNot.py: No se obtuvieron resultados')
            return None
        score = [1.0 - (s / float(total)) for s in score]
        return score
