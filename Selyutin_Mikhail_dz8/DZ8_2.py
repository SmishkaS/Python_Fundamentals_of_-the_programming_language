# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class Division_by_null:
    def __init__(self, number, divider):
        self.number = number
        self.denominator = divider

    @staticmethod
    def divide_by_null(number, divider):
        try:
            return number / divider
        except:
            return f'Деление на ноль недопустимо'


div = Division_by_null(10, 10)
print(Division_by_null.divide_by_null(10, 0))
print('Не завершиться с ошибкой')
