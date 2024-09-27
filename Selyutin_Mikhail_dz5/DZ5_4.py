# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

str_file = 'first_file_for_DZ5_4.txt'
rus_dict = {'One': 'Один',
            'Two': 'Два',
            'Three': 'Три',
            'Four': 'Четыре'
}
new_file = []

with open(str_file, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.split(' ', 1)
        new_file.append(rus_dict[i[0]] + ' ' + i[1])
    print(new_file)

with open('new_file_for_DZ5_4.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)
