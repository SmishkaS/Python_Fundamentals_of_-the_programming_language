# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
# Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, array):
        self.matrix = array
        self._size = None

    @property
    def size(self):
        if self._size is None:
            self._size = (len(self.matrix), len(self.matrix[0]))
        return self._size

    def __str__(self):
        tmp = '\n'.join(str(row) for row in self.matrix)
        return ''.join(el.strip(',[]') for el in tmp)

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError(f'Wrong type: {type(other)}')
        if not self.size == other.size:
            raise ValueError('Array are not equal.')

        result = [
            [a + b for a, b in zip(row1, row2)]
            for row1, row2 in zip(self.matrix, other.matrix)
        ]
        return Matrix(result)


matrix1 = Matrix([[5, 18, 11],
                  [6, 17, 23],
                  [41, 50, 9]])
matrix2 = Matrix([[45, 8, 2],
                  [6, 7, 93],
                  [24, 5, 97]])
matrix3 = Matrix([[4, 10, 9],
                  [6, 17, 23],
                  [41, 50, 9]])

print(matrix1 + matrix2 + matrix3)
