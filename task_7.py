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

    def __str__(self):
        sign = lambda s: '+' if s >= 0 else ''
        return f'{self.real}{sign(self.imaginary)}{self.imaginary}i'

d = Complex(3, -5)

print(d.real, d.imaginary)
print(d.complex)
print(d)