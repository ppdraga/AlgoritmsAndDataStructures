# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое
# число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


ALFA = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}

ALFA2 = ['A', 'B', 'C', 'D', 'E', 'F']

def toDecimal(hex):
    num = 0
    res = 0
    base = 1
    for letter in hex[::-1]:
        try:
            num = ALFA[letter]
        except KeyError:
            print('Были введены некорректные данные')
            break
        res += num * base
        base *= 16
    return res

def toHex(num):
    res = []
    while num > 0:
        temp = num % 16
        num //= 16
        if temp < 10:
            res += str(temp)
        else:
            res += ALFA2[temp - 10]
    res = res[::-1]
    return res


hex1 = input('Первое 16-ричное число ')
hex2 = input('Второе 16-ричное число ')
hex1 = hex1.upper()
hex2 = hex2.upper()
sum_ = toHex(toDecimal(hex1) + toDecimal(hex2))
mult_ = toHex(toDecimal(hex1) * toDecimal(hex2))
print('Сумма чмсел равна ', sum_)
print('Произведение чмсел равно ', mult_)