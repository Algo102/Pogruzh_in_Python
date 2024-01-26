# Нарисовать в консоли ёлку спросив у пользователя количество рядов.
space = ' '
star = '*'

rows = int(input('Количество рядов'))
spaces = rows - 1
stars = 1

for i in range(rows):
    print((space * spaces) + (star * stars))
    stars += 2
    spaces -= 1


rows = int(input("Сколько рядов у ёлки? "))

for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * (2*i - 1)
    print(f"{spaces}{stars}")