min_ = 0
max_ = 10
count = 3
num = None

while count > 0:
    print('Попытка ', count)
    count -= 1

    print('Число между', min_, 'и', max_)
    num = float(input())
    if num < min_ or num > max_:
        print('No')
    else:
        break

else:
    print('Счерпан лимит')
    quit()

print('Yes', num)