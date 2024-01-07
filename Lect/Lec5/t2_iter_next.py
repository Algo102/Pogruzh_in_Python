# Функция iter()
data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter) # <list_iterator object at 0x000002830EFC9630>
print(*list_iter) # 2 4 6 8
print(*list_iter) # Пусто, т.к. iter одноразовый

# Функция next(), итерирутся по элементам, без дефолта будет ошибка,
# когда эл-ты закончатся
data = [2, 4, 6]
list_iter = iter(data)
print(next(list_iter, 42)) # 2
print(next(list_iter, 42)) # 4
print(next(list_iter, 42)) # 6
print(next(list_iter, 42)) # 42
print(next(list_iter, 42)) # 42
