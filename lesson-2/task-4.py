# task-4
# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

count = int(input('Введите число элементов ряда '))
result = 0
current_elem = 1

while count > 0:
    result = result + current_elem
    current_elem = current_elem * (-1) * 0.5
    count -= 1

print(result)
