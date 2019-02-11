# TriviaBot

A question answering system developed in python focused on solving trivia questions that apply techniques of natural language processing and web scraping.
This program is focused on the app InGame, but it also works with other trivia apps such as HQTrivia, CashShow and TriviaLive(Preguntados).

Its **accuracy for the InGame application is 86%**, which means that it gets just over 10 correct answers every 12 questions.

## Getting Started

First of all, you have to donwload this repository and execute:
```
$ git clone https://github.com/barufa/TriviaBot.git
$ cd TriviaBot
```
In order to install the program, you need to:
* Install pipenv and tesseract
* Install all program dependences and models of spacy
* Test the program
For this purpose there is a simple makefile in the repository:
```
$ make dependences
$ make install
$ make test
$ make clean
```
If everything ends correctly, the program is ready to be used.

It is highly recommended to use Google Cloud services to avoid character recognition errors.
For this it is necessary to create an account in Google Cloud and register in the services of Google Cloud Vision.

## How it works:

This project uses python 3.6. In particular the packages/libraries used are...
* nltk
* regex
* unidecode
* mypy
* urllib3
* lxml
* requests
* google-cloud
* pytesseract
* opencv-python
To make the handling of dependencies easier, we use pipenv.

## Usage

Once the program is installed, it can be executed through the following commands:
```
$ pipenv shell
$ python3 TriviaBot.py [OPTIONS]
```
Where options are:
* --help: Show this help message and exit
* --Game: Game interface. The possible values are: InGame, HQTrivia, CashShow, TriviaLive.
* --Search: Search engine that will use the program. The possible values are: Google, Ask, Bing, Combine, Metacrawle.
* --Method: Main method used to solve the trivia. The available methods are: SimpleSearch, PageScrape, WikipediaSearch, CompleteSearch.
* --OCR: Character recognition engine to be used. The possible values are: FreeOCR, Tesseract, GoogleVision.
* --Source: Source from which the trivia will be obtained
* --Language: Language in which you want to run the program. The possible values are: Spa (Spanish), Eng (English).

An example:
>python3 TriviaBot.py --Source=../questions/InGame/1.png+../questions/InGame/2.png --Game=InGame --OCR=Tesseract

## Screenshots

![](/questions/HQTrivia/HQTrivia.gif)
![](/questions/InGame/InGame.gif)
![](/questions/CashShow/CashShow.gif)
![](/questions/TriviaLive/TriviaLive.gif)


**WORK IN PROGRESS**
