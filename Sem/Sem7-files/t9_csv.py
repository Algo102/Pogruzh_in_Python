import csv
# для работы с таблицами

# Запись в файл
# data = [['Stone', 39, 'DP', 'Show'], ['Andrey', 18, 'DP', 'Back'], ['Diana', 20, 'DP', 'Assist']]
#
# with open('example.csv', 'w', encoding='utf-8') as file:
#     csv_w = csv.writer(file, dialect='excel', delimiter=';') # делимитр можно не указывать по умолчанию ,
#     header = ['name', 'age', 'work', 'position']
#     csv_w.writerow(header)
#     for i in data:
#         csv_w.writerow(i)

# # Чтение из файла
with open('example.csv', 'r', encoding='utf-8') as file:
    csv_r = csv.reader(file, dialect='excel')
    data = [*csv_r]


print(data)