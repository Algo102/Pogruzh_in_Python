from random import randint


# Зполнение листа рандомом и с помощью лист комлекейшн
size = int(input('Enter a size array: '))

# list2 = []
# for _ in range(size):
#     num = randint(-5, 5)
#     list2.append(num)

# Что вставляем и сколько раз
list2 = [randint(-5, 5) for _ in range(size)]
print(list2)

# Пример с лист комлекейшн с if
list2 = []
for i in range(size):
    if i % 2 == 0:
        list2.append(randint(-5, 5))
    else:
        list2.append(1)
print(list2)

# Дописывается if
list2 = [randint(-5, 5) for i in range(size) if i % 2 == 0]
print(list2)

# Если появляется else. То if и else тавится перед for
list2 = [randint(-5, 5) if i % 2 == 0 else 1 for i in range(size) ]
print(list2)
