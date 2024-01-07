# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

company = {
    'Microsoft': [300, 500, -200.5, 1000],
    'IBM': [300, -500, -200.5, 1000],
    'Google': [-300, 500, 200.5, 1000]
}
def earn_count(my_dict):
    for comp in my_dict:
        if sum(my_dict[comp]) < 0:
            return False
    return True

print(earn_count(company))