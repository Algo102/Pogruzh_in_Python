# Дан список повторяющихся элементов lst. Вернуть список с
# дублирующимися элементами. В результирующем списке не должно быть
# дубликатов.
import random

# На выходе:
# [1, 2, 3]

lst = [1, 1, 2, 2, 3, 3]
duplicates = set()

for item in lst:
    if lst.count(item) >= 2:
        duplicates.add(item)

result = list(duplicates)
print(result)

# Другой вариант
lst1 = [random.randint(0,10) for _ in range(20)]
print(lst1)
new_lst1 = []
for i in set(lst1): # проходим по множеству в котором уже нкт дубликатов
    if lst1.count(i) != 1: # если в списке этот элемент больше 1
        new_lst1.append(i)
print(new_lst1)
