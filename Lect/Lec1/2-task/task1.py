name = 'Alex'
age = None

a = 42
print(id(a))
a = 'Hello word'
print(id(a))

print(name, age, a, 456, 'text', sep=' (=^.^=) ')

res = input('Print your text: ')
print('Ты написал ', res)

age = int (input('Сколько тебе лет? '))

ADULT = 18
age1 = int(input('Введи свой возраст '))
res1 = ADULT - age1
print('До совершеннолетия тебе ', res1, ' лет')