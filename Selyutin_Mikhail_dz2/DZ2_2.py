# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# my_list = input("Введите элементы списка через пробел: ").split()
my_list = [1, 'a', 2, 'b', 3, 'c', 4, 'd', 5]

# Первый способ
for i in range(0, len(my_list) - 1, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

# Второй способ
# if len(my_list) % 2 == 0:
#     i = 0
#     while i < len(my_list):
#         el = my_list[i]
#         my_list[i] = my_list[i+1]
#         my_list[i+1] = el
#         i += 2
# else:
#     i = 0
#     while i < len(my_list) - 1:
#         el = my_list[i]
#         my_list[i] = my_list[i + 1]
#         my_list[i + 1] = el
#         i += 2
# print(my_list)
