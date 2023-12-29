class Bank:
    def __init__(self, name, age, money, key):
        self._name = name
        self._age = age
        self.__money = money
        self.__key = key

    def set_name(self, name):...

    def get_name(self): ...


class Main(Bank):
    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_money(self, money):
        self._money = money

    def set_key(self, key):
        self._key = key


class Nemain(Main):
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def money(self):
        return self._money

    @property
    def key(self):
        return self._key

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

    @money.setter
    def money(self, money):
        self._money = money

    @key.setter
    def key(self, key):
        self.key = key

    def __str__(self):
        return f'{self.age}  {self.name} {self.money} {self.key}'
