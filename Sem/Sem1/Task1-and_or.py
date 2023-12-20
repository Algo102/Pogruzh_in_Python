in_year = int(input('Веедите год: '))
CONST1 = 4
CONST2 = 100
CONST3 = 400
res = in_year % CONST1 == 0 and in_year % CONST2 != 0 or in_year % CONST3 == 0
print('Високосный' if res else 'Не високосный')
