#Задание 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

def fin_salary():
    try:
        time = float(input('Укажите выработку сотрудника по часам: '))
        salary = float(input('Укажите ставку в у.е.: '))
        bonus = float(input('Укажите премию в у.е.: '))
        wage = time * salary + bonus
        print(f'Заработная плата сотрудника составляет {wage}')
    except ValueError:
        return print('Не числовое выражение!')


fin_salary()


#Задание 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.


number_line = [2, 9, 5, 5, 8, 10, 1]
new_line = [el for number, el in enumerate(number_line) if number_line[number - 1] < number_line[number]]
print(f'Исходный список: {number_line}')
print(f'Итоговый список: {new_line}')


#Задание 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.


print(f'В последовательности от 20 до 240 числа, кратные 20 и 21: {[i for i in range(20, 240, 1) if i % 20 == 0 or i % 21 == 0]}')


#Задание 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.


my_list = [2, 5, 5, 34, 1, 1, 98, 20, 11, 1, 23, 34]
my_new_list = [i for i in my_list if my_list.count(i) < 2]
print(my_new_list)


#Задание 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def my_func(el1, el2):
    return el1 * el2


print(f'Четные элементы списка: {[i for i in range(100, 1001) if i % 2 == 0]}')
print(f'Результат умножения элементов списка: {reduce(my_func,[i for i in range(100, 1000) if i % 2 == 0])}')


#Задание 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.


from itertools import count, cycle
count1 = 1
for el in count(int(input('Введите число для старта: '))):
    if count1 > 10:
        break
    print(el)
    count1 += 1


count2 = 1
my_line = [1, 2, 3, 4, 5]
for i in cycle(my_line):
    if count2 > 3:
        break
    print(my_line)
    count2 += 1


#Задание 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
#
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.


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
