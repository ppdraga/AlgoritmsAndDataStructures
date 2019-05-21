# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. 
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.



# Проанализировать скорость и сложность одного любого алгоритма, разработанных в
# рамках практического задания первых трех уроков.

# Определить, какое число в массиве встречается чаще всего.

import random
import sys
memory = 0
SIZE = 500
array = [random.randint(1, SIZE // 1.5) for _ in range(SIZE)]
print(array)
memory += sys.getsizeof(array) + sys.getsizeof(SIZE)


def findElem1(array):
    # array = [random.randint(1, size // 1.5) for _ in range(size)]
    mem = 0
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
        mem += sys.getsizeof(unique_elems) + sys.getsizeof(max_appearances) + sys.getsizeof(appearances) + sys.getsizeof(result) + sys.getsizeof(unique_num) + sys.getsizeof(num)
        print(f'findElem1 - {mem + memory}')
        return result
    return False


def findElem2(array):
    # array = [random.randint(1, size // 1.5) for _ in range(size)]
    counter = {}
    frequency = 1
    num = None
    mem = 0
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
        if counter[item] > frequency:
            frequency = counter[item]
            num = item

    if num is not None:
        mem += sys.getsizeof(counter) + sys.getsizeof(frequency) + sys.getsizeof(item) + sys.getsizeof(num)
        print(f'findElem2 - {mem + memory}')
        return num
    return False


def findElem3(array):
    # array = [random.randint(1, size // 1.5) for _ in range(size)]
    mem = 0
    frequency = 1
    num = array[0]
    range_ = range(len(array))
    mem += sys.getsizeof(range_)
    for i in range_:
        spam = 1
        range_2 = range(i + 1, len(array))
        mem += sys.getsizeof(range_2)
        for j in range_2:
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]

    if frequency > 1:
        mem += sys.getsizeof(spam) + sys.getsizeof(frequency) + sys.getsizeof(num)
        print(f'findElem3 - {mem + memory}')
        return num
    return False

if __name__ == "__main__":
    
    print(findElem1(array)) # findElem1 - 6888
    print(findElem2(array)) # findElem2 - 13704
    print(findElem3(array)) # findElem3 - 28432

    # Вывод findElem1 - самый эффективный