import sys
import os
sys.path.append(os.getcwd())

from ImageShape import ImageShape, rgbdiff, Image, ImageOps
from typing import Text

#import cv2

# def image_filter(file_name,filter):
#     img = cv2.imread(file_name, 0)
#     _,img = cv2.threshold(img,127,255,filter)
#     cv2.imwrite(file_name,img)
#     pass

def findbox(imagen):  # No usar este metodo
    l1, l2, l3, l4 = (50, 150, 250, 350)
    pixels = imagen.load()
    cant = 20
    diff = 10
    start = end = k = 0
    # Pixel que siempre esta dentro de la caja y es del color de la caja
    black = pixels[10, 200]
    lenth, height = imagen.size
    for i in range(height - 200):  # Busco con 4 lineas donde comienza la caja
        bottom = height - i - 1
        d1 = rgbdiff(pixels[l1, bottom], black)
        d2 = rgbdiff(pixels[l2, bottom], black)
        d3 = rgbdiff(pixels[l3, bottom], black)
        d4 = rgbdiff(pixels[l4, bottom], black)
        d = max(max(d1, d2), max(d3, d4))
        if d < diff:  # Si las 4 lineas tienen un color similar al de la caja, aumento en 1
            k = k + 1
        else:
            k = 0
        if k >= cant:
            end = height - (i - k)
            break
    k = 0
    for i in range(height):  # Busco con 4 lineas donde comienza la caja
        top = i + 1
        d1 = rgbdiff(pixels[l1, top], black)
        d4 = rgbdiff(pixels[l4, top], black)
        d = max(d1, d4)
        if d < diff:  # Si las 4 lineas tienen un color similar al de la caja, aumento en 1
            k = k + 1
        else:
            k = 0
        if k >= cant:
            start = i - k + 120
            break
    return (0, start, lenth, end)


class InGame(ImageShape):
    image_path: Text
    # Simplifica la imagen separando la pregunta de las opciones y eliminando el fondo
    def shapeImage(self, question_path: Text, option_path: Text) -> None:
        resize_box = (495, 1, 875, 770)  # (izq,arr,der,aba) a partir de donde
        img = Image.open(self.image_path).crop(resize_box)
        img = img.crop(findbox(img))
        lenth, height = img.size
        pregunta_box = (0, 0, lenth, height - 270)
        opciones_box = (0, height - 270, lenth, height)
        pregunta = img.crop(pregunta_box)
        opciones = img.crop(opciones_box)
        pregunta = ImageOps.invert(pregunta)
        pregunta.save(question_path)
        opciones.save(option_path)
