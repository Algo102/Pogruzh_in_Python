# Требуется определить, можно ли от шоколадки размером n × m долек отломить
# k долек, если разрешается сделать один разлом по прямой между дольками (то
# есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите длину шоколадки '))
m = int(input('Введите ширину шоколадки '))

k = int(input('Введите количество желаемых долек '))
if k > m * n:  # and k % m == 0 or k % n == 0:
    print('В шоколадке нет столько долек')
elif k % m == 0 or k % n == 0:
    print('Забирай')
else:
    print('Так разделить нельзя')