"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix:
    def __init__(self, m):
        self.m = m
    
    def __str__(self):
        return f'{self.m}'

    def __add__(self, other):
        m_self, n_self = self.get_dimension()
        m_other, n_other = other.get_dimension()

        if m_self != m_other or n_self != n_other:
            print(f'Matrices have diferent dimensions {m_self}x{n_self} and {m_other}x{n_other}. Can\'t make add!')
            return None
        else:
            result = list()
            for i, el_i in enumerate(B):
                tmp = list()
                for j, el_j in enumerate(el_i):
                    tmp.append(el_j+A1[i][j])
                result.append(tmp)
            return Matrix(result)


    def get_dimension(self):
        return len(self.m), len(self.m[0])


A = [[31, 22], [37, 43], [51, 86]]
A1 = [[31, 22, 13], [37, 43, 12], [51, 86, 99]]
B = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
C = [[3, 5, 8, 3], [8, 3, 7, 1]]

m_A = Matrix(A)
m_A1 = Matrix(A1)
m_B = Matrix(B)
m_C = Matrix(C)

print(f'Matrix A: {m_A}')
print(f'Matrix B: {m_B}')
print(f'Matrix C: {m_C}')

print(f'Matrix D: {m_A1 + m_B}') 