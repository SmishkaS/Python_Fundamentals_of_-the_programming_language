# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий
# название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

# Вариант 1 (через setdefault)
# def to_float(el):
#     try:
#         return float(el)
#     except:
#         return 0
#
#
# def my_func(elem):
#     if elem == '-':
#         return 0
#     else:
#         num = elem.split('(')[0]
#         return to_float(num)
#
#
# str_file = 'file_for_DZ5_6.txt'
# subj = {}
#
# with open(str_file, 'r', encoding='utf-8') as f:
#     for line in f:
#         subject, *my_line_list = line.split()
#         my_list = [my_func(el) for el in my_line_list]
#         hours = sum(my_list)
#         subj.setdefault(subject, hours)
#     print(f'Общее количество часов по предмету - \n {subj}')


# Вариант 2 (через sum)
# def to_float(el):
#     try:
#         return float(el)
#     except:
#         return 0
#
#
# def my_func(elem):
#     if elem == '-':
#         return 0
#     else:
#         num = elem.split('(')[0]
#         return to_float(num)
#
#
# str_file = 'file_for_DZ5_6.txt'
# subj = {}
#
# with open(str_file, 'r', encoding='utf-8') as f:
#     for line in f:
#         subject, my_line_list = line.split(':')
#         subj[subject] = sum([float(itm.split('(')[0]) for itm in my_line_list.split(" ") if itm.split('(')[0].isdigit()])
# print(f'Общее количество часов по предмету - \n {subj}')


# Вариант 3 (через sum map)
def get_nums(itm: str) -> float:
    try:
        return float(itm.split('(')[0])
    except ValueError:
        return 0


str_file = 'file_for_DZ5_6.txt'
subj = {}

with open(str_file, 'r', encoding='utf-8') as f:
    for line in f:
        subject, my_line_list = line.split(':')
        subj[subject] = sum(map(get_nums, my_line_list.split()))

print(f'Общее количество часов по предмету - \n {subj}')
