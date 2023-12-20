# Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

HEX_IND = '0123456789ABCDEF'
num = int(input('Введите целое число: '))
base = int(input('Система исчисления: '))
orig = num
res = ''

while num > 0:
    res = HEX_IND[num % base] + res
    num //= base

print(f'Число {orig} в {base}-чной системе будет {res}')
print('Проверка результата: ', hex(orig))


# print(hex(orig)[2:])
# print(oct(orig)[2:])
# print(bin(orig)[2:])



# не доделанная функция, без перевода букв
# def tobase(num: int, base: int):
#     res = ''
#     while num > 0:
#         res = str(num % base) + res
#         num //= base
#     return res
#
# print(tobase(num, 16))
# print(hex(num))



# еще решение
# num = 255
# base = 16
# HEX_IND = "0123456789ABCDEF"
#
# res = ""
# test_hex_num = hex(num)
#
# while num > 0:
#     ind = num % base
#     res = HEX_IND[ind] + res
#     num //= base
#
# print("Шестнадцатеричное представление числа:", res)
# print("Проверка результата:", test_hex_num)

