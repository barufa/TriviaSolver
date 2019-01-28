#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.getcwd())

from SimpleSearch        import SimpleSearch
from PageScrap           import PageScrap
from WikipediaSearch     import WikipediaSearch
from Method              import Method, cleanLink, zip, Score, Trivia, WebInfo

class CompleteSearch(Method):
    def solve(self, trivia: Trivia, data: WebInfo, negation: bool, lamb: float = 0.5) -> Score:
        if data is None:
            print('CompleteSearch.py: var "data" is None')
            return None
        words_question, words_option = trivia
        l_opt = range(len(words_option))
        nulo = [0.0 for _ in l_opt]
        #WikipediaSearch
        score_wiki = WikipediaSearch().solve(trivia,data,negation)
        if score_wiki is None:
            score_wiki = nulo
        # Si simple search encontro una respuesta clara, la retorno
        if max(score_wiki) > 0.95:
            return score_wiki
        #SimpleSearch
        score_simple = SimpleSearch().solve(trivia, data, negation)
        if score_simple is None:
            score_simple = nulo
        # Si simple search encontro una respuesta clara, la retorno
        if max(score_simple) > 0.95:
            return score_simple
        #PageScrap
        score_page = PageScrap().solve(trivia, data, negation, 5)
        if score_page is None:
            score_page = nulo
        #Calculo las respuestas teniendo en cuenta el parametro lamb
        score = [0.0 for _ in l_opt]
        for i in l_opt:
            score[i] = score_page[i] * (1.0 + lamb) + score_simple[i] + score_wiki[i]
        total = float(sum(score))
        if score_page == nulo or score_simple == nulo:
            total *= 2
        if total == 0:
            print("CompleteSearch.py: No se obtuvieron resultados")
            return None
        score = [float("%0.3f" % (x/total)) for x in score]
        return score
