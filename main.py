from itertools import count
from math import factorial

n = int(input('Введите число: '))


def fact():
    for item in count(1, 1):
        if item > n:
            break
        yield print(int(factorial(item)))


x = 0
for el in fact():
    if x < n-1:
        print(el)
        x += 1
    else:
        break
