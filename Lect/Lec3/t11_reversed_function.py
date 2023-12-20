l1 = [4, 8, 2, 9, 1, 7, 2]

# получаем не список, а объект
res = reversed(l1)
print(type(res), res)

# Чтоб получить спиок, оборачиваем его
rever_l = list(reversed(l1))
print(rever_l)

# Также можно испоьзовать в цикле
for i in reversed(l1):
    print(i)