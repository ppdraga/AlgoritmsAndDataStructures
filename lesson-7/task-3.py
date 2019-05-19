# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите
# в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в
# одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то
# используйте метод сортировки, который не рассматривался на уроках.


import random

START = 0
END = 100
SIZE = 15

# def quickselect_median(l):
#     if len(l) % 2 == 1:
#         return quickselect(l, len(l) / 2)
#     else:
#         return 0.5 * (quickselect(l, len(l) / 2 - 1) + quickselect(l, len(l) / 2))


def quickselect(l, k):
    """
    Выбираем k-тый элемент в списке l 
    :param l: список числовых данных
    :param k: индекс
    :return: k-тый элемент l
    """
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = random.choice(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        # Нам повезло и мы угадали медиану
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

if __name__ == "__main__":
    array = [random.randint(START, END) for _ in range(SIZE)]
    print(array)
    print(f'median: {quickselect(array, SIZE // 2)}')

