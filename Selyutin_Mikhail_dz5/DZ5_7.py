# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме
# : название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

str_file = 'file_for_DZ5_7.txt'
firm_dict = {}

with open(str_file, 'r', encoding='utf-8') as f:
    for line in f:
        firm_list = line.split()
        firm_name = firm_list[0]
        firm_gain = int(firm_list[2])
        firm_loss = int(firm_list[3])
        firm_dict[firm_name] = firm_gain - firm_loss

    profit_dict = {}
    profit = 0
    count = 0
    for val in firm_dict.values():
        if val >= 0:
            profit += val
            count += 1
    av_profit = profit / count
    profit_dict['average_profit'] = av_profit

    final_list = [firm_dict, profit_dict]
    print(firm_list)

with open('file_for_DZ5_7.json', 'w', encoding='utf-8') as f:
    json.dump(firm_list, f)
