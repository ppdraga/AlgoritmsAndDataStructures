# Написать два алгоритма нахождения i-го по счёту простого числа.
# ● Без использования Решета Эратосфена;
# ● Использовать алгоритм решето Эратосфена

from timeit import timeit
import cProfile

def notEratosthene(n):
    # n = input("n=")
    lst=[]
    for i in range(2, n+1):
        # пробегаем по списку (lst) простых чисел
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst[-1]


###################################### Решето Эратосфена ########################################
# n = int(input( "вывод простых чисел до числа ... " ))
def eratosthene(n):
    a = [0] * n # создание массива с n количеством элементов
    for i in range(n): # заполнение массива ...
        a[i] = i # значениями от 0 до n-1
    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0
    m = 2 # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n: # перебор всех элементов до заданного числа
        if a[m] != 0 : # если он не равен нулю, то
            j = m * 2 # увеличить в два раза (текущий элемент - простое число)
            while j < n:
                a[j] = 0 # заменить на 0
                j = j + m # перейти в позицию на m больше
        m += 1

    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0 :
            b.append(a[i])
    del a
    return b[-1]




if __name__ == "__main__":
    print(notEratosthene(1000))
    print(eratosthene(1000))

    # n = 1000
    # print(timeit('notEratosthene(1000)', number=100, globals=globals())) # 0.21615674502021381
    # print(timeit('eratosthene(1000)', number=100, globals=globals()))    # 0.10301124723122357

    # n = 10000
    # print(timeit('notEratosthene(10000)', number=100, globals=globals())) # 9.153166488341784
    # print(timeit('eratosthene(10000)', number=100, globals=globals()))    # 1.0322089748835417

    # cProfile.run('notEratosthene(10000)')
    #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #         1    0.092    0.092    0.092    0.092 task-2.py:8(notEratosthene)

    # cProfile.run('eratosthene(10000)')
    #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #         1    0.016    0.016    0.016    0.016 task-2.py:23(eratosthene)

    # Вывод eratosthene - показал себя эффективнее