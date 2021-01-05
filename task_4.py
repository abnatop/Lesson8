"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""
from abc import ABC, abstractmethod
from random import choice
from string import ascii_uppercase, ascii_lowercase, digits


class Warehouse:
    pass


class Equipment(ABC):
    @staticmethod
    def id_generator(size=6):
        chars = ascii_uppercase + ascii_lowercase + digits
        return ''.join(choice(chars) for _ in range(size))

    @abstractmethod
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.uniq_id = Equipment.id_generator()

    @abstractmethod
    def __str__(self):
        pass

    @property
    def name(self): return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self): return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def uniq_id(self): return self.__uniq_id

    @uniq_id.setter
    def uniq_id(self, value):
        self.__uniq_id = value


class Scanner(Equipment):
    def __init__(self, name, price, resolution):
        super().__init__(name, price)
        self.resolution = resolution

    @property
    def resolution(self): return self.__resolution

    @resolution.setter
    def resolution(self, value):
        self.__resolution = value

    def __str__(self):
        return f'ID {self.uniq_id} - Сканер {self.name}, ' \
               f'цена {self.price}, разрешение {self.resolution}'


class Printer(Equipment):
    def __init__(self, name, price, performance):
        super().__init__(name, price)
        self.performance = performance

    @property
    def performance(self): return self.__performance

    @performance.setter
    def performance(self, value):
        self.__performance = value

    def __str__(self):
        return f'ID {self.uniq_id} - Принтер {self.name}, ' \
               f'цена {self.price}, стр/мин {self.performance}'


class Copier(Equipment):
    def __init__(self, name, price, color=False):
        super().__init__(name, price)
        self.color = color

    @property
    def color(self): return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def __str__(self):
        is_color = lambda i: 'YES' if i else 'NO'
        return f'ID {self.uniq_id} - Копировальный аппарат {self.name}, ' \
               f'цена {self.price}, цветной {is_color(self.color)}'


eq = []
eq.append(Scanner(name='HP-Scan', price=190.0, resolution=720))
eq.append(Printer(name='CANON 12', price=234.0, performance=24))
eq.append(Copier(name='XEROX R5', price=745.0, color=False))

for item in eq:
    print(item)
