# 📌 Напишите программу, которая запрашивает год и проверяет его на високосность.
# 📌 Распишите все возможные проверки в цепочке elif
# 📌 Откажитесь от магических чисел
# 📌 Обязательно учтите год ввода Григорианского календаря
# 📌 В коде должны быть один input и один print

in_year = int(input('Веедите год: '))
CONST1 = 4
CONST2 = 100
CONST3 = 400
res = in_year % CONST1 == 0 and in_year % CONST2 != 0 or in_year % CONST3 == 0
print('Високосный' if res else 'Не високосный')


def func(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return 'yes'
    return 'no'


print(func(2024))


def func1(year):
    return 'yes' if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 else 'no'


print(func1(2024))
