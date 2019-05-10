# task-3
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
# Например, если введено число 3486, то надо вывести число 6843.

number = int(input('Введите число '))
new_numder = 0

while number > 0:
    current_num = number % 10
    number = number // 10
    new_numder = new_numder * 10 + current_num

print(new_numder)
