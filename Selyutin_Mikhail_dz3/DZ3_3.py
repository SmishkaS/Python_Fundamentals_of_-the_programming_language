# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


# # Вариант 1
# def my_func(x, y, z):
#     numbers = [x, y, z]
#     res = sum(numbers) - min(numbers)
#     return res
#
#
# # print(my_func(int(input("Enter x = ")), int(input("Enter y = ")), int(input("Enter y = "))))
# print(f'{my_func(int(-2), int(3), int(5))}')


# Вариант 2
def my_func(x, y, z):
    if x >= z and y >= z:
        return x + y
    elif y < x < z:
        return x + z
    else:
        return y + z


# print(my_func(int(input("Enter x = ")), int(input("Enter y = ")), int(input("Enter z = "))))
print(f'{my_func(int(-2), int(3), int(5))}')
