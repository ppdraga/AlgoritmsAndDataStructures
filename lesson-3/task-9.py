# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]
for line in matrix:
    print(line)

arr_min = matrix[0].copy()
rows = matrix.__len__()
columns = matrix[0].__len__()

for col in range(columns):
    for row in range(rows):
        if matrix[row][col] < arr_min[col]:
            arr_min[col] = matrix[row][col]
print('Массив минимальных:')
print(arr_min)

result = arr_min[0]
for i in range(1, col + 1):
    if arr_min[i] > result:
        result = arr_min[i]
print(f'максимальный элемент среди минимальных равен {result}')