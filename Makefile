all: dependences install test clean
		

dependences:
	sudo apt-get update
	sudo pip3 install pipenv
	sudo apt -y install tesseract-ocr

install:
	pipenv install --dev
	pipenv run python -m spacy download es_core_news_sm
	
test:
	pipenv shell
	./run.sh

clean:
	@echo "Eliminando archivos de ejecucion"
	@find . -name '__pycache__' -exec rm -rv {} +
	@find . -name '*runtimecreationtoremove*' -delete

