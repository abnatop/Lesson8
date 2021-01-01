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
        self.data_value = data_value

    def to_digital(self):
        data = self.data_value.split('-')
        day = int(data[0])
        month = int(data[1])
        year = int(data[2])
        return day, month, year

    def validate(self):
        if not isinstance(self.data_value, str):
            print('NOT valid type (str)')
        regex = r"\d{1,2}-\d{1,2}-\d{2,4}"
        match = re.fullmatch(regex, self.data_value)
        return True if match else False


dd = Data('10-20-3030')
print(dd.validate())