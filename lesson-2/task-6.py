# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать 
# не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться
# больше или меньше введенное пользователем число, чем то, что загадано. Если за 10 попыток 
# число не отгадано, то вывести загаданное число.
# task-6

import random

START_NUM   = 0
END_NUM     = 100
MAX_ATTEMPT = 10

secret = random.randint(START_NUM, END_NUM)
# print(secret)

attempt_count = 0
while attempt_count < MAX_ATTEMPT:
    attempt_count += 1
    num = int(input('Введите число '))
    if num == secret:
        print('Вы отгадали!')
        break
    elif num > secret:
        print('Введенное Вами число больше загаданного!')
    else:
        print('Введенное Вами число меньше загаданного!')
    if attempt_count == MAX_ATTEMPT:
        print('Вы не угадали, правильный ответ '+str(secret))
