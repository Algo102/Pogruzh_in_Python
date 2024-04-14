# Вагоны в электричке пронумерованы натуральными числами, начиная с 1
# (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет электричка). В
# каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда
# и обнаружил, что его вагон имеет номер j. Он хочет определить, сколько
# всего вагонов в электричке. Напишите программу, которая будет это делать
# или сообщать, что без дополнительной информации это сделать невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

n = int(input("Введите порядковый номер вагона : "))
m = int(input("Введите пронумерованный номер вагона : "))

if n != m:
    print('В вашем поезде', n + m - 1)
else:
    print('Не достаточно информации')