"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""
from abc import ABC, abstractmethod


class Warehouse:
    pass


class Equipment(ABC):
    @abstractmethod
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

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
    def count(self): return self.__count

    @count.setter
    def count(self, value):
        self.__count = value


class Scanner(Equipment):
    def __init__(self, name, price, count, resolution):
        super().__init__(name, price, count)
        self.resolution = resolution

    @property
    def resolution(self): return self.__resolution

    @resolution.setter
    def resolution(self, value):
        self.__resolution = value

    def __str__(self):
        return f'Сканер {self.name}, цена {self.price}, ' \
               f'кол-во {self.count}, разрешение {self.resolution}'


class Printer(Equipment):
    def __init__(self, name, price, count, performance):
        super().__init__(name, price, count)
        self.performance = performance

    @property
    def performance(self): return self.__performance

    @performance.setter
    def performance(self, value):
        self.__performance = value

    def __str__(self):
        return f'Принтер {self.name}, цена {self.price}, кол-во {self.count}, стр/мин {self.performance}'


class Copier(Equipment):
    def __init__(self, name, price, count, color=False):
        super().__init__(name, price, count)
        self.color = color

    @property
    def color(self): return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def __str__(self):
        is_color = lambda i: 'YES' if i else 'NO'
        return f'Копировальный аппарат {self.name}, цена {self.price}, ' \
               f'кол-во {self.count}, цветной {is_color(self.color)}'


eq = []
eq.append(Scanner(name='HP-Scan', price=190.0, count=3, resolution=720))
eq.append(Printer(name='CANON 12', price=234.0, count=2, performance=24))
eq.append(Copier(name='XEROX R5', price=745.0, count=5, color=False))

for item in eq:
    print(item)
