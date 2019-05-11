# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4
# квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья
# прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего.

data = {}
# data = {'ent1': [1, 2, 3, 4], 'ent2': [5, 6, 7, 8]}
while True:
    ent = input('Введите название предприятия (или q для выхода) ')
    if ent == 'q':
        break
    profit = [0]*4
    for i in range(4):
        profit[i] = int(input(f'Введите прибыль {ent} за {i + 1} квартал '))
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

print('Предприятия с доходом выше среднего:')
for ent in above:
    print(ent)

print('Предприятия с доходом ниже среднего:')
for ent in below:
    print(ent)


