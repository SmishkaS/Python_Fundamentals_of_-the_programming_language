# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

str_file = 'file_for_DZ5_5.txt'
set_of_num = []

with open(str_file, 'w', encoding='utf-8') as f:
    for i in (randint(0, 100) for i in range(10)):
        f.write(f"{i} ")
        set_of_num.append(i)

print(f'summa {sum(set_of_num)}')
