# Кортежи
a = ()
b1 = 1,
b2 = (1,) # Ориентир на запятую, но со скобками легче понимать
c1 = 1, 2, 3,
c2 = (1, 2, 3)
d = tuple(range(3)) # Три элемента от 0, с шагом 1
print(a, b1, b2, c1, c2, d, sep='\n')

my_tuple = (2, 4, 6, 2, 8, 10, 12, 14, 16, 18)
print(my_tuple[2:6:2]) # (6, 8)
print(my_tuple[-3]) # 14
print(my_tuple.count(2)) # 2
print(f'{my_tuple = }') # my_tuple = (2, 4, 6, 2, 8, 10, 12, 14, 16, 18)
print(my_tuple.index(2, 2)) # 3
print(type('text',)) # <class 'str'>
print(type(('text',))) # <class 'tuple'>