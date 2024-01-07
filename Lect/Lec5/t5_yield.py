# ГЕНЕРАТОР ФУНКЦИЙ
# def factorial(n):
#     number = 1
#     result = []
#     for i in range(1, n + 1):
#         number *= i
#         result.append(number)
#     return result
#
# for i, num in enumerate(factorial(10), start=1):
#     print(f'{i}! = {num}')

# yield превращает функцию в генератор и функция запоминает своё
# состояние: строку, на которой остановилось выполнение, значения
# локальных переменных. Повторный вызов функции продолжает работу с момента
# остановки.

def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number
#
# for i, num in enumerate(factorial(10), start=1):
#     print(f'{i}! = {num}')

my_iter = iter(factorial(4))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# print(next(my_iter)) # StopIteration