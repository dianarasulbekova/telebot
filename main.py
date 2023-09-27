class MBank:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.__cash = 0
        self.__gold = False

    def __verification(self):
        self.__gold = True

    def get__cash(self):
        return f'Balance {self.__cash} som'

    def set__cash(self, x):
        self.__cash = self.__cash + x

    def info(self):
        return f'Name:{self.name}\nSurname:{self.surname}'

    def shopping(self):
        pass


online = MBank('Sanjar', 'Ayazov')
print(online.info())
print(online.get__cash())
online.set__cash(10000)
print(online.get__cash())

