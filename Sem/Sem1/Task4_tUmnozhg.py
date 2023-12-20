for i in range (2, 11):
    res = ''
    for j in range(2, 6):
        res += f'{j:^2} x {i:^2} = {i * j:^2}\t'
    print(res)

print()
for i in range(2, 11):
    res = ''
    for j in range(6, 10):
        res += f'{j:^2} x {i:^2} = {i * j:^2}\t'
    print(res)


print()
print()


for i in range(2, 10):
    for j in range(2, 6):
        print(f"{j} x {i} = {j * i}", end="\t\t")
    print()
print()
for i in range(2, 10):
    for j in range(6, 10):
        print(f"{j} x {i} = {j * i}", end="\t\t")
    print()


print()
print()


for k in [0, 4]:
    for i in range (2, 11):
        res = ''
        for j in range(2+k, 6+k):
            res += f'{j:^2} x {i:^2} = {i * j:^2}\t'
        print(res)
    print()