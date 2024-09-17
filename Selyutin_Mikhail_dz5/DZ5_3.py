# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

str_file = 'file_for_DZ5_3.txt'

with open(str_file, 'r', encoding='utf-8') as f:
    surname = []
    poor = []
    my_list = f.read().split('\n')
    for line in my_list:
        line = line.split()
        if int(i[1]) < 20000:
            poor.append(line[0])
        surname.append(line[1])
print(f'poor employees {poor}\naverage salary {sum(map(int, surname)) / len(surname)}')
