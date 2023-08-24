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

    def __call__(self, data: Wort):
        self.add_data(data)

    def __str__(self):
        self.show_random()

    def show_random(self):
        return self.__random_data


    @staticmethod
    def check_if_exists(data):
        """метод перевіряє, чи є слово, що додається, в базі"""
        flag = True
        with sq.connect('word_data.db') as con:
            cur = con.cursor()
            cur.execute("""SELECT * FROM words""")
            result = cur.fetchall()
            for i in result:
                if data in i:
                    flag = False
        return flag

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
        if self.check_if_exists(data.word):
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
        with sq.connect('word_data.db') as con:
            cur = con.cursor()
            cur.execute("""SELECT * FROM words""")
            result = cur.fetchall()
            self.__random_data = choice(result)




if __name__ == '__main__':
    d = Driller()
    w = Wort('Uhr', 'годинник', 'die')
    w2 = Wort('betreten', 'входити')
    w3 = Wort('verlassen', 'покидати')
    w4 = Wort('Regel','правило','die')
    d.add_data(w)
    d.add_data(w2)
    d(w3)
    d(w4)
    d.get_random_data()
    print(d.show_random())
