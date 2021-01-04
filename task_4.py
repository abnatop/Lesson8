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
    def __str__(self):
        return f'Сканер {self.name}, цена {self.price}, кол-во {self.count}'

class Printer(Equipment):
    def __str__(self):
        return f'Принтер {self.name}, цена {self.price}, кол-во {self.count}'

class Copier(Equipment):
    def __str__(self):
        return f'Копировальный аппарат {self.name}, цена {self.price}, кол-во {self.count}'


a = Scanner(name='HP-Scan', price=190.0, count=3)
b = Printer(name='CANON 12', price=234.0, count=2)
c = Copier(name='XEROX R5', price=745.0, count=5)

print(a)
print(b)
print(c)
