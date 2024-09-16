# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name = None
    surname = None
    position = None
    income = None

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income

    def naming(self):
        print(self.income)


class Position(Worker):
    def get_full_name(self):
        return f"Имя, Фамилия сотрудника: {self.name} {self.surname}"

    def get_total_income(self):
        return f"Доход сотрудника с учетом премии: {sum(self.income.values())}"


my_dict = {"wage": 200000, "bonus": 50000}
employee = Position("Михаил", "Селютин", "IT_Guru", my_dict)

print(employee.get_full_name())
print(employee.get_total_income())
