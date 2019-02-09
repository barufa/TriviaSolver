import sys
import os
sys.path.append(os.getcwd())

from ImageShape import ImageShape, rgbdiff, Image
from typing import Text

class CashShow(ImageShape):
    image_path: Text = ""
    def __init__(self):  # Path de la imagen a simplificar
        pass
    # Simplifica la imagen separando la pregunta de las opciones y eliminando el fondo
    def shapeImage(self, question_path: Text, option_path: Text) -> None:
        resize_box = (485, 150, 880, 550)  # (izq,arr,der,aba) a partir de donde
        img = Image.open(self.image_path).crop(resize_box)
        lenth, height = img.size
        pregunta_box = (0, 0, lenth, height - 270)
        opciones_box = (0, height - 270, lenth, height)
        pregunta = img.crop(pregunta_box)
        opciones = img.crop(opciones_box)
        pregunta.save(question_path)
        opciones.save(option_path)
