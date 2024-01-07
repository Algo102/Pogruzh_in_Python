# Напишите функцию для транспонирования матрицы transposed_matrix,
# принимает в аргументы matrix, и возвращает транспонированную матрицу.
# Пример использования На входе:
matrix = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

# На выходе: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# def transposed_matrix(matrix):
#     # определяем количество строк и столбцов в матрице
#     rows = len(matrix)
#     cols = len(matrix[0])
#
#     # создаем новую матрицу с размерами, поменянными местами
#     transposed = [[0 for row in range(rows)] for col in range(cols)]
#
#     # заполняем новую матрицу значениями из старой матрицы
#     for row in range(rows):
#         for col in range(cols):
#             transposed[col][row] = matrix[row][col]
#
#     return transposed
#
# print(transposed_matrix(matrix))
#
# # Другое решение
# def transpose (matrix):
#     transposed_matrix = []
#     for j in range(len(matrix[0])):
#         row = []
#         for i in range(len(matrix)):
#             row.append(matrix[i][j])
#         transposed_matrix.append(row)
#     return transposed_matrix
#
# transposed_matrix = transpose(matrix)
# print(transposed_matrix)
#
#


def transpose(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    transposed_matrix = [[0 for _ in range(num_rows)] for _ in range(num_cols)]
    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix

transposed_matrix = transpose(matrix)
print(transposed_matrix)

