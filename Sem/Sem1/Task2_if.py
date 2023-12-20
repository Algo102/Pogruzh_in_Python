while True:
    num = int(input('Input number (1-999): '))
    if num in range(1, 1000):
        if num < 10:
            res = num * num
        elif num < 100:
            res = (num // 10) * (num % 10)
        else:
            unity = num % 10
            tenner = (num % 100) // 10
            hundreds = num // 100
            res = unity * 100 + tenner * 10 + hundreds
        break
print(res)