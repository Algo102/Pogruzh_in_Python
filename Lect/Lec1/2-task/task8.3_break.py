min_ = 0
max_ = 10
while True:
    print('Число между', min_, 'и', max_)
    num = float(input())
    if num < min_ or num > max_:
        print('No')
    else:
        break
print('Yes', num)