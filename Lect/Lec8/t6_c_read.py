import csv

# # newline чтоб корректно читать окончание строки
# # по умолчанию dialect='excel'
# with open('biostats.csv', 'r', newline='') as f:
#     csv_file = csv.reader(f)
#     for line in csv_file:
#         print(line)
#     print(type(line))


# # excel-tab для чтения формата tsv или excel_tab
# # quoting=csv.QUOTE_NONNUMERIC для того чтоб значения без ковычек воспринимало как цифры
# как подсказал GPTChat вместо dialect='excel-tab' мажно написать delimiter='\t'
with open('biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(line)
print(type(line))




# функция определяет используемый символ вместо табуляции
# def guess_delimiter(file_pat):
#     with open(file_path, 'r', newline='') as f:
#         sample = f.read(1024)  # Читаем небольшой образец файла
#         dialect = csv.Sniffer().sniff(sample)
#         return dialect.delimiter
#
# file_path = 'biostats_tab.csv'
# delimiter = guess_delimiter(file_path)
#
# with open(file_path, 'r', newline='') as f:
#     csv_file = csv.reader(f, delimiter=delimiter, quoting=csv.QUOTE_NONNUMERIC)
#     for line in csv_file:
#         print(line)