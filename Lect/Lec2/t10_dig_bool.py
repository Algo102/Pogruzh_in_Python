DEFAULT = 42
num = int(input('Введите уровень или 0: '))
level = num or DEFAULT
print(level)
# Выражение не явно приводится к логическому типу
# при вводе 0, num становится ложью и в левел попадает дефолт


# При вводе name --> True, а если пусто, то 0 == False --> else
name = input('what is your name ')
if name:
    print('Hello' + name)
else:
    print('Anonymus, hello')

# pop возвращает последний элемент, удаляя его из коллекции
# и когда коллекция станет пустой, data --> False
data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
while data:
    print(data.pop())
