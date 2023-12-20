# in для проверки входит ли элемент в множество.
my_set = {3, 4, 2, 5, 6, 1, 7}
print(42 in my_set) # False

my_set = frozenset({3, 4, 1, 2, 5, 6, 1, 7, 2, 7})
print(len(my_set)) # 7 - так как есть повторяющиеся элементы
print(my_set - {1, 2, 3}) # frozenset({4, 5, 6, 7})
print(my_set.union({2, 4, 6, 8})) # frozenset({1, 2, 3, 4, 5, 6, 7, 8})
print(my_set & {2, 4, 6, 8}) # frozenset({2, 4, 6})
# print(my_set.discard(10)) # Ошибка, т.к. нельзя изменять неизменяемое множество frozenset