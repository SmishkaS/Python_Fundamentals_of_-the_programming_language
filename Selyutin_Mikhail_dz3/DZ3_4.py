# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


# Первая часть
def my_func(x, y):
    return 1 / x ** abs(y)


# print(my_func(int(input("Enter x = ")), int(input("Enter y = "))))
print(my_func(2, -3))


# Вторая часть
def my_func(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res


# print(my_func(int(input("Enter x = ")), int(input("Enter y = "))))
print(my_func(2, -3))


