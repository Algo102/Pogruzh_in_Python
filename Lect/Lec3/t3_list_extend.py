a = 42
b = 'Hello world'
c = [1, 3, 5, 7]
l1 = [None]
# l1.extend(a) - ошибка, не работает с одним объектом

l1.extend(b)
print(l1)  # [None, 'H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

l1.extend(c)
print(l1)  # [None, 'H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', 1, 3, 5, 7]

l1.extend(l1) # допустимо, удваивает текущий список