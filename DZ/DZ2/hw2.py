# На вход автоматически подаются две строки frac1 и frac2 вида
# a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение
# дробей. Дроби упрощать не нужно.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

# # frac1 = input('Введите первую дробь: ')
# # frac2 = input('Введите вторую дробь: ')
# frac1 = '1/2'
# frac2 = '1/3'
#
# numerator_str1, denominator_str1 = frac1.split('/')
# numerator_str2, denominator_str2 = frac2.split('/')
#
# numerator_num1 = int(numerator_str1)
# numerator_num2 = int(numerator_str2)
# denominator_num1 = int(denominator_str1)
# denominator_num2 = int(denominator_str2)
#
# sum_numerator_num = (numerator_num1 * denominator_num2) + (numerator_num2 * denominator_num1)
# sum_denominator_num = denominator_num1 * denominator_num2
#
# mult_numerator_num = numerator_num1 * numerator_num2
# mult_denominator_num = denominator_num1 * denominator_num2
#
# print(f'Сумма дробей: {sum_numerator_num}/{sum_denominator_num}')
# print(f'Произведение дробей: {mult_numerator_num}/{mult_denominator_num}')
#
#
# # fract1 = Fraction(1, 2)
# # fract2 = Fraction(1, 3)
# fract1 = Fraction(frac1)
# fract2 = Fraction(frac2)
# print(f'Сумма дробей: {fract1 + fract2}')
# print(f'Произведение дробей: {fract1 * fract2}')


# Другое решение
frac1 = input('Введите первую дробь: ').split('/')
frac2 = input('Введите вторую дробь: ').split('/')

numerator_sum = int(frac1[0])*int(frac2[1]) + int(frac2[0])*int(frac1[1])
denominator_sum = int(frac1[1]) * int(frac2[1])
sum = [numerator_sum, denominator_sum]

numerator_mult = int(frac1[0]) * int(frac2[0])
denominator_mult = int(frac1[1]) * int(frac2[1])
mult = [numerator_mult, denominator_mult]

print(sum)
print(mult)
print(f'Сумма дробей: {numerator_sum}/{denominator_sum}')
print(f'Произведение дробей: {numerator_mult}/{denominator_mult}')


