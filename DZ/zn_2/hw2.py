# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате
# по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

total = int(input("Введите сумму двух чисел "))
multipl = int(input("Введите произведение двух чисел "))

for i in range(1, multipl+1):
    if multipl / i == total - i:
        print(i, int(multipl / i))
        break
    else:
        print("Подходящих вариантов нет")


# Другое решение
# summ = int(input("Введите сумму двух чисел "))
# proizv = int(input("Введите произведение двух чисел "))
# for i in range(summ // 2 + 1):  # //2 для уменьшения итераций
#     if i * (summ - i) == proizv:
#         print(i, summ - i)
#         break
#     else:
#         print("Подходящих вариантов нет")