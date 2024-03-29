# Напишите программу, которая выводит на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

#  Просто список с числами от 1 до 100
# my_list = [i for i in range(1, 101)]
# print(*my_gen)

# Мое решение
new = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        new.append('FizzBuzz')
    elif i % 3 == 0:
        new.append('Fizz')
    elif i % 5 == 0:
        new.append('Buzz')
    else:
        new.append(i)
print(new)


res=('FizzBuzz' if i % 3 == i % 5 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range(1, 101))
print(*res)

# решение семинара
# for i in range(1, 101):
#     res = ''
#     if i % 3 == 0:
#         res += 'Fizz'
#     if i % 5 == 0:
#         res += 'Buzz'
#     print(i if res=='' else res)


# Короткие решения
# result = ('FizzBuzz' if i % 3 == 0 and i % 5 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range(1, 101))
# print(*result)
#
# result1 = ('FizzBuzz' if i % 3 == i % 5 == 0 else 'Buzz' if i % 5 == 0 else 'Fizz' if i % 3 == 0 else i for i in range(1, 101))
# print(list(result1))
#
# output = ['FizzBuzz' if i % 3 == 0 and i % 5 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range(1, 101)]
# print(output)



