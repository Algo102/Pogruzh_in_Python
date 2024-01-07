# глобальная переменая, т.к. фнутри функции только локальные
def func(y: int) -> int:
    global x
    x += 100
    print(f'In func {x = }') # Для демонстрации работы
    return y + 1

x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }')


# Не локальные переменные:
def main(a):
    x = 1
    def func(y):
        nonlocal x
        x += 100
        print(f'In func {x = }') # Для демонстрации работы
        return y + 1
    return x + func(a)

x = 42
print(f'In main {x = }')
z = main(x)
print(f'{x = }\t{z = }')


# доступ к константам
LIMIT = 1_000
def func(x, y):
    result = x ** y % LIMIT
    return result
print(func(42, 73))