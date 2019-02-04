#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
from google.cloud import vision
from OCR          import OCR
from typing       import Text, Optional

#Son necesarios los permisos de Google Cloud para que funcione

class GoogleVision(OCR):
    def getText(self, path: Text) -> Optional[Text]:
        # Creo el cliente y abro el archivo
        client = vision.ImageAnnotatorClient()
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        # Extraigo el texto con Cloud Vision
        image = vision.types.Image(content=content)
        response = client.document_text_detection(image=image)
        texts = response.text_annotations
        # Trato nuevamente en caso de error(rara ocasion)
        try:
            if len(texts) == 0:
                response = client.document_text_detection(image=image)
                texts = response.text_annotations
                # En caso de que este vacio y no pueda indexar
            # texts es muy complejo, tener cuidado
            result = texts[0].description
            return result
        except:
            print("Fallo Google Vision")
            pass
        return None
