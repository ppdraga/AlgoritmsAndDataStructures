# 1) Определение количества различных подстрок с использованием хеш-функции. 
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:

# func("papa")
# 6

# Провести поиск подстроки в строке
import hashlib
import collections

def rabin_karp (s, t):
    len_sub = len(t)
    h_subs = hashlib.sha1(t.encode( 'utf-8' )).hexdigest()
    for i in range(len(s) - len_sub + 1 ):
        if h_subs == hashlib.sha1(s[i:i+len_sub].encode( 'utf-8' )).hexdigest():
            return i
    return -1


# string = 'sova'
string = input('Input string: ')

dict_ =  collections.defaultdict(int)

for i in range(len(string)):
    # print(f'i = {i}')
    for sub_len in range(1,len(string)-i+1):
        if sub_len == len(string):
            continue
        # print(f'sub_len = {sub_len}')
        # print(string[i:i+sub_len])
        sub_string = string[i:i+sub_len]
        if rabin_karp (string, sub_string) != -1:
            dict_[sub_string] += 1

print(len(dict_))

