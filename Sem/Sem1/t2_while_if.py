# 📌 Работа в консоли в режиме интерпретатора Python.
# 📌 Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# 📌 Используйте while и if.
# 📌 Попробуйте разные значения e и n.

n, e = 10, 3
n_ = n
summ = 0
while n > 1:
    if n % 2 == 0:
        if not n % e == 0:
            print(n)
            summ += n
    n -= 1
print(f'Сумма нечетных элементов от {1} до {n_} и не кратных {e} равна {summ}')
