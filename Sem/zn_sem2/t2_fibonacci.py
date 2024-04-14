# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6
# 0 1 1 2 3 5 8 13 21 34 55 89

n = int(input("Введите число Фибоначчи: "))
fib1, fib2 = 1, 1
count = 1
temp = 1
while fib2 < n:
    # if count == 1:
    #     print(count, 0)
    # elif count == 2:
    #     print(count, 1)
    if count > 2:
        # print(count, temp)

        # temp = fib1 + fib2
        # fib1 = fib2
        # fib2 = temp
        # множественное присваивание, не требуется буфер
        fib1, fib2 = fib2, fib1 + fib2

    count += 1
    if fib2 == n:
        print(f'Число {n} находится {count}-ым в ряду')
        break
else:
    print("Число не принадлежит ряду Фибоначчи")

# Другое решение
# num = int(input("Введите число, проверим, принадлежит ли оно ряду Фибоначи : "))
# i = 0
# f1 = 1
# f2 = 1
# while i < 999:
#     if i == 0:
#         f1 = 0
#         f2 = 0
#     if i == 1 or i == 2:
#         f1 = 0
#         f2 = 1
#     fib = f1 + f2
#     if fib > num:
#         print("no number")
#         break
#     if fib == num:
#         print("Ваше число находится под номером : ", i+1)
#         break
#     # print(i+1, fib)
#     f1 = f2
#     f2 = fib
#     i += 1


# Другое решение
# a = int(input("Введите число, проверим, принадлежит ли оно ряду Фибоначи : "))
# if a == 0:
#     print(1)
# else:
#     fib1, fib2 = 0, 1
#     n = 1
#     while fib2 <= a:
#         if fib2 == a:
#             print(n)
#             break
#         fib1, fib2 = fib2, fib1 + fib2
#         n += 1
#     else:
#         print(-1)
