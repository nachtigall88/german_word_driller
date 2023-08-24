import sqlite3 as sq
from random import choice


class Wort:
    """клас для опису екземпяру для отримання та запису для зберігання даних"""

    def __init__(self, word, translation, art=None):
        self.word = word
        self.translation = translation
        self.art = art

    def __str__(self):
        if self.art:
            return f'{self.art} {self.word} - {self.translation}'
        else:
            return f'{self.word} - {self.translation}'


class Driller:
    """клас для опису логіки створення бази даних, запису даних в базу та отримання рандомного результату"""
    pass

    def __init__(self):
        self.__random_data = None
        self.make_data_base()

    def __call__(self, *args, **kwargs):
        pass

    def __str__(self):
        self.show_random()

    def show_random(self):
        return self.__random_data

    def make_data_base(self):
        """
        функція для створення бази даних
        :return:
        """
        with sq.connect('word_data.db') as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTs words (
            art TEXT DEFAULT NULL,
            word TEXT,
            translation TEXT
            )""")

    def add_data(self, data: Wort):
        """
        функція для збереження даних в базі
        :param data:
        :return:
        """
        with sq.connect('word_data.db') as con:
            cur = con.cursor()
            cur.execute(f"""INSERT INTO words VALUES (
            '{data.art}', '{data.word}', '{data.translation}'
            )""")

    def get_random_data(self):
        """
        функція для отримання рандомних даних із бази
        :return:
        """
        pass


if __name__ == '__main__':
    w = Driller()
