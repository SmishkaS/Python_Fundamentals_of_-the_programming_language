# 6. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
"""
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
list_of_tuples = []
while input('Want to add a description for a new item? Enter yes/no: ') == 'yes':
    item = int(input('Enter the item number: '))
    tuples_of_dict = dict({'name': input("Enter name: "),
                           'price': input("Enter price: "),
                           'quantity': input("Enter quantity: "),
                           'units': input("Enter units: ")
                           })
    list_of_tuples.append((item, tuples_of_dict))

print(*list_of_tuples, sep='\n')

# list_of_tuples = [(1, {'name': 'computer', 'price': '20000', 'quantity': '5', 'units': 'pcs'}),
#                   (2, {'name': 'printer', 'price': '6000', 'quantity': '2', 'units': 'pcs'}),
#                   (3, {'name': 'scanner', 'price': '2000', 'quantity': '7', 'units': 'pcs'})]

list_analytic = {}
for characteristic in list_of_tuples:
    for number_key, list_value in characteristic[1].items():
        if number_key in list_analytic:
            list_analytic[number_key].append(list_value)
        else:
            list_analytic[number_key] = [list_value]

print(*list_analytic.values(), sep='\n')
