#!/bin/bash

juego="A"
dir=$(pwd)
preguntas=""

echo "Preparando Ejecucion"
#Corriendo Casos
export GOOGLE_APPLICATION_CREDENTIALS="YourTriviaProject.json"
for i in 1 2 3 4 5 6 7 8 9 10 11 12
do
	preguntas=$preguntas" $dir/questions/$juego/$i.png"
done

cd module
time python3 Main.py $preguntas
rm -r Imagen/__pycache__
rm -r Search/__pycache__
rm -r Solvers/__pycache__
rm -r Texto/__pycache__
rm -r __pycache__
