l1 = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# Сарт: ДО Стоп:Шаг - по умолчанию - 0:до конца:1
print(l1[2:7:2]) # [6, 8, 12]
print(l1[:7:2]) # [2, 6, 8, 12]
print(l1[2::2]) # [6, 8, 12, 16]
print(l1[2:7:]) # [6, 2, 8, 10, 12]
print(l1[8:3:-1]) # [16, 14, 12, 10, 8]
print(l1[3::]) # [2, 8, 10, 12, 14, 16, 18]
print(l1[:7:]) # [2, 4, 6, 2, 8, 10, 12]
