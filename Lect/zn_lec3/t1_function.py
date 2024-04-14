# 1 Нет различия функции или процедуры, в Питоне все функции
# 2 Пишется без типа данных
# 3 Сколько элементов передаем, столько и принимаем и наоборот
# если только не передали в аргумент значение по умолчанию, на вывод можно передать другое значение
# 4 После ретурна функция прекращает работу

# программа суммирует числа от 1 до N


def sum_numbers1(n):
    summ = 0
    for i in range(1, n + 1):
        summ += i
    print(summ)


sum_numbers1(5)
# ИЛИ ТАК
n = int(input())
sum_numbers1(n)


# ИЛИ ТАК
def sum_numbers2(n, y='hello'):
    print(y)
    summ = 0
    for i in range(1, n + 1):
        summ += i
    return summ


print(sum_numbers2(5, 'qwert'))
# ИЛИ ТАК
a = sum_numbers2(5)
print(a)


# Для передачи, неопределенного количества аргументов, используем *


def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res


print(sum_str('q', 'e', 'l'))
print(sum_str('q', 'e', 'l', 'r', 't'))


# Вызываем функцию из файла
import modul1  # Импортируем модуль
import modul1 as m1
from modul1 import *  # Чтоб импортировать все функции из модуль1 нужно поставить *
from modul1 import max1


print(modul1.max1(5, 9)) # Вызываем и сразу печатаем
# ИЛИ
print(max1(5, 9))


# Чтоб каждый раз не писать длинное имя функции модуль1 можно сократить имя модудя для вызова в программе
print(m1.max1(5, 9))
