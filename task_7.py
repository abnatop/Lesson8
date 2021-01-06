"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата.
"""


class Complex:
    def __init__(self, real, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    @property
    def complex(self):
        return self.real, self.imaginary

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        self.__real = value

    @property
    def imaginary(self):
        return self.__imaginary

    @imaginary.setter
    def imaginary(self, value):
        self.__imaginary = value

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return Complex(real, imaginary)

    def __mul__(self, other):
        a1, a2 = self.real, self.imaginary
        b1, b2 = other.real, other.imaginary
        real, imaginary = a1 * b1 - a2 * b2, a1 * b2 + a2 * b1
        return Complex(real, imaginary)

    def __str__(self):
        sign = lambda s: '+' if s >= 0 else ''
        return f'{self.real}{sign(self.imaginary)}{self.imaginary}i'


d = Complex(1, -1)
g = Complex(3, 6)

print(d + g)
print(d * g)
