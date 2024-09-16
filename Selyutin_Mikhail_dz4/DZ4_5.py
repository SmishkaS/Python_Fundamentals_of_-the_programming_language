# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce
from random import randrange

my_list = [randrange(100, 1001, 2) for i in range(10)]


def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, my_list))
