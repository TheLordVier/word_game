# Импортируем функцию чтения данных с внешнего ресурса из файла utils.py
from utils import load_random_word
# Импортируем из файла player.py класс Player
from player import Player

# Создаём поле основной функции
if __name__ == '__main__':
    # Создаём переменную с путём к внешнему ресурсу
    data_source = "https://api.npoint.io/288d450a91c2243f31fe"
    # Применяем функцию load_random_word с чтением с внешнего ресурса
    basic_word = load_random_word(data_source)
    # Определяем длину списка допустимых подслов
    len_subwords = basic_word.get_len_subwords()
    # Просим пользователя представиться
    user_name = input("Введите имя игрока:\n").title()
    print()
    # Создаём экземпляр класса Player с полями
    # (имя пользователя, использованные слова)
    words_used = list()
    player = Player(user_name, words_used)
    # Создаём стартовое приветствие пользователя и предлагаем начать
    print(f'Привет, {player.name}\n'
            f'Составьте {len_subwords} слов из слова {basic_word.word.upper()}\n'
            f'Слова должны быть не короче 3 букв\n'
            f'Чтобы закончить игру, угадайте все слова или напишите "stop"\n'
            f'Поехали, ваше первое слово?')
    print()
    # Запускаем основной цикл программы и запрашиваем ответы
    # у пользователя, далее записываем их и выводим результаты пользователю
    i = 0
    while i < len(basic_word.subwords):
        user_input = input().lower()
        loop_exit_1 = "стоп"
        loop_exit_2 = "stop"
        i += 1
        if user_input.lower() == loop_exit_1.lower():
            print()
            break
        elif user_input.lower() == loop_exit_2.lower():
            print()
            break
        elif user_input in words_used:
            player.get_check_word(user_input)
        elif basic_word.get_verify(user_input):
            player.add_word(user_input)
    print(f"Игра завершена, вы угадали {player.count_words_used()} слов!")
