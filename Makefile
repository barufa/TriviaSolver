all: dependences install test clean
		

dependences:
	sudo apt-get update
	sudo pip3 install pipenv
	sudo apt -y install tesseract-ocr tesseract-ocr-spa tesseract-ocr-eng

install:
	pipenv install --dev
	pipenv run python -m spacy download es_core_news_sm
	pipenv run python -m spacy download en_core_web_sm
	pipenv run python -m spacy download xx_ent_wiki_sm
	pipenv run python -m nltk.downloader stopwords
	pipenv run python -m nltk.downloader punkt
	
test:
	pipenv run ./test.sh

clean:
	@echo "Eliminando archivos de ejecucion"
	@find . -name '__pycache__' -exec rm -rv {} +
	@find . -name '*runtimecreationtoremove*' -delete

