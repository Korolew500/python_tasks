import random


def print_matrix(matrix_list):
    answer = ''
    for i_str in matrix_list:
        for j_pos in i_str:
            answer += str(j_pos) + '\t'
        answer += '\n'
    return answer[:-2]


class Matrix:
    def __init__(self, height, weight):
        self.weight = weight
        self.data = [[random.randint(1, 10) for _ in range(weight)] for _ in range(height)]

    def add(self, matrix_2):
        return print_matrix([
            [
                self.data[j][i] + matrix_2.data[j][i]
                for i in range(len(self.data[j]))
            ]
            for j in range(len(self.data))
        ])

    def subtract(self, matrix_2):
        return print_matrix([
            [
                self.data[j][i] - matrix_2.data[j][i]
                for i in range(len(self.data[j]))
            ]
            for j in range(len(self.data))
        ])

    def multiply(self, matrix_2):
        m_2 = matrix_2.transpose_to_matrix()
        return print_matrix([
            [
                sum([self.data[i][j] * m_2[k][j] for j in range(len(self.data[i]))])
                for k in range(len(m_2))
            ]
            for i in range(len(self.data))
        ])

    def transpose(self):
        return print_matrix([
            [
                self.data[j][i] for j in range(len(self.data))
            ]
            for i in range(len(self.data[0]))
        ])

    def transpose_to_matrix(self):
        return [
            [
                self.data[j][i] for j in range(len(self.data))
            ]
            for i in range(len(self.data[0]))
        ]

    def print(self):
        return print_matrix(self.data)


# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
# m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
# m2.data = [[7, 8, 9], [10, 11, 12]]

m3 = Matrix(3, 2)
# m3.data = [[1, 2], [3, 4], [5, 6]]

# Тестирование операций
print("\nМатрица 1:")
print(m1.print())

print("\nМатрица 2:")
print(m2.print())

print("\nМатрица 3:")
print(m3.print())

print("\nСложение матриц 1 и 2:")
print(m1.add(m2))

print("\nВычитание матриц 1 и 2:")
print(m1.subtract(m2))

print("\nУмножение матриц 1 и 3:")
print(m1.multiply(m3))

print("\nТранспонирование матрицы 1:")
print(m1.transpose())
