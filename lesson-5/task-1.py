# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) 
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно 
# вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

import collections

data = collections.defaultdict(list)
'''data = {
    'ent1': [1, 2, 3, 4], 
    'ent2': [5, 6, 7, 8],
    'ent3': [5, 16, 17, 8],
}'''
while True:
    ent = input('Enter company name (or q for exit) ')
    if ent == 'q':
        break
    profit = [0]*4
    for i in range(4):
        profit[i] = int(input('Enter profit {} in {} quarter '.format(ent, i + 1)))
    print()
    data[ent] = profit

# print(data)
ent_total_profit = {}
avr_profit = 0
for ent in data:
    s = 0
    for q_profit in data[ent]:
        s += q_profit
    ent_total_profit[ent] = s
    avr_profit += s
avr_profit /= len(data)
# print(avr_profit)

above = []
below = []
for ent in ent_total_profit:
    if ent_total_profit[ent] > avr_profit:
        above.append(ent)
    else:
        below.append(ent)

print('above:')
for ent in above:
    print(ent)

print('below:')
for ent in below:
    print(ent)
