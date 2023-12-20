a: int = 42  # можно поменять на флоат чтоб ИДЕ не придералась
a: int | float = 42 # а лучше сделать так
b: float = float(input('Entre number: '))
a = a / b


def my_func(data: list[int, float]) -> float:
# дата принимает список из цлого ИЛИ вещественного
# функция возвращает вещественный тип
#def my_func(data): #можно и так
    res = sum(data) / len(data)
    return res

print(my_func([2, 5.5, 15, 8.0, 13.74]))