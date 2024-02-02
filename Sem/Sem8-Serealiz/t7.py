# 📌 Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# 📌 Распечатайте его как pickle строку. 
import pickle

with open('sample.csv', 'r', encoding='utf-8') as file:
    data = file.readlines()
    data = [row.strip().split('|') for row in data]
    res = pickle.dumps(data)

print(res)