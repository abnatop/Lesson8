"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
"""
import re


class Data:
    def __init__(self, data_value):
        if Data.validate(data_value):
            self.data_value = data_value

    @classmethod
    def to_digital(cls, data_value):
        return Data._get_digital(data_value)

    @staticmethod
    def _get_digital(data_value):
        data = data_value.split('-')
        day = int(data[0])
        month = int(data[1])
        year = int(data[2])
        return day, month, year

    @staticmethod
    def check_date(data_value):
        check = Data._get_digital(data_value)
        if check[0] not in range(1, 32):
            raise ValueError('Неверное кол-во дней')
        if check[1] not in range(1, 13):
            raise ValueError('Неверное кол-во месяцев')
        return True

    @staticmethod
    def validate(data_value):
        if not isinstance(data_value, str):
            raise ValueError(f'Неверный тип данных {type(data_value)}')
        regex = r"\d{1,2}-\d{1,2}-\d{2,4}"
        if not re.fullmatch(regex, data_value):
            raise ValueError('Неверный формат данных DD-MM-YYYY')
        if not Data.check_date(data_value):
            raise ValueError('Неверные данные в дате')
        return True


sample = '31-12-3030'
obj = Data(sample)

if Data.validate(sample):
    print(Data.to_digital(sample))
else:
    raise ValueError('Неверный тип данных')
