# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из
# чисел в диапазоне от 2 до 9.

array = list(range(2,100))
result = [0]*8
# print(array)
# print(result)
for i in range(2,10):
    for num in array:
        if num % i == 0:
            result[i-2] += 1
    print(f'{i} - {result[i-2]}')

