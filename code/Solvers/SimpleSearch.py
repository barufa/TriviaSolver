#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.getcwd())

from Encode import cleanText
from Method import Method, cleanLink, zip, Score, Trivia, WebInfo


class SimpleSearch(Method):
    def solve(self, trivia: Trivia, data: WebInfo, negation: bool) -> Score:
        if data is None:
            print('SimpleSearch.py: var "data" is None')
            return None
        words_question, words_option = trivia
        l_opt = range(len(words_option))
        score = [0.0 for _ in l_opt]
        # Cuento las apariciones en los titulos y resumenes
        for name, description, _ in data:
            name = cleanText(name)
            description = cleanText(description)
            for i in l_opt:
                for opt in words_option[i]:
                    score[i] += 2.0 * name.count(opt) + description.count(opt)
        # Emparejo los resultados(distinta cantidad de palabras en cada opcion)

        for i in l_opt:
            score[i] = score[i] / float(len(words_option[i]))
        # Promedio los resultados
        total = float(sum(score))
        if total == 0.0:
            print("SimpleSearch.py: No se obtuvieron resultados")
            return None
        score = [float("%0.3f" % (x/total)) for x in score]
        # En caso de que la pregunta este negada
        if negation:
            score = [1.0 - x for x in score]
        return score
