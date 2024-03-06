# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

m = input('Введите трехзначное число: ')
n = int(m)
hundreds = n // 100
units = n % 10
tens = (n % 100) // 10
print(hundreds, tens, units)


#2
# units1 = m[2]
# tens1 = m[1]
# hundreds1 = m[0]
print(int(m[2]) + int(m[1]) + int(m[0]))

#3
res = 0
while n>0:
    res += n%10
    n //= 10
print(res)
