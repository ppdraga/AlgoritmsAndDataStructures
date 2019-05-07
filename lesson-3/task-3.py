# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный
# элементы.

import random

array = [random.randint(1, 100) for _ in range(10)]
result = []
print(array)
min_elem = {'position': 0, 'value': array[0]}
max_elem = {'position': 0, 'value': array[0]}

for i, elem in enumerate(array):
    if elem > max_elem['value']:
        max_elem['value'] = elem
        max_elem['position'] = i
    if elem < min_elem['value']:
        min_elem['value'] = elem
        min_elem['position'] = i
        
if max_elem['position'] != min_elem['position']:        
    array[max_elem['position']], array[min_elem['position']] = array[min_elem['position']], array[max_elem['position']]
# print(min_elem)
# print(max_elem)
print(array)






