# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу
# : длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500

class Road:
    __length = None
    __width = None
    weight = None
    thickness = None

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def mass(self):
        self.weight = 25
        self.thickness = 0.05
        mass = self.length * self.width * self.weight * self.thickness
        print(f'Для покрытия дорожного полотна необходимого {mass} тон асфальта')


road_surface = Road(20, 5000)
road_surface.mass()
