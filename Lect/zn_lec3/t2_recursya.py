# Рекурсия эта функция которая вызывает сама себя
# Важно всегда указывать, когда фунции нужно остановиться

# Число Фибоначи
def fib(n):
    if n in [1, 2]:  # если n находится в списке среди 1 или 2, то возвращаем 1
        return 1
    return fib(n-1) + fib(n-2)


list1 = []  # Создали список в который будем добавлять ряд
for i in range(1, 10):
    # при каждой итерации мы вызываем функцию
    list1.append(fib(i))

print(list1)