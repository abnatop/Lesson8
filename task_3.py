"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел. Проверить работу исключения на реальном примере. Необходимо
запрашивать у пользователя данные и заполнять список только числами. Класс-исключение
должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
пользователь сам не остановит работу скрипта, введя, например, команду “stop”. При этом
скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и
строки. При вводе пользователем очередного элемента необходимо реализовать проверку
типа элемента и вносить его в список, только если введено число. Класс-исключение должен
не позволить пользователю ввести текст (не число) и отобразить соответствующее
сообщение. При этом работа скрипта не должна завершаться.
"""
EXIT = 'stop'

class ListContentError(Exception):
    @classmethod
    def value_check(cls, value):
        try:
            if not value.isdigit():
                raise ListContentError(f'Value {value} is not digit')
        except ListContentError as err:
            print(err)
            return True


digits = []
while True:
    value = input(f'Input digit: ')
    if value == EXIT:
        break

    if not ListContentError.value_check(value):
        digits.append(value)

print(digits)


# try:
#     a = int(a)
#     if a < 0:
#         raise ListContentError("You give negative!", a)
# except ValueError:
#     print("Error type of value!")
# except ListContentError as err:
#     print(f'Message: {err.args[0]}, args: {err.args[1]}')
# else:
#     print(f'Positive {a}')
# finally:
#     print(f'Finally this is a {a}')

