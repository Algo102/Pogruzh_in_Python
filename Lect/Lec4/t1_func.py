# Функция, которая считает квадратное уравнение ax^2 + bx + c = 0
def quadratic_equations(a: int | float, b: int | float, c: int | float) -> tuple[float, float] | float | str:
# принимает три числа либо целых либо вещественных, на выходе либо 2, либо 1 число либо строку
# def quadratic_equations(a, b, c): - могли указать и так
    d = b ** 2 - 4 * a * c # поиск дескриминанта
    if d > 0: # если больше 0, то 2 икса
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    elif d == 0:
        return -b / (2 * a)
    else:
        return 'Нет решений'
print(quadratic_equations(2, -3, -9))


# Более универсальный подход, чтоб не использовать различные типы данных(вместо str - None)
def quadratic_equations_n(a: int | float, b: int | float, c: int | float) -> tuple[float, float] | float | None:
# принимает три числа либо целых либо вещественных, на выходе либо 2, либо 1 число либо строку
# def quadratic_equations(a, b, c): - могли указать и так
    d = b ** 2 - 4 * a * c # поиск дескриминанта
    if d > 0: # если больше 0, то 2 икса
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    elif d == 0:
        return -b / (2 * a)
    else:
        return None
print(quadratic_equations_n(2, -3, -9))


# Параметры по умолчанию
def quadratic_equations3(a, b=0, c=0):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
print(quadratic_equations3(2, -9))


# Не забываем писать ретурн
def no_return(data: list[int]):
    for i, item in enumerate(data):
        data[i] = item + 1
    return data # Если не писать ретурн, то подставитс ямысленно return None

my_list = [2, 4, 6, 8]
print(f'In main {my_list = }')
new_list = no_return(my_list)
print(f'{my_list = }\t{new_list = }')

# Всегда дополняем список
def from_one_to_n(n, data=[]):
    for i in range(1, n + 1):
        data.append(i)
    return data

new_list = from_one_to_n(5)
print(f'{new_list = }')
other_list = from_one_to_n(7)
print(f'{other_list = }')
# ошибка в том что список бдет постоянно дописываться
# В таком варианте будет без дописывания

# Так список создается каждый раз новый
def from_one_to_n(n, data=None):
    if data is None: # is работает быстрее чем ==
        data = []
    for i in range(1, n + 1):
        data.append(i)
    return data