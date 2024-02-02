import csv

# delimiter=' '  - в качестве разделителя столбцов будем использовать пробел
# quotechar='|' - если символ разделитель (пробел) есть в данных, экранируем их вертикальной чертой
# quoting=csv.QUOTE_MINIMAL - символ экранирования используем по минимум,
#     только там где он необходим для разрешения конфликта с разделителем

with (
    open('biostats_tab.csv', 'r', newline='') as f_read,
    open('new_biostats.csv', 'w', newline='', encoding='utf-8') as f_write
):
    csv_read = csv.reader(f_read, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC) # читаем
    csv_write = csv.writer(f_write, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL) # записываем
    all_data = []
    for i, line in enumerate(csv_read):
        if i == 0:
            csv_write.writerow(line) # сразу записываем заголовок
        else:
            line[2] += 1 # к возрасту прибавляем 1 год
            for j in range(2, 4 + 1): # все цифры переводим в int
                line[j] = int(line[j])
            all_data.append(line) # каждую прочитанную строку записываем в список-матрицу
    csv_write.writerows(all_data) # и этот список разом записываем в файл