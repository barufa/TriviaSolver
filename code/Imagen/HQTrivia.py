import sys
import os
sys.path.append(os.getcwd())

from ImageShape import ImageShape, rgbdiff, Image
from typing import Text

def tk3(x):
    x1, x2, x3, _ = x
    return (x1,x2,x3)

def findbox(imagen):
    l1, l2, l3, l4 = (50, 150, 250, 360)
    pixels = imagen.load()
    cant = 20
    diff = 10
    start = end = k = 0
    # Pixel que siempre esta dentro de la caja y es del color de la caja
    white = tk3(pixels[10, 200])
    lenth, height = imagen.size
    for i in range(height - 200):  # Busco con 4 lineas donde comienza la caja
        bottom = height - i - 1
        d1 = rgbdiff(tk3(pixels[l1, bottom]), white)
        d2 = rgbdiff(tk3(pixels[l2, bottom]), white)
        d3 = rgbdiff(tk3(pixels[l3, bottom]), white)
        d4 = rgbdiff(tk3(pixels[l4, bottom]), white)
        d = max(max(d1, d2), max(d3, d4))
        if d < diff:  # Si las 4 lineas tienen un color similar al de la caja, aumento en 1
            k = k + 2
        else:
            k = 0
        if k >= cant:
            end = height - (i - k) + 10
            break
    k = 0
    for i in range(height):  # Busco con 4 lineas donde comienza la caja
        top = i + 1
        d1 = rgbdiff(tk3(pixels[l1, top]), white)
        d2 = rgbdiff(tk3(pixels[l2, top]), white)
        d3 = rgbdiff(tk3(pixels[l3, top]), white)
        d4 = rgbdiff(tk3(pixels[l4, top]), white)
        d = max(d1, d4)
        if d < diff:  # Si las 4 lineas tienen un color similar al de la caja, aumento en 1
            k = k + 1
        else:
            k = 0
        if k >= cant:
            start = i - k + 110
            break
    return (0, start, lenth, end)

class HQTrivia(ImageShape):
    image_path: Text = ""
    # Simplifica la imagen separando la pregunta de las opciones y eliminando el fondo
    def shapeImage(self, question_path: Text, option_path: Text) -> None:
        resize_box = (480, 1, 880, 770)  # (izq,arr,der,aba) a partir de donde
        img = Image.open(self.image_path).crop(resize_box)
        img = img.crop(findbox(img))
        lenth, height = img.size
        pregunta_box = (0, 0, lenth, height - 270)
        opciones_box = (0, height - 270, lenth, height)
        pregunta = img.crop(pregunta_box)
        opciones = img.crop(opciones_box)
        pregunta.save(question_path)
        opciones.save(option_path)
