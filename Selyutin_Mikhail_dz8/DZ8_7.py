# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, num1, num2, *args):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        return f'Сумма = {self.num1 + other.num1} + {self.num2 + other.num2} * i'

    def __mul__(self, other):
        return f'Произведение = {self.num1 * other.num1 - (self.num2 * other.num2)} + {self.num2 * other.num1} * i'

    def __str__(self):
        return f' {self.num1} + {self.num2} * i'


numbers_1 = ComplexNumber(1, -2)
numbers_2 = ComplexNumber(3, 4)
print(numbers_1)
print(numbers_2)
print(numbers_1 + numbers_2)
print(numbers_1 * numbers_2)
