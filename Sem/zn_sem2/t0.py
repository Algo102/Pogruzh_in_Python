range(3, 15, 2)  # start 3, stop 15, step 2
print(*range(15, 1, -2))  # 15 13 11 9 7 5 3  * распаковка


text = '323456'
print(text)  # 323456
print(*text)  # 3 2 3 4 5 6
print(text[::-1])  # 654323
print(*range(len(text)-1, -1, -1))  # 5 4 3 2 1 0 Индексы в обратном порядке
print(text[4:1:-2])  # 53

new_text = 'Helo world!'
for i in new_text:
    print(i, end=' ')
print()

print(*range(len(new_text)))  # 0 1 2 3 4 5 6 7 8 9 10

for i in range (len(new_text)):
    print(new_text[i:])

print(new_text[-2:])  # d!
print(int('1346кг'[:-2]))  # 1346