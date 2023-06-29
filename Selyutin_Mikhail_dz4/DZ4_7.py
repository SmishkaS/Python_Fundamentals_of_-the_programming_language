# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

# Вариант 1:
# def factorial(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1
#
#
# number = 5
# sequence = 1
# for el in factorial(number):
#     sequence *= el
#     print(sequence)


# Вариант 2 (исправленный):
def factorial(n):
    count = 1
    for i in range(1, n + 1):
        count *= i
        yield count


number = 5
for el in factorial(number):
    print(el)
