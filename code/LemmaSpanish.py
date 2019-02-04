#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re         import sub as regex_remove
from unidecode  import unidecode
from typing     import Text
import pickle

def normalize(text: Text) -> Text:
    text = text.replace('¿', '')
    text = text.replace("\'s", '')
    text = text.replace("\n", ' ')
    text = unidecode(text)
    text = text.lower()
    text = regex_remove(r'[^\w\s]','',text)
    return text

###Preparo un map a partir del diccionario 'lemmatization-es.txt'####
# lemmaDict = {}
# with open('lemmatization-es.txt', 'rb') as f:
#     data = f.read().decode('utf8').replace(u'\r', u'').split(u'\n')
#     ldata = [a.split(u'\t') for a in data]
#
# for a in ldata:
#     if len(a) >1:
#         lemmaDict[normalize(a[1])] = normalize(a[0])
file_Name = "lemmaDict"
fileObject = open(file_Name,'rb')
lemmaDict = pickle.load(fileObject)
#####################################################################


def word_lemmatize(word:Text) -> Text:
    lword = lemmaDict.get(word, word)##Args: (Palabra a trasformar, Palabra retornada en caso de error)
    return lword


print(word_lemmatize('japones'))
