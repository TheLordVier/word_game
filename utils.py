# Импортируем стандартные модули json, random, urllib.request
import json
import random
import urllib.request
# Импортируем из файла basic_word.py класс BasicWord
from basic_word import BasicWord


def load_random_word(filename):
    """
    Создаём функцию чтения данных с внешнего ресурса,
    с дальнейшим выбором случайного слова
    """
    with urllib.request.urlopen(filename) as file:
        data = json.load(file)
        choice_word = random.choice(data)
        data_choice = BasicWord(choice_word.get('word'), choice_word.get('subwords'))
    return data_choice
