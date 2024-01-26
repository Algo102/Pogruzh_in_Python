# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.


def sum_list(list_n, nm1, nm2):
    sum = 0
    if nm1 > nm2:
        nm1, nm2 = nm2, nm1

    if nm1 < 1:
        nm1 = 1

    if nm2 > len(list_n):
        nm2 = len(list_n)

    for i in range(nm1, nm2 + 1):
        sum += list_n[i - 1]
    return sum

my_list = [1, 2, 6, 4, 5, 6, 7, 8, 9]
print(sum_list(my_list, 1, 3))

# Другой вариант записи
def sum_list1(list_n, nm1, nm2):
    if nm1 > nm2:
        nm1, nm2 = nm2, nm1

    # Тернарные операторы
    # nm1 = 1 if nm1 < 1 else nm1
    # nm2 = len(list_n) if nm2 > len(list_n) else nm2
    # Не нужно вгонять в рамки, т.к. сумму считали срезами, а они сами не выходят за рамки
    return sum(list_n[nm1 - 1: nm2])

my_list1 = [1, 2, 6, 4, 5, 6, 7, 8, 9]
print(sum_list1(my_list1, 1, 3))
