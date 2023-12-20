# Сравнение типов
# Сравниваем объект с типом
data = 42
print(isinstance(data, int))

# True - подкласс целых чисел
data = True
print(isinstance(data, int))

# Спрашиваем, является ли 3,14 одним из типов
data = 3.14
print(isinstance(data, (int, float, complex)))