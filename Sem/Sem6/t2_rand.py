from random import randint as rnd
from sys import argv

__all__ = ['serch_num', 'params']

def serch_num(low: int=1, up: int=10, count: int=3): # по умолчанию, если введут меньше чисел
    num = rnd(low, up)
    while count:
        num_us = int(input('Введи ваш вариант числа: '))
        if num_us < num:
            print("Загаданное число больше")
        elif num_us > num:
            print("Загаданное число меньше")
        else:
            print("Вы угадали")
            return True
        count -= 1
    print('Увы, Искомое число', num)
    return False



params = list(map(int, argv[1:])) # Отрезали наименование файла, т.к. argv начинает с него


if __name__ == '__main__': # чтоб не запускался при вызове модуля
    print(serch_num(1, 10, 3))

