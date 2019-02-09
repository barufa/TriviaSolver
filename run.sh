#!/bin/bash

juego="InGame"
dir=$(pwd)
preguntas=""

echo "Preparando Ejecucion"
#Corriendo Casos
#export GOOGLE_APPLICATION_CREDENTIALS="Keys/YourKey.json"
preguntas="$dir/questions/$juego/1.png"
for i in 2 #3 4 5 6 7 8 9 10 11 12
do
	preguntas=$preguntas"+$dir/questions/$juego/$i.png"
done

cd code
time python3 TriviaBot.py -src=$preguntas -o=Tesseract
echo "Fin de la Ejecucion"
