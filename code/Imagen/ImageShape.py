#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL     import Image, ImageOps
from typing  import Text
from typing import Union, Tuple

Number = Union[int,float]
Tripla = Tuple[Number,Number,Number]

def rgbdiff(x:Tripla, y:Tripla) -> Number:  # Auxiliar para findbox
    x1, x2, x3 = x
    y1, y2, y3 = y
    return abs(x1 - y1) + abs(x2 - y2) + abs(x3 - y3)

class ImageShape:
    image_path: Text = ""
    def set(self,path: Text):
        self.image_path = path
    def shapeImage(self, question_path: Text, option_path: Text) -> None:
        pass

# ~ x = ImageShape('path_imagen')
#~ x.shapeImage('path_pregunta','path_opciones')

# Tratar de disminuir el peso de la imagen sin perder reconocimiento
# Agregrar para preguntados y buscar otros
