# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

str_file = 'file_for_DZ5_1.txt'

with open(str_file, 'w', encoding='utf-8') as f:
    my_text = True
    while my_text:
        my_text = input("Enter any text or enter an empty string to complete\n: ")
        f.write(f'{my_text}\n')
