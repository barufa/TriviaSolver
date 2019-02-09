import sys
import os
sys.path.append(os.getcwd())

from ImageShape import ImageShape, rgbdiff, Image
from typing import Text
import cv2

class TriviaLive(ImageShape):
    image_path: Text
    # Simplifica la imagen separando la pregunta de las opciones y eliminando el fondo
    def shapeImage(self, question_path: Text, option_path: Text) -> None:
        resize_box = (475, 220, 895, 680)  # (izq,arr,der,aba) a partir de donde
        img = Image.open(self.image_path).crop(resize_box)
        lenth, height = img.size
        pregunta_box = (0, 0, lenth, height - 270)
        opciones_box = (0, height - 270, lenth, height)
        pregunta = img.crop(pregunta_box)
        opciones = img.crop(opciones_box)
        pregunta.save(question_path)
        opciones.save(option_path)
