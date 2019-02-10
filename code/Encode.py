#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
from nltk.tokenize       import RegexpTokenizer, word_tokenize
from nltk.corpus         import stopwords as stopw
from nltk.stem.snowball  import SpanishStemmer
from re                  import sub as regex_remove
from unidecode           import unidecode
from typing              import Tuple, List, Text, Optional, Any


def normalize(text: Text) -> Text:
    text = text.replace('¿', '')
    text = text.replace("\'s", '')
    text = text.replace("\n", ' ')
    text = unidecode(text)
    text = text.lower()
    text = regex_remove(r'[^\w\s]','',text)
    return text

lemmaDict = {}
stopwords = {}
# lemmaDict = pickle.load(open("es_lemmaDict",'rb'))
# stopwords = set([normalize(x) for x in stopwords.words("spanish")])
# stopwords.remove('estados')
# stopwords.add('siguientes')

def idioma(lang: Text):
    global lemmaDict
    global stopwords
    if lang=="spa":
        lemmaDict = pickle.load(open("es_lemmaDict",'rb'))
        stopwords = set([normalize(x) for x in stopw.words("spanish")])
        stopwords.remove('estados')
        stopwords.add('siguientes')
    else:
        lemmaDict = pickle.load(open("en_lemmaDict",'rb'))
        stopwords = set([normalize(x) for x in stopw.words("english")])

def tokenize(sentence: Text)-> Text:
    sentence = regex_remove(r'\[\w*\]','',sentence)
    sentence = normalize(sentence)
    tokens = word_tokenize(sentence)
    filtered_words = [w for w in tokens if not w in stopwords]
    sentence = " ".join(filtered_words)
    return sentence

def cleanText(text: Text) -> List[Text]:
    text = tokenize(text)
    tokenizer = RegexpTokenizer(r'\w+')
    ltext = tokenizer.tokenize(text)
    return ltext

#Ver si realmente es util
def steming(text: Text) -> List[Text]:
    stem = SpanishStemmer()
    ltext = [stem.stem(w) for w in cleanText(text)]
    return ltext

def word_lemmatize(word:Text) -> Text:
    lword = lemmaDict.get(word, word)##Args: (Palabra a trasformar, Palabra retornada en caso de error)
    return lword

def lemmatizeall(txt: Text) -> List[Text]:
    ltext = cleanText(txt)
    return [word_lemmatize(word) for word in ltext]

# def lemmatize(txt: Text) -> List[Text]: #Tiene en cuenta las entidades
# ##########Funcion Auxiliar#################################
#     def lem(ents: List[Any],txt: Text,e=0,times=3) -> Text:
#         if len(ents)<=e:
#             ltext = cleanText(txt)
#             lem_fun = (lambda lword: [word_lemmatize(word) for word in lword])
#             for i in range(times):
#                 ltext = lem_fun(ltext)
#             s = ' '.join(ltext)
#             return s
#         else:
#             ent = ents[e].text
#             ltxt = [lem(ents,ls,e+1,times) for ls in txt.split(ent)]
#             return (' '+ent+' ').join(ltxt)
# ###########################################################
#     doc = spc(txt)
#     t = lem(doc.ents,txt)
#     return cleanText(t)
