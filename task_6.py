"""
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
"""
from abc import ABC, abstractmethod
from random import choice
from string import ascii_uppercase, ascii_lowercase, digits


class Warehouse:
    def __init__(self, name):
        self.name = name
        self.__content = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def content(self):
        return self.__content

    @property
    def quantity(self):
        return len(self.__content)

    def add_item(self, item):
        self.__content.append(item)

    def delete_item(self, item_id):
        for index, item in enumerate(self.__content):
            if item_id == item.uniq_id:
                return self.__content.pop(index)


class Equipment(ABC):
    @staticmethod
    def id_generator(size=6):
        chars = ascii_uppercase + ascii_lowercase + digits
        return ''.join(choice(chars) for _ in range(size))

    @abstractmethod
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.uniq_id = f'{self.__class__.__name__}_{Equipment.id_generator()}'

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
        if not isinstance(value, (int, float)):
            raise ValueError('Price value type error')
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


wh1 = Warehouse('WH1')
wh2 = Warehouse('WH2')

eq = []
eq.append(Scanner(name='HP-Scan', price=190.0, resolution=720))
eq.append(Scanner(name='Pixma', price=140.0, resolution=640))
eq.append(Printer(name='CANON 12', price=234.0, performance=24))
eq.append(Printer(name='EPSON 890', price=345.0, performance=18))
eq.append(Printer(name='BROTHER 4T', price=468.0, performance=10))
eq.append(Copier(name='XEROX R5', price=745.0, color=False))

for item in eq:
    wh1.add_item(item)  # приход товара на склад

goods_id = wh1.content[2].uniq_id  # проверочный id

goods = wh1.delete_item(goods_id)  # перемещение товара со склада wh1
wh2.add_item(goods)  # на склад wh2

print(f'=> Склад {wh1.name}, всего товаров {wh1.quantity}')
for item in wh1.content:
    print(item)

print()

print(f'=> Склад {wh2.name}, всего товаров {wh2.quantity}')
for item in wh2.content:
    print(item)
