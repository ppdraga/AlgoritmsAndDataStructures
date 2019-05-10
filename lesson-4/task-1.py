# Проанализировать скорость и сложность одного любого алгоритма, разработанных в
# рамках практического задания первых трех уроков.

# Определить, какое число в массиве встречается чаще всего.

import random
from timeit import timeit
import cProfile

# SIZE = 100
# array = [random.randint(1, SIZE // 1.5) for _ in range(SIZE)]
# print(array)

def findElem1(size):
    array = [random.randint(1, size // 1.5) for _ in range(size)]
    unique_elems = list(set(array))
    max_appearances = 1
    result = unique_elems[0]

    for unique_num in unique_elems:
        appearances = 0
        for num in array:
            if num == unique_num:
                appearances += 1
        if appearances > max_appearances:
            result = unique_num
            max_appearances = appearances
    if max_appearances > 1:
        return result
    return False

def findElem2(size):
    array = [random.randint(1, size // 1.5) for _ in range(size)]
    counter = {}
    frequency = 1
    num = None
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
        if counter[item] > frequency:
            frequency = counter[item]
            num = item

    if num is not None:
        return num
    return False

def findElem3(size):
    array = [random.randint(1, size // 1.5) for _ in range(size)]
    frequency = 1
    num = array[0]
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]

    if frequency > 1:
        return num
    return False

if __name__ == "__main__":
    # n = 100
    # print(timeit('findElem1(100)', number=100, globals=globals())) # 0.13184189548046704
    # print(timeit('findElem2(100)', number=100, globals=globals())) # 0.0758340243878424
    # print(timeit('findElem3(100)', number=100, globals=globals())) # 0.16016090812220612
   

    # n = 1000
    # print(timeit('findElem1(1000)', number=100, globals=globals())) # 5.42140175757589
    # print(timeit('findElem2(1000)', number=100, globals=globals())) # 0.7145762541271816
    # print(timeit('findElem3(1000)', number=100, globals=globals())) # 9.570602067109961

    # cProfile.run('findElem1(1000)')
    #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #         1    0.047    0.047    0.063    0.063 task-1.py:14(findElem1)

    # cProfile.run('findElem2(1000)')
    #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #         1    0.001    0.001    0.014    0.014 task-1.py:32(findElem2)

    # cProfile.run('findElem3(1000)')
    #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #         1    0.096    0.096    0.104    0.104 task-1.py:50(findElem3)

    # Вывод findElem2 - самый эффективный