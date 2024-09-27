# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# month = int(input("Введите месяц цыфрами: "))
month = 9

# Первый способ
number = month // 3 % 4

if 12 >= number >= 1:
    season_dict = {0: 'winter', 1: 'spring', 2: 'summer', 3: 'autumn'}
    season_list = list(season_dict.values())

    print(f'For list: {month} month refers to {season_list[number]}')
    print(f'For dict: {month} month refers to {season_dict.get(number)}')
else:
    print('no such month')

# # Второй способ
# if 12 >= month >= 1:
#     season_dict = {1: 'winter',
#                    2: 'winter',
#                    3: 'spring',
#                    4: 'spring',
#                    5: 'spring',
#                    6: 'summer',
#                    7: 'summer',
#                    8: 'summer',
#                    9: 'autumn',
#                    10: 'autumn',
#                    11: 'autumn',
#                    12: 'winter'}
#     season_list = list(season_dict.values())
#     for i, el in enumerate(season_list):
#         if i == month - 1:
#             print(f'For list: {month} month refers to {season_list[i]}')
#             break
#     print(f'For dict: {month} month refers to {season_dict[month]}')
# else:
#     print('no such month')
