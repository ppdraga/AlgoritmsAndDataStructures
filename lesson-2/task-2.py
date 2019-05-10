# task-2
# Посчитать четные и нечетные цифры введенного натурального числа. 
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = int(input('Введите число '))
even_nums = 0
odd_nums  = 0

while number > 0:
    current_num = number % 10
    number = number // 10
    if current_num % 2 == 0:
        even_nums += 1
    else:
        odd_nums += 1

print('Четных цыфр в числе ' + str(even_nums) + ', нечетных ' + str(odd_nums))

#print(f"Четных цыфр в числе {even_nums} нечетных {odd_nums}.")

