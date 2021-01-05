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


def id_generator(size=4):
    chars = ascii_uppercase + ascii_lowercase + digits
    return ''.join(choice(chars) for _ in range(size))


class Warehouse:
    pass


class Equipment(ABC):
    @abstractmethod
    def __init__(self, name, price, uniq_id):
        self.name = name
        self.price = price
        self.uniq_id = uniq_id

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
    def __init__(self, name, price, uniq_id, resolution):
        super().__init__(name, price, uniq_id)
        self.resolution = resolution

    @property
    def resolution(self): return self.__resolution

    @resolution.setter
    def resolution(self, value):
        self.__resolution = value

    def __str__(self):
        return f'Сканер {self.name}, цена {self.price}, ' \
               f'кол-во {self.uniq_id}, разрешение {self.resolution}'


class Printer(Equipment):
    def __init__(self, name, price, uniq_id, performance):
        super().__init__(name, price, uniq_id)
        self.performance = performance

    @property
    def performance(self): return self.__performance

    @performance.setter
    def performance(self, value):
        self.__performance = value

    def __str__(self):
        return f'Принтер {self.name}, цена {self.price}, кол-во {self.uniq_id}, стр/мин {self.performance}'


class Copier(Equipment):
    def __init__(self, name, price, uniq_id, color=False):
        super().__init__(name, price, uniq_id)
        self.color = color

    @property
    def color(self): return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def __str__(self):
        is_color = lambda i: 'YES' if i else 'NO'
        return f'Копировальный аппарат {self.name}, цена {self.price}, ' \
               f'кол-во {self.uniq_id}, цветной {is_color(self.color)}'


eq = []
eq.append(Scanner(name='HP-Scan', price=190.0, uniq_id=3, resolution=720))
eq.append(Printer(name='CANON 12', price=234.0, uniq_id=2, performance=24))
eq.append(Copier(name='XEROX R5', price=745.0, uniq_id=5, color=False))

for item in eq:
    print(item)
