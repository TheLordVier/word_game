# Создаём класс игрока
class Player:

    def __init__(self, name, words_used):
        """
        Создаём инициализатор (дандер метод) для класса Player
        с полями (имя пользователя, использованные слова пользователя)
        """
        self.name = name
        self.words_used = words_used

    def __repr__(self):
        """
        Определяем метод __repr__
        """
        return self.name, self.words_used

    def add_word(self, word):
        """
        Добавление слова в использованные слова
        """
        self.words_used.append(word.lower())

    def count_words_used(self):
        """
        Получение количества использованных слов
        """
        return len(self.words_used)

    def get_check_word(self, word):
        """
        Проверка использования данного слова до этого
        """
        if word in self.words_used:
            print("Уже использовано")
            print()
            return True
        else:
            return False
