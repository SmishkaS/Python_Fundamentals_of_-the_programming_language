# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def my_func(x, y):
    try:
        res = x / y
    except ZeroDivisionError:
        return '"y" is not be a zero'
    return res


# print(my_func(int(input("Enter x = ")), int(input("Enter y = "))))
print(my_func(int(4), int(0)))
