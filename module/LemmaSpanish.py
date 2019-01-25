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

file_Name = "lemmaDict"
fileObject = open(file_Name,'rb')
lemmaDict = pickle.load(fileObject)

def word_lemmatize(word:Text) -> Text:
    lword = lemmaDict.get(word, word)##Args: (Palabra a trasformar, Palabra retornada en caso de error)
    return lword
