all: dependences install test clean
		

dependences:
	sudo pip3 install pipenv
	sudo apt install tesseract-ocr

install:
	pipenv install --dev
	pipenv run python -m spacy download es_core_news_sm
	
test:
	pipenv shell
	./run.sh

clean:
	echo "Eliminando archivos de ejecucion"
	rm -r Imagen/__pycache__
	rm -r Search/__pycache__
	rm -r Solvers/__pycache__
	rm -r Texto/__pycache__
	rm -r __pycache__
