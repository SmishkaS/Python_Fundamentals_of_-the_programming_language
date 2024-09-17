# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def person_info(name, surname, birth, city, email, phone):
    res = f'{name}, {surname}, {birth}, {city}, {email}, {phone}'
    return res


print(person_info('Mikhail', 'Selyutin', 1987, 'Moscow', '7822733@mail.ru', 88007777777))
