# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и 
# заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" 
# в каждой строке.
# task-5

START_NUM = 32
END_NUM   = 127

i = START_NUM
while i <= END_NUM:
    row = ''
    for _ in range(10):
        row = row + ' '+str(i)+' - '+chr(i)
        i += 1
        if i > END_NUM:
            break
    print(row)

