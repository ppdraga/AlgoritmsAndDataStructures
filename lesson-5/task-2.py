# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
# При этом каждое число представляется как массив, элементы которого — цифры числа. 
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] 
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


import collections

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

'''MULT16 = [
    ['0', '0',        '0',        '0',        '0',        '0',        '0',        '0',        '0',        '0',        '0',        '0',        '0',        '0',        '0',       '0'],
    ['0', '1',        '2',        '3',        '4',        '5',        '6',        '7',        '8',        '9',        'A',        'B',        'C',        'D',        'E',       'F'],
    ['0', '2',        '4',        '6',        '8',        'A',        'C',        'E', ['1', '0'], ['1', '2'], ['1', '4'], ['1', '6'], ['1', '8'], ['1', 'A'], ['1', 'C'], ['1', 'E']],
    ['0', '3',        '6',        '9',        'C',        'F', ['1', '2'], ['1', '5'], ['1', '8'], ['1', 'B'], ['1', 'E'], ['1', '8'], ['2', '4'], ['2', '7'], ['2', 'A'], ['2', 'D']],    
    ['0', '4',        '8',        'C', ['1', '0'], ['1', '4'], ['1', '8'], ['1', 'C'], ['2', '0'], ['2', '4'], ['2', '8'], ['2', 'C'], 
    ['0', '5',        'A',        'F', ['1', '4'], 
    ['0', '6',        'C', ['1', '2'],
    ['0', '7',        'E', ['1', '5'],
    ['0', '8', ['1', '0'], ['1', '8'],
    ['0', '9',
    ['0', 'A',
    ['0', 'B',
    ['0', 'C',
    ['0', 'D',
    ['0', 'E',
    ['0', 'F',
]'''


ALFANUM = collections.deque(
    ['0', '1', '2', '3', '4', 
     '5', '6', '7', '8', '9', 
     'A', 'B', 'C', 'D', 'E', 'F'], 16)
#ALFANUM.rotate(1) 

print(ALFANUM)     

ALFA2 = ['A', 'B', 'C', 'D', 'E', 'F']

def sum_x16(hex1, hex2):
    res = collections.deque()
    remainder = 0
    i = len(hex1)
    j = len(hex2)
    if (i > j):
        while(i > j):
            hex2.appendleft(ALFANUM[0])
            j += 1
    elif (i < j):
        while(i < j):
            hex1.appendleft(ALFANUM[0])
            i += 1
    i = i - 1
    while (i >= 0):
        rot = ALFA[hex1[i]] + ALFA[hex2[i]] + remainder
        ALFANUM.rotate(-rot)
        res.appendleft(ALFANUM[0])
        if rot > 15:
            remainder = 1
        else:
            remainder = 0
        ALFANUM.rotate(rot)
        i -= 1
    if remainder == 1:
        res.appendleft(ALFANUM[1])
    return res

def simple_mult_x16(hex1, hex2):
    res = collections.deque()
    digit = collections.deque(hex1)
    res.appendleft('0')
    i = ALFA[hex2]
    while(i > 0):
        res = sum_x16(res, digit)
        i -= 1
    return res
# print(simple_mult_x16('F', 'F'))

def semi_simple_mult_x16(multiplier, hex1):
    res = collections.deque()
    res.appendleft('0')
    i = len(hex1)
    j = 0
    while(i > 0):
        temp = simple_mult_x16(multiplier, hex1[i - 1])
        k = j
        while(k > 0):
            temp.append('0')
            k -= 1
        res = sum_x16(res, temp)
        i -= 1
        j += 1
    return res
#print(semi_simple_mult_x16('F', collections.deque(['1','2','3']))) # 110D

def mult_x16(hex1, hex2):
    res = collections.deque()
    res.appendleft('0')
    
    i = len(hex1)
    j = 0
    while (i > 0):
        temp = semi_simple_mult_x16(hex1[i - 1], hex2)
        k = j
        while(k > 0):
            temp.append('0')
            k -= 1
        res = sum_x16(res, temp)
        i -= 1
        j += 1
    return res
# t = mult_x16(collections.deque(['1','2','3']), collections.deque(['1','2','3']))
# print(t) # 110D

def toDecimal(hex):
    num = 0
    res = 0
    base = 1
    for letter in hex[::-1]:
        try:
            num = ALFA[letter]
        except KeyError:
            print('Errors!!!')
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
# hex1 = 'aabc'
# hex2 = 'f25'
hex1 = collections.deque(hex1.upper())
hex2 = collections.deque(hex2.upper())
print(hex1)
print(hex2)
# print(sum_x16(hex1, hex2))
# print(mult_x16(hex1, hex2))
sum_ = sum_x16(hex1, hex2)
mult_ = semi_simple_mult_x16(hex1, hex2)
print('Sum = ', sum_)
print('Mult = ', mult_)
