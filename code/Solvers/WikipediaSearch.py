import sys,os
sys.path.append(os.getcwd())

from Encode        import word_lemmatize, lemmatizeall
from Internet      import Browser
from Method        import Method, cleanLink, Score, Trivia, WebInfo
from nltk.tokenize import sent_tokenize
from Internet      import Browser
from typing        import Text, List


class WikipediaSearch(Method):
    def solve(self, trivia: Trivia, data: WebInfo, negation: bool) -> Score:
        if data is None:
            print('WikipediaSearch.py: var "data" is None')
            return None
        #Preparo la informacion
        words_question, words_option = trivia
        lwords_question = lemmatizeall(' '.join(words_question))
        lwords_option = [lemmatizeall(' '.join(list_option)) for list_option in words_option]

        l_opt = range(len(words_option))
        score = [0.0 for _ in l_opt]
        link_list = cleanLink(data)
        current_links = [link for link in link_list if 'es.wikipedia' in link]
        # Cuento las apariciones dentro de las primeras paginas
        for link in current_links:
            text = Browser().getText(link)
            if not(text is None):
                lsent = [lemmatizeall(text) for text in sent_tokenize(text)]
                for i in l_opt:
                    for sentence in lsent:
                        score[i] += coef_sent(sentence,lwords_question,lwords_option[i])
        score = [p**2 for p in score]

        # Promedio los resultados
        total = float(sum(score))
        if total == 0.0 or (total-max(score))==0:
            print("WikipediaSearch.py: No se obtuvieron resultados")
            return None
        score = [float("%0.3f" % (x/total)) for x in score]
        # En caso de que la pregunta este negada
        if negation:
            score = [1.0 - x for x in score]
        return score

def coef_sent(text: List[Text],preg: List[Text],resp: List[Text]) -> float:
    cpreg = 0
    cresp = 0
    crest = 0
    for word in text:
        inp = bool(word in preg)
        inr = bool(word in resp)
        if inp:
            cpreg = cpreg + 1
        if inr:
            cresp = cresp + 1
        if (not inp) and (not inr):
            crest = crest + 1

    if(cpreg==0 or cresp==0):
        return 0.0

    pcrest = crest / float(len(text))
    pcpreg = cpreg / float(len(preg))
    pcresp = cresp / float(len(resp))

    return float((1.0 - pcrest) * ((pcpreg * pcresp)))
