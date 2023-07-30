# Создаём класс слова
class BasicWord:

    def __init__(self, word, subwords):
        """
        Создаём инициализатор (дандер метод) для класса BasicWord
        с полями (исходное слово, набор допустимых подслов)
        """
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        """
        Определяем метод __repr__
        """
        return f"(word = {self.word}, subwords = {self.subwords})"

    def get_verify(self, user_word):
        """
        Проверка введенного слова на длину и
        наличие слова в списке допустимых подслов
        """
        if len(user_word) < 3:
            print("Слишком короткое слово")
            print()
            return False
        elif user_word.strip().lower() not in self.subwords:
            print("Неверно")
            print()
            return False
        elif user_word.strip().lower() in self.subwords:
            print("Верно")
            print()
            return True

    def get_len_subwords(self):
        """
        Подсчёт количества подслов
        """
        return len(self.subwords)
